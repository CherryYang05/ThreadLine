"""Check repository text files and local Markdown file links without network access."""

from pathlib import Path
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".json", ".toml"}
ROOT_TEXT_FILES = {".editorconfig", ".gitattributes", ".gitignore"}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CODE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.*?)\1(?!`)", re.DOTALL)
# Handle ordinary inline links, images and reference definitions. This is not a
# complete Markdown parser; anchors and remote destinations are not checked.
INLINE_LINK = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:[ \t]+[\"'][^\n]*?[\"'])?[ \t]*\)"
)
REFERENCE_LINK = re.compile(r"^ {0,3}\[[^\]\n]+\]:[ \t]*(<[^>\n]+>|\S+)", re.MULTILINE)


def markdown_prose(text: str) -> str:
    """Mask fenced/indented code and code spans while preserving line numbers."""
    lines = []
    fence = None
    for line in text.split("\n"):
        match = FENCE.match(line)
        if fence:
            if (
                match
                and match[1][0] == fence[0]
                and len(match[1]) >= len(fence)
                and not match[2].strip()
            ):
                fence = None
            lines.append("")
        elif match:
            fence = match[1]
            lines.append("")
        elif line.startswith(("    ", "\t")):
            lines.append("")
        else:
            lines.append(line)
    return CODE_SPAN.sub(lambda match: "\n" * match[0].count("\n"), "\n".join(lines))


def main() -> int:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Cannot list repository files: {error}", file=sys.stderr)
        return 2

    errors = []
    files_checked = links_checked = 0
    for name in sorted({os.fsdecode(item) for item in result.stdout.split(b"\0") if item}):
        relative = Path(name)
        if relative.suffix.lower() not in TEXT_SUFFIXES and not (
            len(relative.parts) == 1 and name in ROOT_TEXT_FILES
        ):
            continue
        files_checked += 1
        source = ROOT / relative
        if not source.resolve().is_relative_to(ROOT):
            errors.append((name, 1, "text file points outside the repository"))
            continue
        try:
            raw = source.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            errors.append((name, raw[: error.start].count(b"\n") + 1, "invalid UTF-8"))
            continue
        except OSError as error:
            errors.append((name, 1, f"cannot read text file: {error.strerror}"))
            continue
        if b"\r" in raw:
            errors.append((name, raw[: raw.index(b"\r")].count(b"\n") + 1, "use LF line endings"))
        if raw and not raw.endswith(b"\n"):
            errors.append((name, raw.count(b"\n") + 1, "missing final newline"))
        for number, line in enumerate(text.split("\n"), 1):
            content = line.rstrip(" \t\r")
            whitespace = line[len(content) :].removesuffix("\r")
            if whitespace and not (
                relative.suffix.lower() == ".md" and content and whitespace == "  "
            ):
                errors.append((name, number, "trailing whitespace"))
        if relative.suffix.lower() != ".md":
            continue
        prose = markdown_prose(text)
        for pattern in (INLINE_LINK, REFERENCE_LINK):
            for match in pattern.finditer(prose):
                target = match[1].strip("<>")
                number = prose[: match.start()].count("\n") + 1
                try:
                    url = urlsplit(target)
                    path = unquote(url.path)
                    if url.scheme or url.netloc or not path or path.startswith("/"):
                        continue
                    links_checked += 1
                    destination = (source.parent / path).resolve()
                    if not destination.is_relative_to(ROOT):
                        errors.append((name, number, f"local link leaves repository: {target}"))
                    elif not destination.exists():
                        errors.append((name, number, f"broken local file link: {target}"))
                except (OSError, RuntimeError, ValueError):
                    errors.append((name, number, f"invalid local file link: {target}"))

    for name, number, message in errors:
        print(f"{name}:{number}: {message}", file=sys.stderr)
    status = "FAIL" if errors else "PASS"
    print(f"{status}: {files_checked} text files, {links_checked} local file links, {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
