# zonxpk.github.io

Personal GitHub Pages site for Pakawat Smutkun.

This repository is a collection of static portfolio pages and product case-study prototypes:

- `/index.html` is the main portfolio landing page.
- `/break-even/` is the **When? / กี่โมง?** cross-platform parody super-app case study with a live embedded build and architecture walkthrough.
- `/edusight/` contains the CognitiveReplay / EduSight prototype and supporting assets.
- `/thaimart/` contains the ThaiMart product-management case study prototype.
- `/performance-management/` contains the performance-review decision-report prototype.

## What’s inside

- A lightweight, no-build static site
- Custom HTML, CSS, and vanilla JavaScript
- Multiple presentation modes for hiring managers, technical leads, and recruiters
- Interactive product evidence through runnable prototypes and live embeds
- Accessibility-conscious structure with keyboard and reduced-motion support

## Local Preview

You can open the HTML files directly in a browser, or serve the repo locally:

```bash
python3 -m http.server 8000
```

Then visit:

- `http://localhost:8000/`
- `http://localhost:8000/break-even/`
- `http://localhost:8000/edusight/`
- `http://localhost:8000/thaimart/`
- `http://localhost:8000/performance-management/`

## Project Structure

```text
.
├── index.html
├── break-even/
│   └── index.html
├── edusight/
│   ├── index.html
│   ├── teacher.html
│   ├── parent.html
│   ├── js/
│   ├── css/
│   └── data/
├── performance-management/
├── thaimart/
│   ├── index.html
│   ├── 01-smartrewards.html
│   ├── 02-localpick.html
│   └── 03-vendorexpress.html
└── README.md
```

## Notes

- There is no build step for the root site.
- The `edusight` folder has its own `package.json` for targeted testing and local serving.
- Some `.bak` files are kept as backups while iterating on the ThaiMart prototype.
