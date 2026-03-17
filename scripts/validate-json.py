"""Validate a simple JSON key/value pair from a file."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: validate-json.py <file> <key> <expected>")
        return 2

    file_path = Path(sys.argv[1])
    key = sys.argv[2]
    expected = sys.argv[3]

    payload = json.loads(file_path.read_text(encoding="utf-8"))
    actual = str(payload.get(key, ""))
    if actual != expected:
        print(f"validation failed: {key} expected {expected!r} got {actual!r}")
        return 1

    print(f"validated {key}={expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
