"""Run the official validator when the empty OpenSpec scaffold gains content."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD_FILES = {".gitkeep", "README.md"}


def has_content(directory: Path, *, changes: bool = False) -> bool:
    if not directory.exists():
        return False
    ignored = SCAFFOLD_FILES | ({"archive"} if changes else set())
    return any(entry.name not in ignored for entry in directory.iterdir())


def main() -> int:
    if not (
        has_content(ROOT / "openspec" / "specs")
        or has_content(ROOT / "openspec" / "changes", changes=True)
    ):
        print("SKIP: no specs/changes yet; OpenSpec framework only.")
        return 0

    try:
        result = subprocess.run(
            ["openspec", "validate", "--all", "--strict", "--no-interactive"],
            cwd=ROOT,
            check=False,
        )
    except OSError as error:
        print(f"Cannot run OpenSpec validation: {error}. Run npm ci first.", file=sys.stderr)
        return 2
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
