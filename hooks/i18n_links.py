"""Keep strict MkDocs builds working with suffix-localized alternates.

English pages link to ``*.pt-BR.md`` siblings. Those siblings are not separate
pages in the English build; they are the Portuguese alternates. Portuguese
builds of untranslated English articles retarget ``docs/*.md`` anchors onto
the Portuguese page, which uses different heading ids.

This hook rewrites those links to absolute pages on the other language.
Source files stay unchanged.
"""

from __future__ import annotations

import posixpath
import re
from pathlib import PurePosixPath

LINK = re.compile(r"(\]\()([^)\s]+)(\))")


def _site_href(config, locale_prefix: str, page_src: str, target: str) -> str | None:
    path, sep, fragment = target.partition("#")
    if not path or path.startswith(("#", "mailto:", "http://", "https://")):
        return None
    resolved = posixpath.normpath(str(PurePosixPath(page_src).parent / path))
    if resolved.startswith("../") or not resolved.endswith(".md"):
        return None
    document = PurePosixPath(resolved)
    if document.name in {"README.md", "index.md"}:
        url_path = "" if str(document.parent) == "." else document.parent.as_posix()
    else:
        url_path = document.with_suffix("").as_posix()
    site = (config.site_url or "").rstrip("/")
    if not site:
        return None
    prefix = f"/{locale_prefix}" if locale_prefix else ""
    # site_url already includes the project path (for example /nirmata).
    base = site + prefix
    href = f"{base}/{url_path}/" if url_path else f"{base}/"
    if sep:
        href = f"{href}#{fragment}"
    return href


def _rewrite(markdown: str, page_src: str, config, locale_prefix: str, predicate) -> str:
    def replace(match: re.Match) -> str:
        target = match.group(2)
        path = target.partition("#")[0]
        if not predicate(path):
            return match.group(0)
        stripped = path
        if path.endswith(".pt-BR.md"):
            stripped = path[: -len(".pt-BR.md")] + ".md"
            target = stripped + target[len(path) :]
        href = _site_href(config, locale_prefix, page_src, target)
        if href is None:
            return match.group(0)
        return f"{match.group(1)}{href}{match.group(3)}"

    return LINK.sub(replace, markdown)


def on_page_markdown(markdown, page, config, files):
    del files
    language = config.theme.get("language") if config.theme else "en"
    src = page.file.src_uri.replace("\\", "/")
    if language == "pt-BR":
        # Untranslated English essays keep English heading anchors.
        if not src.startswith("articles/en/"):
            return markdown
        return _rewrite(
            markdown,
            src,
            config,
            "",
            lambda path: path.endswith(".md") and not path.endswith(".pt-BR.md"),
        )
    return _rewrite(
        markdown,
        src,
        config,
        "pt-BR",
        lambda path: path.endswith(".pt-BR.md"),
    )
