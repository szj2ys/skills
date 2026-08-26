#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2] / "skills"
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n(?:---|\.\.\.)\s*(?:\r?\n|$)", re.DOTALL)


def fail(errors, message):
    errors.append(message)


def main():
    errors = []
    if not ROOT.is_dir():
        fail(errors, f"missing skills directory: {ROOT}")
        print("\n".join(errors))
        return 1

    directories = sorted(path for path in ROOT.iterdir() if path.is_dir())
    names = {}
    validated = 0

    for directory in directories:
        path = directory / "SKILL.md"
        label = directory.name
        if not path.is_file():
            fail(errors, f"{label}: SKILL.md is missing")
            continue

        try:
            text = path.read_text(encoding="utf-8")
            match = FRONTMATTER.match(text)
            if not match:
                raise ValueError("frontmatter delimiter is missing")
            metadata = yaml.safe_load(match.group(1))
        except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
            fail(errors, f"{label}: invalid SKILL.md frontmatter ({exc})")
            continue

        if not isinstance(metadata, dict):
            fail(errors, f"{label}: frontmatter must be a mapping")
            continue

        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not name.strip():
            fail(errors, f"{label}: name is missing or empty")
        elif name != directory.name:
            fail(errors, f"{label}: frontmatter name {name!r} does not match directory")
        elif name in names:
            fail(errors, f"{label}: duplicate skill name with {names[name]}")
        else:
            names[name] = label

        if not isinstance(description, str) or not description.strip():
            fail(errors, f"{label}: description is missing or empty")

        if not errors or not errors[-1].startswith(f"{label}:"):
            validated += 1

    print(f"Validated {validated} of {len(directories)} skill directories.")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
