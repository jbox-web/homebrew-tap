#!/usr/bin/env python3
"""Update version and SHA256 checksums in a Homebrew formula.

Usage:
    python3 scripts/update_formula.py \\
        --formula Formula/mcp-grimoire-server.rb \\
        --version 0.2.0 \\
        --darwin-arm64   <sha256> \\
        --darwin-x86-64  <sha256> \\
        --linux-arm64    <sha256> \\
        --linux-x86-64   <sha256>
"""
import argparse
import re
import sys
from pathlib import Path


def replace_version(content: str, version: str) -> str:
    return re.sub(r'version "\S+"', f'version "{version}"', content)


def replace_sha(content: str, platform: str, sha: str) -> str:
    """Replace the sha256 following the URL that contains `platform`."""
    pattern = re.compile(
        r'(url\s+"[^"]*' + re.escape(platform) + r'[^"]*"\s+sha256\s+)"[a-f0-9]{64}"',
        re.DOTALL,
    )
    result, n = pattern.subn(rf'\g<1>"{sha}"', content)
    if n == 0:
        print(f"ERROR: no sha256 found for platform {platform!r}", file=sys.stderr)
        sys.exit(1)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--formula", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--darwin-arm64", required=True, dest="darwin_arm64")
    parser.add_argument("--darwin-x86-64", required=True, dest="darwin_x86_64")
    parser.add_argument("--linux-arm64", required=True, dest="linux_arm64")
    parser.add_argument("--linux-x86-64", required=True, dest="linux_x86_64")
    args = parser.parse_args()

    path = Path(args.formula)
    content = path.read_text()

    content = replace_version(content, args.version)
    content = replace_sha(content, "darwin-arm64",  args.darwin_arm64)
    content = replace_sha(content, "darwin-x86_64", args.darwin_x86_64)
    content = replace_sha(content, "linux-arm64",   args.linux_arm64)
    content = replace_sha(content, "linux-x86_64",  args.linux_x86_64)

    path.write_text(content)
    print(f"Updated {path} to v{args.version}")


if __name__ == "__main__":
    main()
