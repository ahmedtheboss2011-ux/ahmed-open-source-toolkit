"""CLI for checking basic open-source repository hygiene."""

from __future__ import annotations

import argparse
from pathlib import Path

CHECKS = (
    ("README.md", "README"),
    ("LICENSE", "License"),
    (".gitignore", "Git ignore"),
    ("tests", "Tests directory"),
    (".github/workflows/ci.yml", "GitHub Actions CI"),
)


def check_repository(root: Path) -> list[tuple[str, bool]]:
    """Return (label, present) pairs for the repository essentials."""
    return [(label, (root / path).exists()) for path, label in CHECKS]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check open-source repository essentials.")
    parser.add_argument("path", nargs="?", default=".", help="Repository path (default: current directory)")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}")
        return 2

    results = check_repository(root)
    passed = sum(ok for _, ok in results)
    print(f"Open-source readiness: {passed}/{len(results)} checks passed\n")

    for label, ok in results:
        mark = "PASS" if ok else "MISS"
        print(f"[{mark}] {label}")

    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
