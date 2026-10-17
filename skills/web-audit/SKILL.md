---
name: web-audit
description: "Audit a running web app with a real browser and turn the measurements into a redesign proposal. Use when asked to audit, review, critique, or redesign a landing page or web UI, or when someone asks whether a page is accessible, fast, readable, trustworthy, or crawlable. Produces hard evidence — contrast ratios, tap-target sizes, LCP/CLS, payload budget, SSR-versus-hydrated parity, offline behaviour — and a self-contained dark-theme HTML proposal. Triggers include audit this site, redesign this landing page, 审计网站, 页面体检, 重构 landing page, 落地页重构, 可访问性检查, is this page accessible, why is this page slow."
agent_created: true
---

# Web Audit

Measure first, then propose. A redesign argument built on opinions gets argued with; one built on
numbers gets implemented.

## The one rule

**Never report a finding you did not measure.** "The contrast looks low" is not a finding.
`--fg-3 on --surface = 3.1:1, below the 4.5:1 threshold, 12 text nodes affected` is a finding.
If you cannot measure it, say you could not measure it.

## When to use

- A user asks you to audit, review, or redesign a web page or app UI.
- A user asks if a page is accessible, fast, readable, or SEO-friendly.
- You are about to propose visual changes and want to know what is actually broken first.
- Not for: pure technical SEO and indexing (`seo-launch`, `serp-seo`), Lighthouse-score
  chasing, or greenfield design with no existing page.

---

## Step 0 — Get the app running and capturable

Do not audit a source tree. Audit a live URL.

Find the start commands from `README.md` or the framework config, then confirm with HTTP status
codes rather than by assuming success:

```bash
# start the backend (background it; long-running)
(cd <repo> && <start-command> > /tmp/audit-server.log 2>&1 &)

# confirm it is actually serving before writing any script
curl -s -o /dev/null -w "root:%{http_code} api:%{http_code}\n" \
  http://127.0.0.1:8000/ http://127.0.0.1:8000/api/health
```

Build the frontend to its production bundle if the app serves one — auditing the dev server
measures HMR overhead, not the product.

---

## Step 1 — The browser launch recipe (this is the part that wastes an hour)

On this machine Playwright is available as **`playwright-core`** inside the managed Node workspace,
and the browsers are already in the shared cache. Two traps:

1. **`playwright-core` is CommonJS.** `import { chromium } from ...` fails with
   `Named export 'chromium' not found`. Use `require` in a `.cjs` file.
2. **Browsers are in the ms-playwright cache, not next to the package.** `playwright-core` has no
   bundled binary; pass `executablePath` explicitly.

Discover the paths rather than hardcoding them:

```bash
# the module
ls /Users/$USER/.workbuddy/binaries/node/workspace/node_modules/playwright-core

# the browser (headless shell is enough for screenshots + measurement and starts faster)
find ~/Library/Caches/ms-playwright -maxdepth 3 -name "chrome-headless-shell*" -o -maxdepth 3 -name "Chromium" | head
```

Then every script starts like this:

```js
// audit.cjs  —  MUST be .cjs
const { chromium } = require('/Users/<you>/.workbuddy/binaries/node/workspace/node_modules/playwright-core');
const exe = '/Users/<you>/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell';

(async () => {
  const b = await chromium.launch({ executablePath: exe });
  // ...
  await b.close();
})();
```

Run it with the managed Node and `NODE_PATH` set:

```bash
NODE_PATH=/Users/<you>/.workbuddy/binaries/node/workspace/node_modules \
  /Users/<you>/.workbuddy/binaries/node/versions/22.22.2-3/bin/node audit.cjs
```

Write the script with the Write tool, not a heredoc. Heredocs containing `${...}` template
literals get mangled by the shell and fail with `Bad substitution`.

---

## Step 2 — The five measurements that carry the argument

Run these five. Each one proves something a source-code read cannot.

### 2.1 Contrast, computed not eyeballed

Walk every text node, resolve the background it actually sits on, compute the WCAG ratio, and
flag against the correct threshold (3.0 for ≥18px or ≥14px bold, 4.5 otherwise).

Two traps here will each hand you a **confidently wrong pass**:

**Trap 1 — `opacity` is not optional.** Comparing `color` to `backgroundColor` and stopping there
reports the *undimmed* ratio. A disabled control at `opacity: .5` blends glyph and fill toward the
page together, so a button that "passes at 9.55:1" can actually render at **3.46:1**. Model the real
composite: glyph-over-fill first, then blend that whole group at the accumulated opacity.

**Trap 2 — parse colours with the browser, never a regex.** Tailwind v4 emits `oklab()` for opacity
modifiers (`bg-white/8` → `oklab(0.999 0.00004 0.00002 / 0.08)`). A `match(/[\d.]+/g)` reads that as
`rgb(1, 0, 0)` at 8%, silently lightening the reported background. Paint onto a cleared 1×1 canvas
instead and read the pixel back.

```js
const _cv = document.createElement('canvas'); _cv.width = _cv.height = 1;
const _g = _cv.getContext('2d', { willReadFrequently: true });
const parse = c => {                       // browser-native parse, handles oklab/color-mix
  _g.clearRect(0, 0, 1, 1);
  _g.fillStyle = '#000'; _g.fillStyle = String(c);
  _g.fillRect(0, 0, 1, 1);
  const d = _g.getImageData(0, 0, 1, 1).data;
  return { r: d[0], g: d[1], b: d[2], a: d[3] / 255 };
};
const over = (c, u) => ({ r: c.r*c.a + u.r*(1-c.a), g: c.g*c.a + u.g*(1-c.a), b: c.b*c.a + u.b*(1-c.a), a: 1 });

// Flatten the paint stack behind `el`, plus `el`'s own fill over that backdrop.
const stack = (el, PAGE) => {                 // PAGE = the opaque page base, e.g. {r:7,g:9,b:11}
  const chain = []; let n = el;
  while (n && n !== document.documentElement) { chain.unshift(n); n = n.parentElement; }
  let acc = PAGE, own = null, backdrop = null;
  for (const node of chain) {
    const c = parse(getComputedStyle(node).backgroundColor);
    if (node === el) { backdrop = acc; if (c.a > 0) own = over(c, acc); }
    if (c.a > 0) acc = over(c, acc);
  }
  return { backdrop: backdrop || acc, own: own || backdrop || acc };
};
// accumulate opacity from el up to <html>
let alpha = 1, n = el;
while (n && n !== document.documentElement) { alpha *= parseFloat(getComputedStyle(n).opacity || '1'); n = n.parentElement; }
const s = stack(el, PAGE);
const fade = c => ({ r: c.r*alpha + s.backdrop.r*(1-alpha), g: c.g*alpha + s.backdrop.g*(1-alpha), b: c.b*alpha + s.backdrop.b*(1-alpha) });
const fg = fade(over(parse(getComputedStyle(el).color), s.own));   // glyph over its own fill, then faded
const bg = fade(s.own);
```

Seed `PAGE` with the real opaque base colour. Deriving it from `body` fails: `background:` shorthand
with only gradients resets `background-color` to transparent, so a naive walk falls through to
`rgba(0,0,0,0)` and scores everything against pure black.

Why this measurement matters: it is the one most likely to **exonerate** a design. If it comes back
clean, say so loudly — it is the constraint the redesign must not break. Track the *lowest* ratio
too; a page passing at 9.7:1 has very different headroom from one passing at 4.6:1.

WCAG formally exempts *inactive* controls from 1.4.3, so a faded disabled button is not a
conformance failure. Report it anyway when the brief bans low-opacity text: `disabled:opacity-50`
is the usual culprit, and swapping it for an explicit muted fill plus a full-strength label
recovers the ratio without losing the unavailable affordance.

### 2.2 Tap targets, by hit-test not by bounding box

At 390×844 with `isMobile` and `hasTouch`, check every `button, a, select, textarea, [role=button],
[role=switch], [role=checkbox]`.

Two corrections to the obvious approach:

- **`getBoundingClientRect()` cannot see a `::after` hit-area overlay.** Expanding a control's touch
  target with a pseudo-element is the standard trick (`after:absolute after:size-11`), and the layout
  box still reports the small visual size. Hit-test with `document.elementFromPoint` instead — it
  returns the element that actually receives the tap, pseudo-element included.
- **Use two thresholds.** Interactive controls are held to the 44px touch floor; inline text links are
  held to WCAG 2.5.8 AA, which is **24×24**. Failing a 27×44 footer text link against 44×44 is a
  false positive that costs you credibility.

```js
const owns = (el, x, y) => { const h = document.elementFromPoint(x, y); return !!(h && (h === el || el.contains(h))); };
// only elementFromPoint can reach what is on screen, so scroll it into view first.
// `instant` overrides the page's `scroll-behavior: smooth`, which would otherwise
// animate and leave the rect stale.
el.scrollIntoView({ block: 'center', behavior: 'instant' });
const r = el.getBoundingClientRect();
const need = isControl ? 44 : 24;
const dx = Math.max(0, (need - 2) / 2 - r.width / 2), dy = Math.max(0, (need - 2) / 2 - r.height / 2);
const reach = [[cx-dx,cy],[cx+dx,cy],[cx,cy-dy],[cx,cy+dy]].every(([x,y]) => owns(el, x, y));
```

Probe **1px inside** the required square. `elementFromPoint` is half-open at the boundary, so probing
exactly on the edge reads as a miss at random and produces a flaky failure.

Why this measurement earns its keep: it reliably finds real defects — a footer link row at 20px tall,
a 32×18 switch — that no amount of visual review catches, because they look fine in a screenshot.

### 2.3 Payload, LCP and CLS

Register `PerformanceObserver` for `largest-contentful-paint` and `layout-shift` via
`addInitScript` **before** `goto`, so you capture the real first-viewport values. Read transfer sizes
from `page.on('response')` or `performance.getEntriesByType('resource')`, and group by initiator
type so you can separate script from fetch.

Also record any single API response over ~20KB that gates interactivity. A 72KB JSON payload
fetched before a control unlocks is a performance finding even when the bundle is small.

### 2.4 Weak network

Use CDP throttling, not a hope:

```js
const cdp = await ctx.newCDPSession(page);
await cdp.send('Network.enable');
await cdp.send('Network.emulateNetworkConditions', {
  offline: false, latency: 400,
  downloadThroughput: 400*1024/8, uploadThroughput: 400*1024/8,
});
```

Sample the DOM text at 2.5s and again at ~9s. What matters is **what is painted while waiting** —
if prerendered content is up early, say so; that is a genuine strength.

### 2.5 Offline and recovery

Set the context offline, navigate, and record both the rendered text and whether a service worker
was controlling. `navigator.serviceWorker.controller === false` means there is no offline story at
all — a fact worth stating plainly rather than dressing up.

---

## Step 3 — The technique most audits miss: SSR-versus-hydrated parity

Server-rendered marketing content that React destroys on hydration is a silent, common, and
completely invisible-in-the-browser defect. Crawlers see one page; humans see another.

```js
const ssrHtml  = await (await fetch(URL)).text();   // raw HTML, no JS
const hydHtml  = await page.content();              // after hydration

const strip = h => h
  .replace(/<script[\s\S]*?<\/script>/g, '')
  .replace(/<style[\s\S]*?<\/style>/g, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&#x27;/g, "'").replace(/&amp;/g, '&')
  .replace(/\s+/g, ' ').trim();

const ssrTokens = new Set(strip(ssrHtml).split(' '));
const hydTokens = new Set(strip(hydHtml).split(' '));
const lost = [...ssrTokens].filter(t => !hydTokens.has(t));
// pass condition for any redesign: lost.length === 0
```

On a real project this surfaced a hero call-to-action that existed only in the HTML source —
crawlers saw a CTA, humans never did. Make "SSR-only token set is empty" an acceptance gate.

Complement it by diffing the content model against what the app actually renders. Walk the
translation/content JSON, search the component tree for each key, and list the orphans:

```python
# for each leaf key in content/*.json -> grep app/src for the reference path
# anything unreferenced is a designed-but-dead state
```

Orphaned keys are the highest-signal finding available, because they prove the UI *regressed*: the
copy, the states and often the translations already exist and were dropped.

---

## Step 4 — Read the code for what a browser cannot show you

Measurement finds symptoms; the source finds causes. Always capture file:line references.

Look specifically for:

- **State dropped on refresh** — is the user's actual input persisted, or only an opaque job id?
- **Empty states that return `null`** rather than rendering a placeholder (causes layout jumps).
- **Cleanup routines wired only to startup**, so lifetime promises quietly stop being true.
- **Duplicated dependencies** — a UI library pulled in for two dropdowns, measured in the bundle.
- **Breakpoint-hidden navigation** with no mobile replacement.

---

## Step 5 — The output contract

Deliver a **single self-contained HTML file**, dark theme, no build step, no external requests. The
document must practice the design language it proposes.

Structure that works:

0. Executive summary — what is good and must not regress, what is wrong, the three moves.
1. What the page is today — runtime shape, limits, lifecycle, content model.
2. Findings table, severity-ranked (P0/P1/P2), each row carrying evidence and impact.
3. Reference-site teardown, split into *take* and *refuse* — with the reason for each refusal.
4. Positioning and copy, with banned words and the message hierarchy.
5. Design system — colour with measured ratios, type scale, spacing, radius, elevation, motion.
6. Component selection — adopted **and rejected**, each rejection naming the principle it violates.
7. Desktop blueprint — an inline SVG wireframe plus a per-section spec.
8. Mobile redesign — the mobile-specific decisions, with a touch-geometry table.
9. States and reliability matrix, including offline and recovery.
10. SEO and accessibility, split into fix and protect.
11. Performance budget, measured-today versus target, with the method.
12. Verification plan mapping each gate to a method and a pass condition.
13. Delivery plan in independently shippable batches.
14. Risks, explicit non-goals, and a measurable definition of done.

Craft rules:
- Every finding cites file:line or a measured number. No unsupported adjectives.
- Include the *rejected* component list. Refusing to use a library's flashy components is the
  strongest evidence of judgement available.
- Refuse to fabricate social proof, testimonials, logos or usage counters. If the reference site
  leans on them and the product has none, say so and replace them with demonstrated capability.
- Mark what the redesign must **protect** (already-clean contrast, existing CLS) separate from what
  it must fix.

---

## Pitfalls

- **A clean contrast result is a result.** Report it as a constraint to preserve, not as a
  non-finding. It reframes the whole proposal.
- **Screenshots lie about touch.** A 20px-tall link looks perfectly fine in a capture. Measure.
- **Verify a suspected visual regression from rendered pixels before "fixing" it.** A button that
  *looks* washed out in a screenshot may simply be in its correct `disabled` state. Sample the
  actual pixels and read the computed style first; inventing a fix for a non-issue is the most
  expensive mistake available here.
- **A `<label>` does not forward clicks to a Radix switch.** Radix renders `<button role="switch">`,
  and the wrapper-label proxy does *not* hold. `el.closest('label')` will vouch for a genuinely
  32×18 target. Test it: click the label text and assert `aria-checked` flipped.
- **Tailwind v4 translate utilities set the `translate` property, not `transform`.** Reading
  `getComputedStyle(el, '::after').transform` returns `none` even when `-translate-x-1/2` applied,
  which looks exactly like a broken utility. Check `.translate`.
- **Never log a computed style truncated to N characters.** A `box-shadow` sliced to 90 chars cut off
  slot 5 of 5 — the only slot carrying the real value — and produced a phantom "the shadow is
  missing" defect. Print the whole value, or assert on it.
- **Let overlays finish unmounting before hit-testing.** A vaul/Radix drawer keeps its
  `[data-slot="drawer-overlay"]` mounted during the exit transition; a fixed `waitForTimeout` will
  let it swallow every `elementFromPoint` probe beneath it. Wait for detachment:
  `page.waitForFunction(() => !document.querySelector('[data-slot="drawer-overlay"]'))`.
- **Re-check the harness's own escaping when a regex finds nothing in compiled CSS.** Class names
  escape commas (`255\,255\,255`), so a match written from the source string silently fails. Search
  for a distinctive substring instead.
- **Stale screenshots in `output/`** may predate the current design. Check mtimes, then re-capture.
  Auditing an old render produces confidently wrong conclusions.
- **Do not read the whole frontend before running it.** Start the app, capture both breakpoints,
  and let the render tell you where to read.
- **`vh` units in mobile sheets** cause jump as browser chrome resizes; the fix is `dvh`.
- **A CSS `prefers-reduced-motion` override does not stop JavaScript animation libraries.** Motion
  components need explicit `useReducedMotion()` branches.
- **Windows shell redirection** in these scripts should stay inside the repo (`output/audit-*/`),
  not in system temp, so the evidence survives the session.

## Verification checklist before you hand over

- [ ] Server confirmed up via HTTP status, not assumption.
- [ ] Desktop and mobile captured with zero console errors.
- [ ] Contrast computed on every text node **including disabled/faded ones**, colours parsed by the
      browser (not a regex), result stated with the lowest ratio.
- [ ] Tap targets hit-tested at 390×844 (not measured by bounding box), sub-threshold items listed
      per type — 44px controls, 24px inline links.
- [ ] LCP, CLS and transfer recorded; any gating API payload over 20KB named.
- [ ] Weak-network and offline behaviour sampled at two timestamps.
- [ ] SSR-versus-hydrated token diff run; the lost-token list reported.
- [ ] Content model diffed against the component tree; orphaned keys enumerated, and the count
      compared against the pre-change baseline so new orphans cannot hide.
- [ ] Every finding carries file:line or a number.
- [ ] Any suspected visual regression confirmed from rendered pixels before being written up.
- [ ] HTML proposal written and then rendered once to confirm it opens clean with no overflow.
