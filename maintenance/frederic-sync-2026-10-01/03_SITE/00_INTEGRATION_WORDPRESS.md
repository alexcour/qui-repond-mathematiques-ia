# Intégration du site existant

Les fragments HTML sont du contenu éditorial, pas un nouveau thème ni une application à déployer. Les aperçus servent à la relecture. Insérer les fragments dans les pages existantes et conserver la mise en forme, les images et les éléments de navigation pertinents.

## Ordre

1. Exporter la base, les médias et les révisions depuis WordPress ; créer un environnement de prévisualisation.
2. Exporter la liste réelle des pages, fiches, catégories et médias. Comparer avec les 135 URL de PLAN_PAGE_PAR_PAGE.html. Compléter les pages privées/brouillons et les redirections.
3. Faire les pages Publications, Vérifier, Citer, Dettes ; corriger les blocs communs de l’accueil et du tableau de bord ; mettre à jour les anciens liens.
4. Appliquer les corrections de portée aux fiches signalées. Préserver les textes d’histoire, de philosophie et de littérature. Une date ancienne peut rester correcte comme date de source.
5. Contrôler titres, menus, fil d’Ariane, extraits, cartes, SEO, OpenGraph, liens canoniques et éventuelles données JSON-LD. Ne pas laisser un ancien titre survendre le nouveau corps de page.
6. Recalculer chaque compteur dans son propre périmètre : fiches, claims, événements du pilote et théorèmes Lean sont des unités différentes.
7. Prévisualiser ordinateur et mobile ; vérifier les équations, les tableaux, les liens externes, les téléchargements et le formulaire sans envoyer de message de test réel à un tiers.
8. Après publication réelle, vider les caches concernés, relire hors session d’administration et inscrire l’intervention au journal.

## Emplacements

### 01_ACCUEIL_BLOCS

Cible : /

Remplacer les blocs de synthèse scientifique et les anciennes accroches de preuve globale. Conserver le graphisme, les parcours, le récit et les contenus philosophiques qui ne sont pas contredits.

### 02_PUBLICATIONS_ET_DEPOTS

Cible : /publications-et-depots/

Réconciliation ciblée du corps éditorial ; vérifier le slug réel avant insertion. La page publique contient déjà les sections Cayley `0.1.3-review` et CONT `0.1.0-review` : les préserver, fusionner le fragment avec l’état public courant et ne pas rétablir un snapshot plus ancien. Pour Cayley, conserver la CI actuelle `verify #4` sur le commit de fusion `5e31912134fb6303639facedf4150d32255795bd` (run `37585311793`). Ne pas déployer depuis ce kit sans relecture de la prévisualisation.

### 03_VERIFIER

Cible : /verification/

Remplacement du corps de la page de reproduction. Raccorder la variante /verifier/ selon son contenu réel, sans perdre les anciennes références.

### 04_RECHERCHE_HUMAIN_IA_AJOUT

Cible : /recherche-humain-ia/

Ajouter la section publication après la présentation de la méthode.

### 05_DETTES_PUBLIQUES

Cible : /dettes-publiques/

Remplacer la liste générale ancienne ; conserver un lien vers le snapshot historique.

### 06_TABLEAU_DE_BORD_BANDEAU

Cible : /tableau-de-bord/

Ajouter au-dessus du catalogue ; corriger aussi les titres et compteurs à partir de leur source.

### 07_UTILISER_CITER_CONTRIBUER

Cible : /utiliser-citer-contribuer/

Remplacer le corps par les règles de citation et les liens, après sauvegarde de l’ancien contenu.

### 08_REGISTRE_BANDEAU

Cible : /registre/

Ajouter avant le téléchargement CSV ; dater le CSV réel, sans modifier silencieusement ses événements.

### 09_BERNARD_RACCORD

Cible : /bernard/

Remplacer la phrase « En attente d’Alexandre : scans publiables » devenue incohérente avec la galerie déjà accessible ; conserver les réserves de droits propres aux lots non publiés.

### 10_CONTACT_BLOC

Cible : /contact/

Remplacer les appels « dépôt en cours » et « unique verrou » ; préserver le formulaire et les informations de contact.

### 11_JOURNAL_ENTREE

Cible : /journal-des-versions/

Insérer en tête après déploiement réel ; ajouter la date de l’intervention, distincte des dates de publication historiques.

### 12_LEAN_PERIMETRE

Cible : Plusieurs pages : voir inventaire

Remplacer les assertions générales de compilation non sourcées, sans démotionner une preuve possédant une pièce vérifiable.

### 13_LAMBDA_STATUT

Cible : /publications/1-v7/ et fiche de rigidité

Remplacer les blocs présentant une mesure historique comme signal actuel établi ; conserver l’état ancien avec date et statut.

### 14_ARCHIVES_T1T4

Cible : Pages citant l’ancien cadre

Ajouter à proximité des liens T1–T4 ; conserver les DOI.


## Corrections précises supplémentaires
- Dans l’accueil, remplacer « la démonstration complète, suivie » par « les résultats, leurs pièces et leurs limites ».
- Remplacer « l’unique verrou » par « les questions ouvertes, distinguées par branche ».
- Sur la page Publications, remplacer « Dépôts logiciels certifiés » par « Paquets publics de calcul et de reproductibilité ». L’archivage n’est pas une certification scientifique.
- Distinguer « date de préparation : 30 septembre » et « release GitHub : 1er octobre » pour le paquet humain–IA.
- Ne pas maintenir « 1 prépublication ouverte » sans avoir vérifié la nature des trois notices HAL ; afficher d’abord les notices individuellement.
- La page /programme/fibres-de-realisation/ a pour titre de page récupéré « Provenance », alors que son contenu porte sur les fibres. Corriger le titre SEO, le titre WordPress et le libellé du plan du site en « Fibres de réalisation ».
- Le plan du site contient deux pages « Vérifier » et deux pages « Provenance ». Examiner leur destination et leur rôle. Si elles se recouvrent, retenir une URL canonique puis faire une redirection 301 après sauvegarde ; sinon donner des titres explicites.
- Les nombres 11 et 18 de sorry, 14 et 25 théorèmes ne doivent pas être remplacés arbitrairement par un nombre unique. Un inventaire associé à un commit manque pour les comparer.
- C₂ × C₄ est bien la structure correcte des unités modulo 30 : ne pas la modifier en C₂³. 17² = 19 et 17⁴ = 1 modulo 30.
- Le spectre complet en dimension 8 et sa restriction à l’espace centré de dimension 7 doivent être distingués. Pour l’opérateur du triplet cité, le retrait du vecteur constant enlève une occurrence de la valeur propre 3.
- Sur la fiche de rigidité, « le signal λ vient de l’arithmétique, pas du pipeline » est une conclusion trop forte pour des valeurs historiques non rejouées : utiliser le fragment 13.
- Dans le Cycle du Passage, la postface technique « seulement la cohérence syntaxique » peut devenir : « Lean contrôle une dérivation de l’énoncé formel, sous les définitions et axiomes utilisés ; la correspondance avec la question mathématique et sa portée restent à examiner ». Préserver le texte poétique lui-même.
- Les clauses générales du pied de page ne doivent pas ajouter une notification préalable aux licences MIT/CC-BY des artefacts liés. Le régime des textes du site et des fac-similés reste séparé.

## Politique de références et d’indexation
Les pages publiques ne doivent pas exposer les fichiers internes du pack. Les liens doivent aller vers le travail exact : DOI de version pour reproduire ; DOI concept pour parcourir les versions ; HAL pour le texte ; GitHub pour le code. Conserver l’URL canonique actuelle du site avec www tant que la redirection sans www n’est pas vérifiée. L’échec d’accès de l’outil d’audit à la variante sans www ne démontre pas une panne générale du domaine.
