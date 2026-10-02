# Kit public de synchronisation du site et des dépôts

Ce dossier est le sous-ensemble public du pack Frédéric V4.4. Il fournit les fragments de Couretunification.fr, le plan de ses 135 URL inventoriées et les correctifs documentaires des dépôts publics. Il ne déploie pas le site. Le pack complet contenant le pilotage privé reste dans le Drive du projet.

## État réel

Les trois dépôts scientifiques `alexcour/couret-finite-verifications`, `alexcour/hol01-monodromy-p7` et `alexcour/qui-repond-mathematiques-ia` ont été mis à jour sur main ; leurs CI ont réussi sur les nouveaux commits. Les sept écritures `couret-interia` ont été refusées par l’intégration GitHub (HTTP 403, Resource not accessible by integration). Les commits et contrôles sont dans [ETAT_GITHUB.json](ETAT_GITHUB.json).

Les trois correctifs alexcour sont conservés pour traçabilité et reconnus comme déjà appliqués par le script. Les sept autres restent à exécuter avec un accès habilité. Les paramètres About, topics, Pages et descriptions de releases sont distincts des fichiers. Aucun tag ou DOI historique n’est réécrit.

## Utilisation

1. Télécharger cette branche ou la cloner. Ouvrir `03_SITE/APERCU_INDEX.html` localement et lire `03_SITE/00_INTEGRATION_WORDPRESS.md` puis `PLAN_PAGE_PAR_PAGE.html`. Les 17 fragments sont du contenu pour les pages existantes, pas un nouveau thème WordPress.
2. Sauvegarder le site, intégrer en prévisualisation, vérifier les titres, liens, équations et le rendu mobile. Publier le journal seulement après l’intervention effective.
3. Pour un dépôt couret-interia, cloner son état courant dans un répertoire séparé et créer une branche de maintenance. Depuis ce clone, exécuter le script ci-dessous en adaptant le chemin réel du kit et le nom du dépôt.

```bash
python3 /chemin/du/kit/04_GITHUB/appliquer_correctifs.py --repo couret-interia/interia-math-lab --worktree .
python3 /chemin/du/kit/04_GITHUB/appliquer_correctifs.py --repo couret-interia/interia-math-lab --worktree . --apply
git diff --check
git diff
```

Le premier appel simule, le second applique seulement après vérification de toutes les empreintes. Une divergence provoque un refus avant écriture. Fusionner les changements du mainteneur au lieu de modifier les empreintes de référence. Lire le diff, committer les seuls fichiers concernés, pousser la branche et faire relire la PR avant fusion selon les règles du dépôt.

4. Vérifier séparément les notices HAL/Zenodo et ORCID ; un changement de main ne modifie pas une archive DOI. Utiliser les identifiants existants du référentiel et consigner les réserves non levées.

## Limites scientifiques et documentaires

HOL-01 public reste un certificat fini à p=7. HOL2 présente un résultat classique, avec scindement au seul cas p=3 au premier étage. Le pilote humain–IA reste à 21 événements, 13 sources, 7 claims ; HOL2 n’est pas ajouté rétroactivement à ses CSV. Les documents du Data Descriptor restent dans leur [PR de relecture existante](https://github.com/alexcour/qui-repond-mathematiques-ia/pull/1), distincte de ce kit.

Aucune conversation privée, aucun document de pilotage privé, aucun jeton et aucun contenu scientifique des dépôts privés n’est inclus. Ce kit ne constitue pas une publication scientifique supplémentaire.
