---
name: share-page
description: Design or fix the page where a user's generated result is shared with people who have never used the product — 结果分享页, 分享链接, 裂变. Covers the recipient experience and the link lifecycle; standalone referral programs are growth-ideas.
---

# Share Page

## The one rule

**The recipient gets the shared thing immediately, sees only what the owner chose to share, and meets the product as a quiet next step.**

## Decide before designing

1. **What will the recipient do with it?** Write one sentence. Watch, listen or read (podcast, video, report, quiz result) → immersive, content-first. Act on it (pay, sign, download) → that action is the primary element.
2. **Sharing mode**: public and indexable, unlisted (bearer link), or recipient-restricted. Transactional or confidential documents keep their existing recipient checks; choose the mode with the owner's data in mind.

## Checks — walk the full journey

Generate a result → press Share → get the link → copy or native-share → open it in a separate logged-out browser → consume the artifact → refresh → revoke it → reopen.

1. **Recipient access** matches the chosen mode; unlisted and public links open without an account and the content is in the HTML.
2. **Private by design**: an unguessable token, not a sequential id; only owner-approved fields exposed; revocation also blocks the asset URLs.
3. **Preview**: server-rendered Open Graph and Twitter card from owner-approved fields; generic preview for sensitive items.
4. **Minimal chrome**: no full navigation, banners or footer link lists; one quiet "make your own" entry after the content.
5. **Narrow screens**: the main action completes without clipped controls; media loads progressively.
6. **Gone states**: deleted, revoked or unknown links show a clear message.

Use HTTP evidence for routing and metadata, browser evidence for consuming the artifact.

## Rewards — only when the user asks for them

Define the qualifying action (signup plus first use, or purchase), one reward per unique recipient, the self-referral rule, a cap, and reversal on refund. Grant once from a server-confirmed event.

## Output

The recipient sentence and sharing mode · journey checks 1–6 with evidence · changes made · reward design when requested.
