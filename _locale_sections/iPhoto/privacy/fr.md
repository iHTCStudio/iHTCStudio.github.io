iHTC Studio (« nous », « notre » ou « notre ») a créé iPhoto (également connu sous le nom de « 爱修图 » / « 愛修圖 »). Cette page décrit nos politiques concernant les données lorsque vous utilisez l'application.

## Résumé

**iPhoto ne nécessite pas de compte et ne télécharge pas vos photos sur les serveurs iHTC Studio.** La capture, la beauté, les filtres et l'exportation s'exécutent sur votre appareil. La **synchronisation iCloud** facultative couvre uniquement les préférences, jamais les fichiers photo.

## Collecte de données

Nous n'exploitons pas de backend qui collecte vos informations personnelles :

- **Aucun compte** — Aucune inscription, e-mail ou numéro de téléphone n'est requis.
- **Aucune analyse ni publicité** — Aucune analyse, publicité ou SDK de suivi tiers.
- **Aucun téléchargement de photo pour analyse** — Les repères de visage et le rendu restent sur l'appareil.

## Comment fonctionne l'application

- **Stockage** — Les projets (original/vignette/état d'édition) se trouvent dans le bac à sable de l'application. Les miniatures des widgets utilisent le conteneur App Group.
- **Beauté du visage** — Voir **Données du visage et traitement de la beauté sur l'appareil** ci-dessous.
- **Bibliothèque de photos** : l'accès est limité aux importations que vous choisissez et aux sauvegardes d'exportation facultatives que vous démarrez.
- **Bande de métadonnées** — Supprime éventuellement les champs EXIF/GPS/appareil des exportations que vous créez.

## Données faciales et traitement de la beauté sur l'appareil

Lorsque vous utilisez les fonctionnalités de beauté (Capture d'aperçu en direct, Shutter Bake ou l'outil Beauté de l'éditeur), iPhoto analyse les visages **uniquement sur votre appareil** à l'aide du framework Vision d'Apple (`VNDetectFaceLandmarksRequest`). Il ne s'agit **pas** de reconnaissance faciale, de correspondance d'identité, d'enregistrement biométrique ou d'authentification.

### Quelles données de visage sont traitées

- **Repères transitoires (mémoire uniquement) :** cadre de délimitation du visage, contour du visage, yeux, sourcils, lèvres externes/intérieures, pupilles et géométrie associée utilisés pour créer des masques pour des modifications cosmétiques facultatives (lisser, blanchir, affiner, yeux, dents, fard à joues, rouge à lèvres).
- **Persistance avec un projet (facultatif) :** un **rectangle de délimitation de visage normalisé** plus les **paramètres de force de beauté/couleur** choisis (`FaceBeautyEdit`), afin que les paramètres par visage puissent être restaurés lorsque vous rouvrez le projet. **Les coordonnées complètes des points de repère ne sont pas écrites sur le disque.**

### Utiliser

La géométrie du visage est utilisée uniquement pour appliquer les réglages de beauté **que** activez lors de l'aperçu de la capture, de la capture de photos, de l'aperçu de l'éditeur, de l'actualisation des vignettes et de l'exportation/partage. Il n’est pas utilisé à des fins de publicité, de profilage ou d’identification.

### Partage

**Les données faciales ne sont jamais partagées avec des tiers.** Elles ne sont pas téléchargées sur les serveurs iHTC Studio ni sur aucune API d'analyse cloud. La synchronisation facultative iCloud Key-Value couvre **les préférences uniquement** (par exemple, la langue, le thème, les bascules de capture de recette de beauté) et **ne synchronise pas les photos ni les points de repère du visage**.

### Lieu de stockage

- Photos et fichiers de modification de projet : **bac à sable d'application sur votre appareil**
- Repères transitoires : **RAM uniquement** (effacés lorsque vous quittez l'éditeur / vider le cache d'analyse)
- Miniatures du widget : groupe d'applications sur votre appareil (images rendues, pas d'ensembles de données de points de repère)

### Conservation et suppression

- Les repères transitoires n'existent que pendant le traitement et sont ensuite supprimés.
- Les zones de visage et les paramètres de beauté persistants restent **uniquement tant que vous conservez le projet photo associé**.
- **Supprimez** un projet, **réinitialisez** les modifications ou **désinstallez** l'application pour supprimer les métadonnées de visage et les photos locales associées.

### Tiers

Aucun. Toutes les analyses et rendus de visage utilisent Apple Vision et Core Image sur l'appareil.

## Données stockées sur votre appareil

| Données | Où | Objectif |
|------|-------|---------|
| Projets photo | Documents de l'application | Originaux, pouces, état de modification |
| Métadonnées de modification de la beauté du visage | État d'édition du projet (bac à sable) | Coffret visage normalisé + paramètres beauté uniquement |
| Préférences | Paramètres par défaut du groupe d'applications | Options de langue, de thème, de capture/exportation |
| Instantanés de widgets | Groupe d'applications | Projets/statistiques récents pour les widgets |
| Capturer une recette de beauté | Groupe d'applications (facultatif, rappelez-vous) | Paramètres de force et de beauté |
| Préférences iCloud | Votre KVS iCloud privé | Synchronisation des préférences facultative |

## Synchronisation iCloud

Optional sync uses Apple's `NSUbiquitousKeyValueStore` for lightweight preferences (appearance, language, export defaults, capture beauty settings, and similar). **Photo files and face landmarks are not synced.** Sync can be turned off in Settings.

## Autorisations

| Autorisation | Objectif |
|------------|---------|
| Appareil photo | Onglet Capture |
| Photothèque (lire) | Importer |
| Photothèque (ajouter uniquement) | Exportation facultative vers Photos |
| Micro | Audio en option lors de l'enregistrement vidéo avec son ; la capture de photos ne l'exige pas |

## Achats intégrés

**Tip Developer** facultatif est un achat de consommable StoreKit. Il ne déverrouille pas les fonctionnalités et ne nécessite pas de compte d'application distinct.

## Confidentialité des enfants

iPhoto ne collecte pas sciemment de données personnelles auprès des enfants. Le traitement de base reste sur l'appareil sans backend de collecte de données iHTC Studio.

## Avis de non-responsabilité

iPhoto n'est **pas affilié à Apple Inc.**

## Changements

Nous pouvons mettre à jour cette politique sur cette page. Veuillez le consulter périodiquement.

## Contacter

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
