> **Documentation raccordée au portefeuille actuel — 1 October 2026.** This repository provides supporting tools, templates or community material. Passing software checks is not a mathematical proof of RH or a validation of a general scientific claim. Current bounded publications and permanent identifiers: [CURRENT_STATUS.md](CURRENT_STATUS.md) · [Couret–Unification](https://www.couretunification.fr/publications-et-depots/).

<p align="right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/interia-style/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/interia-style.svg?style=social"></a>
  <sup> · </sup>
  <a href="README_hero.md"><sup>✨</sup></a>
  <sup> · </sup>
  <a href="README_FR.md"><sup>🇫🇷</sup></a>
</p>

# 🏛️ InterIA — Corporate Style & Templates

This repository contains the **official corporate style**, **templates**, and **reference structures** used across all InterIA projects: research frameworks, math labs, proof articles, datasets, and visualizations.

It defines:

- a consistent **visual identity** (badges, headers, layout),
- bilingual **README templates** (EN/FR),
- the canonical **STYLE_GUIDE.md / STYLE_GUIDE_FR.md**,
- reproducible **repository skeletons** (InterIA v1.2, Math Lab),
- and recommended **CI/CD**, **issue templates**, **LaTeX class**, and **GitHub Pages** conventions.

This repository is the **single source of truth** for the InterIA organizational style.

---

## 🪶 About InterIA Style

The InterIA ecosystem aims to unify:

- clean documentation,
- reproducible workflows,
- bilingual accessibility,
- professional scientific presentation,
- shared templates for all teams and contributors.

Having a unified corporate style ensures that all InterIA projects — from proof frameworks (T1′–T4) to exploratory math labs — share the same structure, tone, and level of clarity.

---

## 📘 What This Repository Contains

```text

interia-style/
├── STYLE_GUIDE.md               # Main corporate style guide (EN)
├── STYLE_GUIDE_FR.md            # French version
├── templates/                   # Drop-in templates for any new repo
│    ├── README.template.md
│    ├── README_FR.template.md
│    ├── README_hero.template.md
│    ├── README_hero_FR.template.md
│    ├── CONTRIBUTING.template.md
│    ├── CODE_OF_CONDUCT.template.md
│    ├── index.template.html
│    ├── bug_report.template.yml
│    ├── feature_request.template.yml
│    ├── pull_request_template.template.md
│    ├── interia-article.template.cls
│    └── interia_init.template.py
├── examples/
│    ├── interia_v1.2_repo_structure.md        # Reference repo structure (EN)
│    ├── interia_v1.2_repo_structure_FR.md     # French version
│    ├── interia_math_lab_structure.md         # Math Lab structure (EN)
│    └── interia_math_lab_structure_FR.md      # French version
├── .github/
│    ├── ISSUE_TEMPLATE/
│    └── workflows/
└── LICENSE

```

---

## 🌐 STYLE_GUIDE (Official Corporate Rules)

The core of this repository:

- **STYLE_GUIDE.md** — English
- **STYLE_GUIDE_FR.md** — Français

These define:

- header rules (💬 Discussion · ⭐ Stars · ✨ Hero · 🇺🇸/🇫🇷 switch)
- typography conventions
- Markdown layout
- nested code block handling
- canonical structure for READMEs (EN/FR + Hero)
- best practices for CI/CD
- GitHub Pages conventions
- files that must **not** use corporate style (e.g., LaTeX sources)

Every new InterIA repository **must** follow these guides.

---

## 🧩 Templates (Drop-In)

The `templates/` folder provides ready-to-paste template files:

- README / README_FR
- README_hero / README_hero_FR
- CONTRIBUTING (EN/FR)
- CODE_OF_CONDUCT
- Issue templates
- Pull request template
- GitHub Pages `index.html`
- LaTeX class (`interia-article.cls`)
- Python init script

These ensure **instant consistency** across all InterIA repos.

---

## 📦 Examples (Reference Structures)

`examples/` contains fully documented structures:

### **1. interia_v1.2_repo_structure.md**

Complete layout for a “reference InterIA repository”:

- clean READMEs (EN/FR/hero),
- src/docs/latex/pages/.github,
- recommended CI workflows,
- and usage guidelines.

### **2. interia_math_lab_structure.md**

Reference structure for an InterIA-compliant math lab:

- notebooks (01_, 02_, 99_)
- raw/processed data
- reproducible scripts in `src/`
- reports + figures
- LaTeX notes
- GitHub Pages: Results Gallery

These serve as **gold standards** for new repositories.

---

## 🤝 Contributing

See:

- `CONTRIBUTING.template.md` (EN)
- `CONTRIBUTING_FR.template.md` (FR)

Contributions should:

- respect the STYLE_GUIDE,
- preserve bilingual balance (EN/FR),
- improve clarity and reproducibility,
- keep examples and templates up to date.

---

## 🔧 CI/CD

Included workflows:

- `markdown.yml` — Markdown linting
- `pages.yml` — GitHub Pages deployment

These are minimal and can be extended per project.

---

## 📜 License

This repository contains templates and style documentation.
Choose a license based on your organizational needs (MIT recommended).

---

## 💬 Community

Join the public InterIA discussions:

👉 <https://github.com/couret-interia/community/discussions>

We welcome ideas, improvements, and cross-project initiatives.

---

## ✨ Hero Page

A polished Hero landing page is available in:

- `README_hero.md` (EN)
- `README_hero_FR.md` (FR)

---
