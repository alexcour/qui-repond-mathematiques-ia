# Couret-Unification: A Longitudinal Dataset of Claim-State Transitions in AI-Assisted Mathematical Research

Vetoes, Refutations, Scope Restrictions, Provenance Corrections, and Finite Verifications

Alexandre Couret · Chercheur indépendant, France · ORCID 0009-0000-8246-7146

> Data Descriptor de travail v0.3 · 1er octobre 2026. Description du dataset gelé v1.1.2. Projet distinct du manuscrit existant v1.1.1 ; aucune nouvelle release, soumission ou attribution d’identifiant n’est enregistrée.

## Résumé

Nous décrivons un dataset pilote longitudinal de transitions de revendications mathématiques issu du programme Couret-Unification. Le snapshot public contient 21 événements, sept revendications et 13 sources enregistrées, répartis entre quatre trajectoires sélectionnées. Chaque événement décrit des changements de statut épistémique, documentaire, de workflow ou de diffusion, avec accès à la source, état de preuve, incertitude et lignage. Les cas comprennent veto humains, non-promotion après un test statistique rapporté, restrictions de portée, vérification finie, réfutation et restauration de provenance. La release fournit des tableaux CSV, un codebook et des contrôles Python de cohérence structurelle et d’intégrité des fichiers. Les originaux privés ne sont pas redistribués. Petit, non représentatif et partiellement reconstruit rétrospectivement, le corpus ne mesure ni la fiabilité des modèles ni les effets causaux de la collaboration humain–IA. Il permet une analyse qualitative des trajectoires et la préparation d’outils de provenance et d’annotation, sous les limites d’accès et de validation décrites.

## Contexte et résumé

Le dataset décrit des changements sélectionnés de revendications mathématiques au cours d’une recherche prolongée associant un chercheur humain et des systèmes d’IA [1,2]. Son unité d’observation est une transition reliée à une source. Une preuve finale, une publication ou une réponse conversationnelle ne remplace pas la séquence de tests, restrictions et corrections documentaires qui la précède ou la suit.

L’unité d’observation diffère de celle des benchmarks de mathématiques formelles. MiniF2F organise 488 énoncés formels dans plusieurs systèmes de preuve ; ProofNet comporte 371 exemples de mathématiques de licence associant énoncés formels, énoncés naturels et preuves naturelles [3,4]. La supervision de processus se situe à une autre échelle : PRM800K fournit des annotations humaines par étape, et les expériences associées rapportent un avantage sur la supervision du seul résultat pour les tâches MATH étudiées [5]. Des expériences ultérieures identifient une sensibilité aux procédures d’annotation et d’évaluation [6]. Ces résultats ne démontrent pas l’utilité de ce petit corpus longitudinal pour l’entraînement.

Les modèles de provenance et les représentations structurées d’assertions scientifiques préexistent à ce dataset. PROV-O, les micropublications et les nanopublications représentent déjà provenance, claims et éléments de preuve [7–9]. Ce travail documente une combinaison particulière protocole–corpus ; il ne revendique ni nouvelle ontologie générale de provenance ni priorité pour la conservation d’exemples négatifs. La release publique complète un préprint de travail existant [2] en exposant les tableaux d’événements, les règles de codage et les procédures de vérification.

## Méthodes

### Sélection des sources et construction des événements

La release est une série de cas sélectionnés dans un seul programme, et non un journal exhaustif de toutes les interactions. Elle combine documents publics de dépôts, copie privée contemporaine, rapports internes et reconstructions rétrospectives. Le dossier public n’établit ni protocole prospectif d’échantillonnage ni dénominateur complet des événements candidats. Les quatre cas doivent donc être traités comme sélectionnés de manière raisonnée, avec conservation des limites historiques dans les notes des événements.

Chaque ligne identifie la revendication, sa portée et sa version, la source, le contrôle rapporté et un changement explicite avant/après. Un identifiant enfant conserve une restriction ou une transcription sans modifier silencieusement le claim parent. Les dates peuvent désigner un jour ou un intervalle borné ; event_sequence représente l’ordre au sein d’une journée lorsqu’il est disponible. Date de source et date d’événement restent distinctes. Certains ordres sont reconstruits à partir de dépendances logiques et qualifiés dans les notes.

### Frontières de revendication et quatre dimensions de statut

Des règles documentaires ont été introduites progressivement pour séparer calculs finis, observations, énoncés conditionnels et preuves candidates des revendications plus larges. Les pièces disponibles décrivent veto humains, fichiers de statut, gates de release et contrôles structurels. Elles ne montrent pas que toutes les interactions historiques utilisaient les mêmes contraintes de prompt ni que ces règles ont causé une amélioration mesurable du comportement des modèles.

Le schéma sépare quatre dimensions de statut. Il s’agit de champs distincts soumis à des invariants croisés, et non de variables statistiquement indépendantes. Les labels contrôlés appartiennent à l’axe défini dans CODEBOOK.md ; PROPOSED, DEMOTED, VERIFIED_LOCAL, OBSERVED et NOT_PROMOTED sont des labels épistémiques, non des labels de workflow.

| Axe | Fonction | Exemples du codebook |
| --- | --- | --- |
| Épistémique | Statut mathématique ou empirique rapporté | PROPOSED, REFUTED, VERIFIED_LOCAL, NOT_PROMOTED, SCOPE_RESTRICTED, VERIFIED_FINITE, PROVED_UNREVIEWED |
| Workflow | Processus éditorial ou de release | PUBLICATION_PLANNED, BLOCKED, INTERNAL_RC, INTERNAL_CORRECTED, RELEASE_READY, RELEASED, HAL_READY |
| Diffusion | Visibilité rapportée | PRIVATE, PRIVATE_INTERNAL, PUBLIC |
| Documentaire ou record | État de la trace du claim | RECORDED, REPORTED_MISSING, REDERIVED, RESTORED_ANTERIORITY, MISTRANSCRIBED, DETECTED_UNCORRECTED |

NA est également un état autorisé selon les règles du schéma. Le tableau fournit des exemples sans remplacer les vocabulaires contrôlés complets. Le champ documentary_state décrit la manière dont l’événement est documenté ; il est distinct de record_status_before et record_status_after. Le champ evidence_state, relatif à la source, est lui aussi séparé des quatre axes avant/après.

### État de preuve et limites d’accès

Le registre attribue un état de preuve par défaut à chaque source. Le codebook distingue PRIMARY_PUBLIC, PRIMARY_INTERNAL, PRIMARY_PRIVATE_COPY, SECONDARY_PUBLIC, SECONDARY_INTERNAL et RAW_PRESENT_REPLAYED. Une dérogation au niveau événement exige une justification EVIDENCE_OVERRIDE. Le caractère primaire ou secondaire concerne l’acte documenté : un changelog public peut être primaire pour un retrait et secondaire pour le candidat antérieur qu’il rapporte.

Les conversations privées, originaux de courriels et rapports internes complets ne sont pas redistribués. Les localisateurs non publics utilisent NOT_REDISTRIBUTED::<source_id> ; les notes libres ont été réduites pour supprimer des localisateurs privés non nécessaires. Ces mesures délimitent la représentation publique sans rendre les originaux accessibles. Elles n’établissent ni anonymisation complète ni constat général de conformité éthique. Originaux indisponibles, attribution incertaine et calculs historiques non rejoués limitent la vérification indépendante.

### Nouveauté et révisions ultérieures

Validité mathématique et nouveauté sont deux questions distinctes. Identifier un théorème classique ne le rend pas faux. Le schéma v1.1.2 n’a pas de champ dédié novelty_status, et HOL2-C/D ne figurent pas dans ses 21 événements. Les discussions ultérieures sur HOL2 peuvent motiver des événements sourcés dans une version future ; elles ne constituent pas un événement de réfutation de nouveauté dans ce snapshot. Un axe de nouveauté proposé relève d’une future décision de schéma, non d’une fonctionnalité de v1.1.2.

## Description des fichiers

L’objet diffusé est le paquet public de reproductibilité [1]. Le paquet v1.1.0, le dataset v1.1.2 et le manuscrit existant v1.1.1 désignent des objets différents. Le dépôt contient les fichiers principaux suivants, dont les chemins sont relatifs à sa racine.

| Fichier | Contenu |
| --- | --- |
| data/events_v1.1.2.csv | CSV UTF-8 ; événements de transition, 36 champs |
| data/sources_v1.1.2.csv | CSV UTF-8 ; registre des sources, 9 champs |
| CODEBOOK.md | Champs, vocabulaires contrôlés et invariants structurels |
| POSITIONING_AND_RELATED_WORK.md | Positionnement conceptuel ; aucun mapping PROV-O ou JSON-LD implémenté n’est annoncé |
| PUBLIC_SOURCE_BOUNDARY.md | Représentation publique et règles de non-redistribution |
| POST_FREEZE_NOTES.md | Notes contextuelles ou de gouvernance hors tableaux gelés |
| CONTROL_DESIGN.md | Plan d’étude future, non étude contrôlée accomplie |
| scripts/verify_release.py | Point d’entrée orchestrant validateurs, tests de mutation, contrôles descriptifs et manifeste |
| metadata/ et MANIFEST_SHA256.txt | Versions, empreintes des fichiers gelés et manifeste public |
| CITATION.cff et .zenodo.json | Métadonnées de citation et de dépôt ou archive |

Les deux tables se joignent par source_id. Les événements contiennent aussi event_id, case_id, claim_id, claim_parent_id, lineage_relation, dates, attribution des acteurs, formulation et portée du claim, description des contrôles, états avant/après, incertitude et notes. Les valeurs facultatives vides, NA, UNKNOWN et NOT_REDISTRIBUTED ont des sens différents et ne doivent pas devenir une unique catégorie de valeur manquante. Le codebook et le validateur définissent les valeurs autorisées ; les fréquences observées ne définissent pas le schéma.

Les artefacts mathématiques associés conservent leurs propres releases et procédures de validation. HOL-01 est un certificat fini exact séparé pour p=7 [10]. Le pilote n’est ni un projet Lean embarqué ni une distribution de tous les scripts de vérification finie, certificats Barning–Hall, rapports privés ou documents historiques T1′–T4. L’interprétation globale T1′–T4 est supersédée ; cela n’invalide pas uniformément chaque composant historique.

## Aperçu des données

Le snapshot contient 21 événements, sept identifiants de revendication et 13 sources. Les dates encodées vont du 24 juillet 2025 au 28 septembre 2026 ; elles ne décrivent pas une observation continue. Le registre contient trois entrées PUBLIC, neuf PRIVATE_INTERNAL et une PRIVATE. Onze identifiants de source sont des clés de référence directes d’événements ; deux autres sources apportent un contexte de support. Les annotations actor_type comptent 11 événements UNKNOWN, cinq HUMAN, trois AI et deux COLLECTIVE, et non des participants.

| Cas | Événements | Trajectoire enregistrée |
| --- | --- | --- |
| A | 5 | Claim arithmétique universel, veto, démotion/réfutation ; claim enfant local vérifié séparé |
| B | 3 | Alignement numérique rapporté, non-promotion après un test rapporté et prudence de formulation |
| C | 7 | Restriction de portée, certificat enfant p=7, diffusion publique et régression documentaire ultérieure |
| D | 6 | Trace de preuve, perte rapportée, redérivation, restauration de provenance et transcription erronée distincte |

## Validation technique

La commande de vérification requiert Python 3.10 ou ultérieur et la bibliothèque standard. Elle exécute le validateur structurel, quatre tests de mutation, les contrôles descriptifs, les contrôles de métadonnées et le manifeste SHA-256. Sur le snapshot vérifié, elle rapporte 517 contrôles structurels réussis et se termine par RELEASE VERIFICATION: OK. Les tests de mutation rejettent un identifiant conversationnel ambigu, un état initial de claim invalide, une dérogation de preuve non justifiée et un recodage primaire erroné.

```bash
python3 scripts/verify_release.py
```

Les contrôles couvrent unicité des identifiants, vocabulaires, références événements–sources, dates, ordonnancement, lignage, chaînage des états et règles d’axes prescrites. Ils confirment que les références des événements se résolvent ; ils n’imposent pas que chaque source de support soit une clé directement utilisée par un événement. Les mutations démontrent la détection des erreurs ciblées, non la complétude du validateur ou la vérité des claims mathématiques.

Le cas C illustre un invariant entre axes. C1 et C2 concernent C-UNIFORM, dont le statut passe de CANDIDATE_UNIFORM à SCOPE_RESTRICTED. C3 introduit l’enfant C-P7 avec epistemic_before=NA et epistemic_after=VERIFIED_FINITE. C4 change ensuite sa diffusion vers PUBLIC en conservant VERIFIED_FINITE. Réduire ce lignage à une seule chaîne terminée par PUBLIC mélangerait les identités des claims et confondrait publication et validation mathématique.

Les empreintes permettent de comparer des octets à une référence enregistrée. Elles n’authentifient pas à elles seules les originaux privés, ne prouvent pas les dates réelles des actes et n’établissent pas l’exhaustivité de l’histoire. Les empreintes des données et validateurs gelés sont séparées des métadonnées courantes. Le tag v1.1.0 original est conservé, y compris dans son état antérieur à l’insertion des DOI sur main.

La release n’établit ni recodage indépendant à l’aveugle ni accord entre annotateurs. Les mesures historiques du cas B ne sont pas rejouées par ces contrôles structurels. Les preuves mathématiques externes exigent leurs propres pièces et vérifications. Les contrôles réussis étayent ainsi la cohérence technique de la représentation publique, sous les limites sémantiques et historiques décrites.

## Conseils de réutilisation

Avant analyse, noter l’archive ou le commit choisi, exécuter le vérificateur et lire le codebook. Conserver lignage, intervalles de dates et qualifications d’accès. Les commandes suivantes reproduisent le snapshot documenté de main contenant les identifiants courants. Ce commit n’est pas rebaptisé tag archivé original.

```bash
git clone https://github.com/alexcour/qui-repond-mathematiques-ia.git
cd qui-repond-mathematiques-ia
git checkout b15eb057dcea32b8290961bdaa22909324f4aa17
python3 scripts/verify_release.py
```

Les enregistrements peuvent servir de petit jeu d’essai pour un logiciel de provenance ou un exercice d’annotation conçu séparément. Ils ne constituent pas un benchmark de transcriptions de référence arbitré indépendamment : les conversations complètes ne sont pas fournies et les labels n’ont pas été validés extérieurement à ce titre. Évaluer un classifieur exige de définir la cible, justifier les entrées, faire relire les labels indépendamment et déclarer le traitement des sources restreintes.

Les événements d’un même claim et d’un même cas sont dépendants. Une séparation aléatoire par ligne peut diffuser des informations d’une même trajectoire entre entraînement et évaluation. Toute tâche exploratoire doit préserver autant que possible les groupes de claims ou de cas et rapporter son très faible effectif utile. Ce pilote d’un seul programme ne permet ni estimation populationnelle de fiabilité IA, ni comparaison de familles de modèles, ni effet causal établi. Son utilité pour entraîner des modèles de récompense de processus n’est pas démontrée.

Les corrections et extensions doivent être versionnées avec une source et une justification. Les événements ultérieurs de preuve, nouveauté ou provenance ne doivent pas être insérés rétroactivement dans les tableaux gelés v1.1.2. Un résultat classé classique doit rester distinct d’une assertion mathématiquement réfutée.

## Disponibilité des données

Les tableaux d’événements et de sources sont accessibles dans https://github.com/alexcour/qui-repond-mathematiques-ia et dans l’archive du paquet identifiée par le DOI de version https://doi.org/10.5281/zenodo.23079572 [1]. Le DOI de série est https://doi.org/10.5281/zenodo.23079571. Le manuscrit existant associé est https://hal.science/hal-05773424 [2]. Ces identifiants désignent les objets existants, non un nouveau dépôt du Data Descriptor. Les originaux privés ne sont pas redistribués et leur accès n’est pas promis.

## Disponibilité du code

Le même dépôt fournit validateur structurel, scripts de mutation, audit descriptif et contrôles de release. Le code public, les exports CSV et la documentation du dépôt, y compris CODEBOOK.md, conservent la licence MIT. Le manuscrit narratif existant associé est consigné sous CC-BY 4.0. Ce draft ne modifie pas ces licences et n’attribue pas de droits sur les originaux privés ou tiers. La chaîne de vérification utilise Python 3.10 ou ultérieur et sa bibliothèque standard ; elle ne requiert pas d’environnement Lean, SageMath ou PARI/GP embarqué.

## Références

1. Couret, A. Qui répond des mathématiques produites par machine ? Public reproducibility package v1.1.0, frozen dataset v1.1.2 (2026). https://doi.org/10.5281/zenodo.23079572

2. Couret, A. Qui répond des mathématiques produites par machine ? Traçabilité longitudinale des transitions de revendications en recherche mathématique assistée par IA. Working preprint, internal v1.1.1 (2026). https://hal.science/hal-05773424

3. Zheng, K., Han, J. M. & Polu, S. MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics. ICLR 2022; arXiv:2109.00110v2. https://arxiv.org/abs/2109.00110v2

4. Azerbayev, Z. et al. ProofNet: Autoformalizing and Formally Proving Undergraduate-Level Mathematics. Preprint, arXiv:2302.12433 (2023). https://arxiv.org/abs/2302.12433

5. Lightman, H. et al. Let’s Verify Step by Step. arXiv:2305.20050 (2023). PRM800K data are described in this paper. https://arxiv.org/abs/2305.20050

6. Zhang, Z. et al. The Lessons of Developing Process Reward Models in Mathematical Reasoning. Findings of ACL 2025, 10495–10516 (2025). https://doi.org/10.18653/v1/2025.findings-acl.547

7. Lebo, T., Sahoo, S. & McGuinness, D. (eds). PROV-O: The PROV Ontology. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/

8. Clark, T., Ciccarese, P. N. & Goble, C. A. Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications. Journal of Biomedical Semantics 5, 28 (2014). https://doi.org/10.1186/2041-1480-5-28

9. Nanopublication Guidelines. Working draft, consulted 1 October 2026. https://nanopub.net/guidelines/working_draft/

10. Couret, A. HOL-01 exact finite monodromy certificate at p=7, version 1.1.1 (2026). https://doi.org/10.5281/zenodo.22978389

## Contributions de l’auteur

> **Emplacement pré-soumission — saisie de l’auteur requise.** Ne pas déduire les contributions de l’historique du dépôt. Compléter la déclaration de contributions dans le workflow de soumission Scientific Data actif ; conserver une déclaration dans le manuscrit uniquement si le système de soumission utilisé l’exige.

## Intérêts concurrents

> **Emplacement pré-soumission — déclaration de l’auteur requise.** Aucune déclaration d’intérêts concurrents n’est déduite du contenu public du dépôt. Compléter cette déclaration dans le workflow de soumission Scientific Data actif ; n’ajouter un texte au manuscrit que si le système de soumission utilisé l’exige.

## Financement

> **Emplacement pré-soumission — déclaration de l’auteur requise.** Aucune source de financement, subvention ni absence de financement externe n’est déduite du contenu public du dépôt. Remplacer cet emplacement par la déclaration exacte de l’auteur avant toute soumission.
