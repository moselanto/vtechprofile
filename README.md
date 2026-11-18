# VTECH Company Profile

Company profile for **VTECH Audio Visual Solutions / VTech Audio Kenya** (https://vtechaudio.co.ke), built by Pimofy Digital. Current version: **7.1.3** (see `CHANGELOG.md`).

One source, two outputs:
- **Web profile:** `index.html` (responsive; works on GitHub Pages, a subdomain such as profile.vtechaudio.co.ke, or any static host).
- **Printable PDF (landscape 16:9, 338.67 x 190.5 mm, 17 pages):** `dist/VTECH-Company-Profile.pdf`, generated from the same `index.html` with print CSS.

## Pages
1 Cover - 2 Who we are - 3 Mission and four promises - 4 What we do - 5 The VTECH difference (8 steps, Plan / Deliver) - 6-8 Solution pillars (audio; acoustics; video, conferencing and lighting) - 9 Expertise in action - 10 Industries - 11-13 Featured projects (West Nairobi School, CITAM Buruburu, Sarit Expo Centre) - 14 Case studies (PCEA Kahawa Farmers Church, All Saints Cathedral, COVO NBO) - 15 Houses of worship - 16 Brands (15 logos) - 17 Contact.

## Structure
| Path | What |
|---|---|
| `index.html` | All profile content |
| `assets/css/profile.css` | Brand styles: screen layout + `@media print` 16:9 pages |
| `assets/fonts/` | Manrope + Inter (self-hosted, same as the website) |
| `assets/img/logo-symbol-*.png` | Official VTech Audio Kenya symbol (white and purple) |
| `assets/img/g/` | Purple-graded photos used in the profile |
| `assets/img/projects/` | Real VTECH project photos (owner confirmed authority to use) |
| `assets/img/brands/` | Manufacturer logos for the brands page |
| `build/build-pdf.py` | Rebuilds the PDF with WeasyPrint |
| `docs/FACTS-NEEDED.md` | Items still worth confirming with VTECH |
| `AGENTS.md` | Rules for anyone (human or AI) editing this repo |

## Live web page (GitHub Pages)
Published from `main` / root at **https://moselanto.github.io/vtechprofile/** (Settings > Pages > Deploy from a branch > `main` / `/ (root)`, switched on 14 Nov 2026). The web page has a phone layout below 760px wide. The "Download PDF" button links to `dist/VTECH-Company-Profile.pdf`, so rebuild and commit the PDF with every change. `.nojekyll` makes GitHub serve the files as they are.

## Build the PDF
```
pip install weasyprint
python3 build/build-pdf.py
```
Or open `index.html` in Chrome > Print > Save as PDF (custom 338.67 x 190.5 mm, margins None, background graphics on).

## Brand
Black `#0A0A0A`, VTECH purple `#80008A` (gradient `#A51DB6` > `#80008A` > `#4A0352`) and white; Manrope headings, Inter body. Images prefixed `p-` are AI-generated illustrations, not project photos.
