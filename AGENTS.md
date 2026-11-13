# Rules for editing this repo

1. **Source of truth for facts** is the live site https://vtechaudio.co.ke and the repo `moselanto/vtechaudio` (`AGENTS.md`, `vtech-av/docs/HANDOVER-2026-10.md`). Do not contradict them.
2. **Never invent** clients, projects, results, team members, certifications, licences, registration numbers, prices, reviews or awards. Use only facts supplied by VTECH or published on the site. Unknown items stay as visible `<span class="todo">` / `<p class="todo">` placeholders until supplied.
3. **Contact details** (only these): +254 182 942 946 (phone and WhatsApp), info@vtechaudio.co.ke, Ground Floor, Mpaka Plaza, Mpaka Road, Westlands, Nairobi, P.O. Box 66734-00800, Mon-Fri 8:00 AM - 6:00 PM, Sat 8:00 AM - 6:30 PM. +254 728135246 is outdated.
4. Stats must match the live site (currently 42+ installations, 47 counties, 24h quote, 12mo support). Older copy saying "200+" is outdated.
5. Keep web and PDF in one source (`index.html`). After any content or style change, rebuild `dist/VTECH-Company-Profile.pdf`, check every A4 page for overflow, and commit both together.
6. Remove the `todo` placeholders only when the real fact is supplied; before a client-facing release, no `todo` may remain (`grep -n todo index.html`).
7. Record each change in `CHANGELOG.md`.
8. Peer company profiles may be used for layout ideas only. Never copy their wording, projects, case studies or photos into this profile.
