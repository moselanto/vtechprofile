#!/usr/bin/env python3
"""Build dist/VTECH-Company-Profile.pdf from index.html (A4, print CSS).
Usage: pip install weasyprint && python3 build/build-pdf.py
Alternative: open index.html in Chrome > Print > Save as PDF (A4, margins None, background graphics on).
"""
from pathlib import Path
from weasyprint import HTML
root = Path(__file__).resolve().parent.parent
out = root / "dist" / "VTECH-Company-Profile.pdf"
out.parent.mkdir(exist_ok=True)
HTML(filename=str(root / "index.html"), base_url=str(root)).write_pdf(str(out), presentational_hints=True)
print("Wrote", out)
