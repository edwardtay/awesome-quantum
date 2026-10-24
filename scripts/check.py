#!/usr/bin/env python3
"""Check this list's Markdown links and tables using only the standard library."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")


def slug(heading):
    heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def anchors(content):
    counts = Counter()
    result = set()
    for heading in re.findall(r"^#{1,6} (.+)$", content, re.MULTILINE):
        base = slug(heading)
        result.add(base if counts[base] == 0 else f"{base}-{counts[base]}")
        counts[base] += 1
    return result


def inspect_local():
    errors = []
    urls = set()
    files = sorted(ROOT.rglob("*.md"))
    files = [p for p in files if not any(x.startswith(".") for x in p.relative_to(ROOT).parts[:-1])]
    # Include the PR template explicitly; hidden metadata directories are otherwise excluded.
    template = ROOT / ".github/pull_request_template.md"
    if template.exists():
        files.append(template)
    primary_urls = []
    for path in files:
        content = path.read_text(encoding="utf-8")
        fenced = False
        table_width = None
        for number, line in enumerate(content.splitlines(), 1):
            location = f"{path.relative_to(ROOT)}:{number}"
            if line.startswith("```"):
                fenced = not fenced
                continue
            if fenced:
                continue
            if line.rstrip() != line:
                errors.append(f"{location}: trailing whitespace")
            if line.startswith("| "):
                width = len(re.split(r"(?<!\\)\|", line)) - 2
                if table_width is not None and width != table_width:
                    errors.append(f"{location}: table width {width}, expected {table_width}")
                table_width = width
                first = LINK.search(line)
                if path.name == "README.md" and first and first.group(1).startswith("https://"):
                    primary_urls.append(first.group(1))
            else:
                table_width = None
            for destination in LINK.findall(line):
                parts = urllib.parse.urlsplit(destination)
                if parts.scheme in ("http", "https"):
                    if parts.scheme != "https":
                        errors.append(f"{location}: use HTTPS: {destination}")
                    urls.add(urllib.parse.urldefrag(destination)[0])
                    continue
                if parts.scheme:
                    errors.append(f"{location}: unsupported link scheme: {destination}")
                    continue
                target = (path.parent / urllib.parse.unquote(parts.path)).resolve() if parts.path else path
                if not target.is_relative_to(ROOT) or not target.exists():
                    errors.append(f"{location}: missing local target: {destination}")
                elif parts.fragment and target.suffix == ".md":
                    if urllib.parse.unquote(parts.fragment) not in anchors(target.read_text(encoding="utf-8")):
                        errors.append(f"{location}: missing heading: {destination}")
        if fenced:
            errors.append(f"{path.relative_to(ROOT)}: unclosed code fence")
    for url, count in Counter(primary_urls).items():
        if count > 1:
            errors.append(f"README.md: duplicate primary entry ({count}): {url}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    toc = readme.split("## Contents\n", 1)[1].split("\n## ", 1)[0]
    for heading in re.findall(r"^## (.+)$", readme, re.MULTILINE):
        if heading not in ("Contents", "Contributing", "Footnotes") and f"(#{slug(heading)})" not in toc:
            errors.append(f"README.md: section missing from contents: {heading}")
    return errors, urls, len(files), len(primary_urls)


def check_url(url):
    result = {"url": url}
    request = urllib.request.Request(url, headers={"User-Agent": "AwesomeQuantumLinkCheck/1.0", "Accept": "text/html,application/pdf,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            result.update(status=response.status, final_url=response.url, outcome="ok")
            content_type = response.headers.get("Content-Type", "")
            if "html" in content_type:
                body = response.read(1_500_000).decode("utf-8", errors="replace")
                title = re.search(r"<title[^>]*>(.*?)</title>", body, re.DOTALL | re.IGNORECASE)
                if title:
                    result["title"] = html.unescape(re.sub(r"\s+", " ", title.group(1))).strip()
                if urllib.parse.urlsplit(response.url).hostname == "github.com" and re.search(r"This repository was archived by the owner", body):
                    result["notice"] = "Archived repository; review placement and lifecycle description."
    except urllib.error.HTTPError as exc:
        result.update(status=exc.code, outcome="blocked" if exc.code in (403, 429) else "error", error=str(exc))
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        result.update(outcome="error", error=str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true", help="GET unique external URLs; access blocks require review")
    parser.add_argument("--report", type=Path, help="Write a JSON report (requires --network)")
    args = parser.parse_args()
    if args.report and not args.network:
        parser.error("--report requires --network")
    errors, urls, file_count, entry_count = inspect_local()
    for error in errors:
        print(f"ERROR {error}")
    print(f"Checked {file_count} Markdown files, {entry_count} primary README entries, and {len(urls)} unique external URLs.")
    if errors:
        return 1
    print("Local links, heading targets, contents, table widths, and duplicate primary entries: passed.")
    if not args.network:
        return 0
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(check_url, sorted(urls)))
    problems = [r for r in results if r["outcome"] != "ok"]
    for result in results:
        if result["outcome"] != "ok":
            print(f"{result['outcome'].upper()} {result['url']}: {result.get('error')}")
        elif result.get("notice"):
            print(f"REVIEW {result['url']}: {result['notice']}")
        elif result["final_url"].rstrip("/") != result["url"].rstrip("/"):
            print(f"REDIRECT {result['url']} -> {result['final_url']}")
    print(f"External checks: {len(results) - len(problems)} accessible; {len(problems)} require investigation.")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps({"checked_at": datetime.now(timezone.utc).isoformat(), "results": results}, indent=2) + "\n", encoding="utf-8")
        print(f"Report: {args.report}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
