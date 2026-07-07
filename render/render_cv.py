#!/usr/bin/env python3
"""
render_cv.py — turn a tailored CV Markdown file into a sleek, single-page,
ATS-friendly PDF (single column, no graphics/tables, selectable text).

Usage:
    python render_cv.py my_cv.md                 # -> my_cv.pdf
    python render_cv.py my_cv.md out/cv.pdf       # explicit output
    python render_cv.py my_cv.md --size letter    # US Letter (default: A4)

Deps:  pip install markdown weasyprint
"""
import sys, argparse
import markdown
from weasyprint import HTML

# ── Sleek 1-page CV stylesheet (single column, ATS-safe, print-tight) ──────────
def css(page_size: str) -> str:
    return f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@page {{ size: {page_size}; margin: 0.6in 0.7in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Inter','Helvetica Neue',Helvetica,Arial,sans-serif;
        font-size: 9.5pt; line-height: 1.42; color: #1a1a1a; }}
h1 {{ font-size: 21pt; font-weight: 700; letter-spacing: -0.5px; color: #0d0d0d; margin: 0 0 2px; }}
/* role-targeted headline (bold line right under the name) */
h1 + p strong {{ font-size: 9.5pt; font-weight: 600; color: #444; }}
h1 + p {{ margin: 0 0 4px; }}
/* contact line (email · phone · links) */
h1 + p + p {{ font-size: 8.5pt; color: #555; margin: 0 0 6px; }}
h2 {{ font-size: 10.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;
      color: #0d0d0d; border-bottom: 1px solid #ccc; padding-bottom: 2px; margin: 11px 0 5px; }}
h3 {{ font-size: 10pt; font-weight: 600; color: #111; margin: 7px 0 0; }}
/* company | dates line */
h3 + p {{ font-size: 9pt; font-weight: 600; color: #555; margin: 0 0 2px; }}
ul {{ margin: 2px 0 4px; padding-left: 15px; }}
li {{ margin: 1px 0; }}
p {{ margin: 2px 0; }}
strong {{ font-weight: 600; }}
hr {{ border: none; border-top: 1px solid #ddd; margin: 6px 0; }}
"""

def md_to_pdf(md_path: str, pdf_path: str, page_size: str = "A4"):
    with open(md_path, encoding="utf-8") as f:
        body = markdown.markdown(f.read(), extensions=["extra", "nl2br"])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css(page_size)}</style></head><body>{body}</body></html>"
    HTML(string=html).write_pdf(pdf_path)
    print(f"✓ {pdf_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Render a CV markdown file to a sleek 1-page PDF.")
    ap.add_argument("md", help="input CV markdown file")
    ap.add_argument("out", nargs="?", help="output PDF path (default: same name, .pdf)")
    ap.add_argument("--size", default="A4", choices=["A4", "letter"], help="page size (default A4)")
    a = ap.parse_args()
    out = a.out or (a.md.rsplit(".", 1)[0] + ".pdf")
    md_to_pdf(a.md, out, "Letter" if a.size == "letter" else "A4")
