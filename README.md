# VTECH Company Profile

Company profile for **VTECH Audio Visual Solutions** (https://vtechaudio.co.ke), built by Pimofy Digital.

One source, two outputs:
- **Web profile:** `index.html` (responsive; works on GitHub Pages, a subdomain such as profile.vtechaudio.co.ke, or any static host).
- **Printable PDF (A4, 17 pages):** `dist/VTECH-Company-Profile.pdf`, generated from the same `index.html` with print CSS.

## Structure
| Path | What |
|---|---|
| `index.html` | All profile content (cover, contents, about, promises, services, 3 solution pillars, deliverables, process + sectors, featured project, case studies, houses of worship, brands, company info, contact) |
| `assets/css/profile.css` | Brand styles: screen layout + `@media print` A4 pages |
| `assets/fonts/` | Manrope + Inter (same self-hosted files as the website) |
| `assets/img/` | Logo and photos taken from the vtechaudio theme |
| `build/build-pdf.py` | Rebuilds the PDF with WeasyPrint |
| `docs/FACTS-NEEDED.md` | Facts and photos still to be supplied by VTECH |
| `AGENTS.md` | Rules for anyone (human or AI) editing this repo |

## Build the PDF
```
pip install weasyprint
python3 build/build-pdf.py
```
Or open `index.html` in Chrome > Print > Save as PDF (A4, margins None, Background graphics on).

## Brand
Taken from `moselanto/vtechaudio` `vtech-av/docs/STYLE-GUIDE.md`: v3 black & yellow: ink `#0B0B0B`, yellow `#FFC400` (always with black text), white; Manrope headings, Inter body; VTECH purple symbol `assets/img/vtech-symbol.png`. Images prefixed `p-` are AI-generated illustrations, not project photos.
