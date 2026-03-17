"""Create a small release manifest for artifact tracking."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

TRACKED_FILES = [
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    ".github/workflows/pr-validation.yml",
    ".github/workflows/release-promotion.yml",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def git_head() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return os.getenv("GITHUB_SHA", "unknown")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: create-release-manifest.py <output>")
        return 2

    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)

    manifest = {
        "service": "secure-docker-api",
        "branch": os.getenv("GITHUB_REF_NAME", "local"),
        "commit": git_head(),
        "environment": os.getenv("APP_ENV", "prod"),
        "files": [],
    }

    for entry in TRACKED_FILES:
        path = Path(entry)
        manifest["files"].append(
            {
                "path": entry,
                "sha256": sha256_file(path),
            }
        )

    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
