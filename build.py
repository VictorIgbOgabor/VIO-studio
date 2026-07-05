#!/usr/bin/env python3
"""
build.py — run this before every git push.

Reads the readable source pages (index.html, about.html, services.html) from
the current folder, injects the protect.js deterrent script, minifies the
HTML/CSS/JS, and writes the result to dist/. Only dist/ should be committed
and pushed to GitHub — keep the source files local and out of git if you
want the readable version to never touch a public repo.

Usage:
    python3 build.py
"""

import os
import re
import shutil
import htmlmin
from rcssmin import cssmin
from rjsmin import jsmin

SOURCE_PAGES = ["index.html", "about.html", "services.html"]
SRC_DIR = "src"
DIST_DIR = "."
PROTECT_JS_PATH = "protect.js"


def minify_inline_blocks(html: str) -> str:
    # Minify inline <style>...</style> blocks
    def style_sub(match):
        css = match.group(1)
        return "<style>" + cssmin(css) + "</style>"

    html = re.sub(r"<style>(.*?)</style>", style_sub, html, flags=re.DOTALL)

    # Minify inline <script>...</script> blocks (skip ones with a src attribute)
    def script_sub(match):
        js = match.group(1)
        if not js.strip():
            return match.group(0)
        return "<script>" + jsmin(js) + "</script>"

    html = re.sub(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", script_sub, html, flags=re.DOTALL)
    return html


def inject_protect_js(html: str, protect_js: str) -> str:
    snippet = f"<script>{jsmin(protect_js)}</script>\n</body>"
    return html.replace("</body>", snippet, 1)


def build():
    with open(PROTECT_JS_PATH) as f:
        protect_js = f.read()

    for page in SOURCE_PAGES:
        src_path = os.path.join(SRC_DIR, page)
        if not os.path.exists(src_path):
            print(f"skip (not found): {page}")
            continue

        with open(src_path, encoding="utf-8") as f:
            html = f.read()

        html = inject_protect_js(html, protect_js)
        html = minify_inline_blocks(html)
        html = htmlmin.minify(
            html,
            remove_comments=True,
            remove_empty_space=True,
            remove_all_empty_space=False,
            reduce_boolean_attributes=True,
        )

        out_path = os.path.join(DIST_DIR, page)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        before = os.path.getsize(src_path)
        after = os.path.getsize(out_path)
        print(f"{page}: {before/1024:.1f}KB -> {after/1024:.1f}KB")

    print(f"\nBuild complete. index.html, about.html, services.html at repo root are now up to date.")
    print("Commit and push as usual — src/ stays out of git via .gitignore.")


if __name__ == "__main__":
    build()
