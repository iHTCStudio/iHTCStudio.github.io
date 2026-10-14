**Dernière mise à jour :** 29 juillet 2026

iHTC Studio (« nous », « notre » ou « nos ») a créé **iDeveloper** (aussi connu sous les noms « 爱开发者 » / « 愛開發者 », Bundle ID `com.iHTCboy.iDeveloper`). Cette Politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l’app. **Apple App Review** et les utilisateurs peuvent s’appuyer sur cette page comme URL publique de confidentialité.

## Résumé (alignement sur l’étiquette de confidentialité Apple)

| Sujet | Notre pratique |
|-------|----------------|
| Compte | **Non requis** |
| Collecte de données par iHTC Studio | **Aucune donnée collectée** — nous n’exploitons **aucun** serveur qui reçoit vos entrées d’outils ou vos données personnelles |
| Réseau | Les outils et aide-mémoire fonctionnent **hors ligne** par défaut. Les outils compatibles réseau n’envoient une requête que lorsque **vous** en lancez une |
| Analyse / publicité / suivi | **Aucun** — aucun SDK tiers d’analyse, de publicité ou de suivi |
| Services Apple facultatifs | **iCloud** (votre KVS privé), pourboire **StoreKit**, destinations de partage système que vous choisissez, widgets / Live Activities / Siri fournis par Apple |

## Collecte de données

Nous ne collectons, ne vendons et ne partageons **aucune** information personnelle à des fins publicitaires ou d’analyse. Vos entrées, sorties, favoris, historique et snippets restent sur votre appareil (et, en option, dans **votre** iCloud). Ils ne sont jamais transmis aux serveurs d’iHTC Studio, car **nous n’exploitons pas de tels serveurs pour cette app**.

## Fonctionnement de l’app

- **Outils et références intégrés** — Les moteurs et le JSON des aide-mémoire sont inclus dans les bundles de l’app, du widget et de l’extension de partage.
- **Traitement sur l’appareil** — Le formatage, l’encodage, les utilitaires de chiffrement, les regex et la plupart des utilitaires s’exécutent localement.
- **Réseau sur demande** — Si un outil a besoin d’Internet, l’interface affiche une invite ; la requête n’est déclenchée que par votre action et part vers l’hôte de destination propre à cet outil — pas via un proxy d’iHTC Studio.
- **Extension de partage** — Le texte / les contenus partagés sont transmis sur votre appareil via l’App Group `group.com.iHTCboy.iDeveloper`.
- **Widgets et Live Activity** — Affichent des instantanés de contenus que vous avez déjà ouverts ou de minuteurs que vous avez lancés, via App Group / ActivityKit.
- **Pourboire facultatif** — Achat consommable **StoreKit** traité par Apple.

## Données stockées sur votre appareil

| Données | Finalité |
|---------|----------|
| Catalogue d’outils et bibliothèque de références | Outils et aide-mémoire hors ligne |
| Favoris / outils récents | Accès rapide |
| Historique des opérations | Restaurer des entrées / sorties précédentes |
| Snippets | Fragments réutilisables que vous enregistrez |
| Tampons de la boîte de partage | Transfert temporaire depuis Partager / Envoyer vers l’outil |
| Apparence et préférences | Thème, accent, langue, onglets, widgets |
| État de Concentration / Live Activity | Affichage du minuteur |
| Présentation initiale et demandes d’avis | Parcours d’accueil / d’évaluation |

## Synchronisation iCloud (facultative)

Si elle est activée, certaines préférences / états de workflow peuvent être synchronisés via **`NSUbiquitousKeyValueStore`** d’Apple, lié à **votre identifiant Apple**. Le trafic de synchronisation va vers **Apple iCloud**, pas vers iHTC Studio.

## Autorisations

iDeveloper ne demande des autorisations que lorsqu’une fonction en a besoin (par exemple la photothèque si un outil enregistre une image que vous exportez, ou le réseau lorsque vous exécutez un outil réseau). Nous ne demandons **pas** de suivi, de contacts ni de localisation précise à des fins d’analyse.

## Contact

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
