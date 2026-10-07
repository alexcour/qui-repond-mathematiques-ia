# Kit public de synchronisation du site et des dépôts

Ce dossier est le sous-ensemble public du pack Frédéric V4.4. Il fournit les fragments de Couretunification.fr, le plan de ses 135 URL inventoriées et les correctifs documentaires des dépôts publics. Il ne déploie pas le site. Le pack complet contenant le pilotage privé reste dans le Drive du projet.

## État réel

Les trois dépôts scientifiques `alexcour/couret-finite-verifications`, `alexcour/hol01-monodromy-p7` et `alexcour/qui-repond-mathematiques-ia` ont été mis à jour sur main ; leurs CI ont réussi sur les commits enregistrés. Les refus HTTP 403 observés le 1er octobre sur les sept dépôts `couret-interia` sont conservés comme historique, mais ils ne décrivent plus l’état public courant. Le contrôle du 7 octobre constate que `community`, `interia-quality`, `interia-style` et `interia-suite` portent intégralement le raccord prévu ; `.github` porte le raccord avec une formulation publique ultérieure compatible ; `interia-math-lab` et `rh-analytic-framework-t1t4` portent les bandeaux de statut mais restent privés de la seule procédure d’archivage dans `CURRENT_STATUS.md`. Les commits et contrôles sont dans [ETAT_GITHUB.json](ETAT_GITHUB.json).

Les correctifs `couret-interia` ont donc été reclassés : aucun patch restant pour les cinq dépôts raccordés ; patch résiduel limité à la procédure d’archivage pour les deux dépôts historiques. Ne pas réappliquer les patches complets du 1er octobre ni écraser les formulations publiques plus récentes. Les paramètres About, topics, Pages et descriptions de releases restent distincts des fichiers. Aucun tag ou DOI historique n’est réécrit.

## Utilisation

1. Télécharger cette branche ou la cloner. Ouvrir `03_SITE/APERCU_INDEX.html` localement et lire `03_SITE/00_INTEGRATION_WORDPRESS.md` puis `PLAN_PAGE_PAR_PAGE.html`. Les 17 fragments sont du contenu pour les pages existantes, pas un nouveau thème WordPress.
2. Sauvegarder le site, intégrer en prévisualisation, vérifier les titres, liens, équations et le rendu mobile. Publier le journal seulement après l’intervention effective.
3. Pour un dépôt `couret-interia`, consulter d’abord `04_GITHUB/manifest_correctifs.json`. Si l’état est `APPLIED_*`, aucun patch ne reste à appliquer. Pour `interia-math-lab` et `rh-analytic-framework-t1t4`, appliquer uniquement le `correctif.patch` résiduel après vérification du `CURRENT_STATUS.md` courant ; préserver les autres formulations publiques.

```bash
python3 /chemin/du/kit/04_GITHUB/appliquer_correctifs.py --repo couret-interia/interia-math-lab --worktree .
python3 /chemin/du/kit/04_GITHUB/appliquer_correctifs.py --repo couret-interia/interia-math-lab --worktree . --apply
git diff --check
git diff
```

Le premier appel simule, le second applique seulement après vérification de toutes les empreintes. Une divergence provoque un refus avant écriture. Fusionner les changements du mainteneur au lieu de modifier les empreintes de référence. Lire le diff, committer les seuls fichiers concernés, pousser la branche et faire relire la PR avant fusion selon les règles du dépôt.

4. Vérifier séparément les notices HAL/Zenodo et ORCID ; un changement de main ne modifie pas une archive DOI. Utiliser les identifiants existants du référentiel et consigner les réserves non levées.

## Limites scientifiques et documentaires

HOL-01 public reste un certificat fini à p=7. HOL2 présente un résultat classique, avec scindement au seul cas p=3 au premier étage. Le pilote humain–IA reste à 21 événements, 13 sources, 7 claims ; HOL2 n’est pas ajouté rétroactivement à ses CSV. Les documents du Data Descriptor PUB-IA-02 ont été fusionnés dans `main` par la [PR #1](https://github.com/alexcour/qui-repond-mathematiques-ia/pull/1) le 7 octobre 2026 à 19:07:28 UTC : head final `12917f4`, commit de fusion [`020c1e0`](https://github.com/alexcour/qui-repond-mathematiques-ia/commit/020c1e07a5c3a6b74d644ac556631fc1e1e7852f), [Validate public release #70 réussi](https://github.com/alexcour/qui-repond-mathematiques-ia/actions/runs/37672100663). La [copie publique fusionnée](https://github.com/alexcour/qui-repond-mathematiques-ia/tree/020c1e07a5c3a6b74d644ac556631fc1e1e7852f/manuscripts/PUB-IA-02) reste un brouillon de travail v0.3 pour relecture ; cette fusion ne vaut ni soumission ni acceptation éditoriale et ne crée aucune release scientifique ni aucun identifiant DOI/HAL. Le site reste non déployé ; les procédures d’archivage de `interia-math-lab` et `rh-analytic-framework-t1t4` restent en attente.

Aucune conversation privée, aucun document de pilotage privé, aucun jeton et aucun contenu scientifique des dépôts privés n’est inclus. Ce kit ne constitue pas une publication scientifique supplémentaire.
