> **Documentation raccordée au portefeuille actuel — 1 October 2026.** This repository provides supporting tools, templates or community material. Passing software checks is not a mathematical proof of RH or a validation of a general scientific claim. Current bounded publications and permanent identifiers: [CURRENT_STATUS.md](CURRENT_STATUS.md) · [Couret–Unification](https://www.couretunification.fr/publications-et-depots/).

<p align="right" style="float:right">
  <a href="https://github.com/couret-interia/community/discussions"><img alt="💬 Discussion" src="https://img.shields.io/badge/💬-Discussion-1e88e5?labelColor=0d47a1"></a>
  <sup> · </sup>
  <a href="https://github.com/couret-interia/interia-suite/stargazers"><img alt="⭐" src="https://img.shields.io/github/stars/couret-interia/interia-suite.svg?style=social"></a>
</p>

# 🌌 InterIA Suite

<details><summary><b>🇫🇷 Français</b> — cliquer pour déployer</summary>

> **Suite unifiée pour le style, la qualité, les cartes de structure \
et la refactorisation assistée par IA des dépôts scientifiques.**

---

## 📚 Liens rapides

- 🧭 **Aperçu canonique** : [`INTERIA_SUITE.md`](./INTERIA_SUITE.md)
- 📘 **Index des docs** : [`docs/index.md`](./docs/index.md)
- 🚀 **Commencer** : [`docs/getting_started.md`](./docs/getting_started.md)

### Dépôts de composants

- 🎨 **Style InterIA** — modèles, image de marque, guides de style
  ↳ <https://github.com/couret-interia/interia-style>

- 🧪 **InterIA Quality Pack v4** — moteur qualité modulaire, aide à la refactorisation, AI Bridge, Cosmos & Galaxies
  ↳ <https://github.com/couret-interia/interia-quality>
  ↳ PyPI : <https://pypi.org/project/interia-quality/>

- 👥 **Communauté InterIA** — discussions, gouvernance, politiques
  ↳ <https://github.com/couret-interia/community>

---

## 🧭 Qu'est-ce que InterIA Suite ?

InterIA Suite est le **point d'entrée unifié** pour :

- **style & image de marque** (Style InterIA),
- **qualité & assistance à la refactorisation** (InterIA Quality Pack),
- **cartographie de la structure documentaire** (Cosmos Map, Galaxies LaTeX & BibTeX),
- **analyse multi-repo** (Multivers),
- **refactorisations assistées par AI** via un AI Bridge basé sur JSON.

On peut le considérer comme un petit **“système d'exploitation scientifique”** pour vos dépôts.

Le dépôt `interia-suite` lui-même est :

- le **centre narratif** (`INTERIA_SUITE.md`),
- l'endroit où se trouvent les **docs d'intégration** (`docs/…`),
- l'index de tous les **dépôts de composants**.

---

## 🧩 Composants (niveau élevé)

Une description plus détaillée se trouve dans [`INTERIA_SUITE.md`](./INTERIA_SUITE.md), mais les éléments clés sont :

### 🎨 Style InterIA

- Dépôt : `interia-style`
- Fournit :
  - README / templates principaux (EN/FR),
  - GUIDE_DE_STYLE pour Markdown, LaTeX, code,
  - modèles pour les issues / PR / CI sur GitHub.

### 🧪 Pack InterIA Quality v4 (`interia-quality`)

- Dépôt : `interia-quality`
- Package PyPI : `interia-quality`
- Fonctionnalités :
  - contrôles qualité modulaires (Python / Markdown / LaTeX / BibTeX),
  - pipeline basé sur JSON : `quality_report.json`, `refactor_plan.{json,md}`,
  - AI Bridge : `ai_request.json`, `ai_response.json`, `ai_prompt.txt`,
  - carte Cosmos & chronologie, galaxies LaTeX/BibTeX, outils Multivers,
  - un **tableau** HTML local (`interia_portal.html` et amis).

### 🌐 Cosmos & Chronologie

- Cartographie de structure à dépôt unique :
  - `cosmos_map.json`, `cosmos_map_summary.json`,
  - `cosmos_timeline.json`, `cosmos_history/…`.
- Visualisé via le tableau InterIA :
  - `cosmos_explorer.html`,
  - `cosmos_timeline.html`.

### 🌠 Multivers

- Analyse structurale multi-dépôt :
  - `interia_multiverse_map.json`,
  - `interia_multiverse_matrix.json`,
  - `interia_multiverse_gravity.json`,
  - `interia_multiverse_3d.json`.
- Visualisation en 3D via `multiverse_3d.html` sur le tableau.

### 👥 Communauté InterIA

- Discussions, RFCs, gouvernance, code de conduite :
  - dépôt `community` (Discussions GitHub, modèles, politiques).

---

## 🚀 Commencer

Le manuel complet “comment faire” se trouve dans [`docs/getting_started.md`](./docs/getting_started.md).
Résumé :

### Mode 1 — Essayez-le via PyPI (`interia-quality`)

Pour une évaluation rapide dans un dépôt existant :

```bash
pip install interia-quality

cd /chemin/vers/votre/repo

# Exécutez les contrôles qualité
interia-quality

# Construire un plan de refactorisation
interia-quality refactor-plan

# Construire cosmos / galaxies
interia-quality cosmos-map
interia-quality latex-galaxy
interia-quality bib-galaxy

# Optionnel : installez et ouvrez le tableau HTML
interia-quality init-board
interia-quality portal
```

### Mode 2 — Mode intégré (intégrez le pack)

Pour les dépôts InterIA à long terme / officiels, vous pouvez **vendre** le pack complet :

- utilisez `interia_install.py` depuis le dépôt `interia-quality` pour :

  - copier `interia_quality/`,
  - copier `interia_quality/board/…`,
  - déposer un Makefile avec les cibles InterIA (`quality-all`, `portal-all`, `cosmos-map`, `multiverse-3d-html`, …).

Les détails et exemples se trouvent dans [`docs/getting_started.md`](./docs/getting_started.md).

---

## 🗺️ Comment ce dépôt s'intègre avec les autres

- Ce dépôt (`interia-suite`) est la **carte canonique** et le centre de documentation.
- `interia-quality` contient le **moteur + tableau**.
- `interia-style` contient **présentation & modèles**.
- `community` contient **personnes & processus**.

D'autres dépôts peuvent faire un lien vers celui-ci, par exemple avec :

```md
Voir l'aperçu global de InterIA Suite dans
[INTERIA_SUITE.md](https://github.com/couret-interia/interia-suite/blob/main/INTERIA_SUITE.md).
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues !
Pour les directives de la communauté, veuillez vous référer à :

- dépôt `community` — discussions et politiques
- documents partagés **CODE_OF_CONDUCT** et **CONTRIBUTING** (qui seront référencés depuis cette suite une fois stabilisés)

---

## 📜 Licence

Sauf indication contraire, les méta-documents de InterIA Suite sont publiés sous la licence MIT.
Voir `LICENSE` dans chaque dépôt de composant pour les détails.

---

<p align="center">
  Fait avec 💖 par l'équipe InterIA
</p>

</details>

<details open><summary><b>🇬🇧 English</b> — click to collapse</summary>

> **Unified suite for style, quality, structure maps and \
AI‑assisted refactors across scientific repos.**

---

## 📚 Quick links

- 🧭 **Canonical overview**: [`INTERIA_SUITE.md`](./INTERIA_SUITE.md)
- 📘 **Docs index**: [`docs/index.md`](./docs/index.md)
- 🚀 **Getting started**: [`docs/getting_started.md`](./docs/getting_started.md)

### Component repositories

- 🎨 **InterIA Style** — templates, branding, style guides
  ↳ <https://github.com/couret-interia/interia-style>

- 🧪 **InterIA Quality Pack v4** — modular quality engine, refactor assist, AI Bridge, Cosmos & Galaxies
  ↳ <https://github.com/couret-interia/interia-quality>
  ↳ PyPI: <https://pypi.org/project/interia-quality/>

- 👥 **InterIA Community** — discussions, governance, policies
  ↳ <https://github.com/couret-interia/community>

---

## 🧭 What is InterIA Suite?

InterIA Suite is the **unified entry point** for:

- **style & branding** (InterIA Style),
- **quality & refactor assistance** (InterIA Quality Pack),
- **document structure mapping** (Cosmos Map, LaTeX & BibTeX Galaxies),
- **multi‑repo analysis** (Multiverse),
- **AI‑assisted refactors** via a JSON‑first AI Bridge.

You can think of it as a small **“scientific operating system”** for your repositories.

The `interia-suite` repo itself is:

- the **narrative hub** (`INTERIA_SUITE.md`),
- the place where **onboarding docs** live (`docs/…`),
- the index of all **component repositories**.

---

## 🧩 Components (high‑level)

A more detailed description lives in [`INTERIA_SUITE.md`](./INTERIA_SUITE.md), but the core bricks are:

### 🎨 InterIA Style

- Repository: `interia-style`
- Provides:
  - README / hero templates (EN/FR),
  - STYLE_GUIDE for Markdown, LaTeX, code,
  - GitHub issue / PR / CI templates.

### 🧪 InterIA Quality Pack v4 (`interia-quality`)

- Repository: `interia-quality`
- PyPI package: `interia-quality`
- Features:
  - modular quality checks (Python / Markdown / LaTeX / BibTeX),
  - JSON‑first pipeline: `quality_report.json`, `refactor_plan.{json,md}`,
  - AI Bridge: `ai_request.json`, `ai_response.json`, `ai_prompt.txt`,
  - Cosmos map & timeline, LaTeX/BibTeX galaxies, Multiverse tools,
  - a local HTML **board** (`interia_portal.html` and friends).

### 🌐 Cosmos & Timeline

- Single‑repo structure mapping:
  - `cosmos_map.json`, `cosmos_map_summary.json`,
  - `cosmos_timeline.json`, `cosmos_history/…`.
- Visualised via the InterIA board:
  - `cosmos_explorer.html`,
  - `cosmos_timeline.html`.

### 🌠 Multiverse

- Multi‑repo structural analysis:
  - `interia_multiverse_map.json`,
  - `interia_multiverse_matrix.json`,
  - `interia_multiverse_gravity.json`,
  - `interia_multiverse_3d.json`.
- 3D visualisation via `multiverse_3d.html` on the board.

### 👥 InterIA Community

- Discussions, RFCs, governance, code of conduct:
  - `community` repo (GitHub Discussions, templates, policies).

---

## 🚀 Getting started

The full “how‑to” is in [`docs/getting_started.md`](./docs/getting_started.md).
Summary:

### Mode 1 — Try it via PyPI (`interia-quality`)

For a quick evaluation in an existing repo:

```bash
pip install interia-quality

cd /path/to/your/repo

# Run quality checks
interia-quality

# Build a refactor plan
interia-quality refactor-plan

# Build cosmos / galaxies
interia-quality cosmos-map
interia-quality latex-galaxy
interia-quality bib-galaxy

# Optional: install and open the HTML board
interia-quality init-board
interia-quality portal
```

### Mode 2 — Vendored mode (embed the pack)

For long‑lived / official InterIA repos, you can **vendor** the full pack:

- use `interia_install.py` from the `interia-quality` repo to:

  - copy `interia_quality/`,
  - copy `interia_quality/board/…`,
  - drop a Makefile with InterIA targets (`quality-all`, `portal-all`, `cosmos-map`, `multiverse-3d-html`, …).

Details and examples live in [`docs/getting_started.md`](./docs/getting_started.md).

---

## 🗺️ How this repo fits with others

- This repo (`interia-suite`) is the **canonical map** and doc hub.
- `interia-quality` contains the **engine + board**.
- `interia-style` contains **presentation & templates**.
- `community` contains **people & process**.

Other repos can link back here, for example with:

```md
See the global InterIA Suite overview in
[INTERIA_SUITE.md](https://github.com/couret-interia/interia-suite/blob/main/INTERIA_SUITE.md).
```

---

## 🤝 Contributing

Contributions are welcome!
For community guidelines, please refer to:

- `community` repo — discussions and policies
- shared **CODE_OF_CONDUCT** and **CONTRIBUTING** documents (to be referenced from this suite once stabilised)

---

## 📜 License

Unless stated otherwise, InterIA Suite meta‑documents are released under the MIT License.
See `LICENSE` in each component repository for details.

---

<p align="center">
  Made with 💖 by InterIA collaborators
</p>

</details>
