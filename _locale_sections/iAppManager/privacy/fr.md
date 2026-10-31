iHTC Studio (« nous ») a développé iAppManager (爱应用者 / 愛應用者).

## Résumé

**iHTC Studio n'exploite pas de backend pour vos données App Store Connect.** Vous vous connectez avec une **clé API** stockée dans le **Keychain de l'appareil**. Les requêtes métier vont **directement à Apple** (`api.appstoreconnect.apple.com`). **Pas de compte iHTC Studio. Pas de pub. Pas de SDK analytics / crash.** Les pourboires StoreKit optionnels sont traités par **Apple**.

## Données sur l'appareil

| Donnée | Usage |
|------|---------|
| Comptes clé API (Issuer ID, Key ID, `.p8` PEM) | Auth App Store Connect API — Keychain |
| Index de comptes / compte courant / préférences | Multi-comptes, apparence, langue, accent |
| Cache d'images distantes | Icônes d'apps & vignettes média (effaçable dans Réglages) |
| Modèles de réponse aux avis, presets de rapports / étoiles | Aides productivité locales par compte |
| Instantané widget App Group | Compteurs pipeline, thème / langue — **sur l'appareil uniquement** |

## Réseau

| Destination | Pourquoi |
|-------------|-----|
| `api.appstoreconnect.apple.com` | Toute gestion ASC (JWT signé sur l'appareil) |
| Apple iTunes Lookup (multi-régions) | Enrichissement d'icônes optionnel |
| Apple CDN / URL d'upload pré-signées | Captures, previews, upload IPA/PKG par morceaux (PUT sans Bearer) |
| `apps.apple.com` / App Store | Ouvrir les fiches produit (système / externe) |
| Client mail | Retours que vous choisissez d'envoyer |

iHTC Studio **ne reçoit pas** votre clé privée API, métadonnées d'apps, contenu IPA, rapports de ventes ni avis clients.

## Autorisations & plateforme

| Capacité | Quand | Pourquoi |
|------------|------|-----|
| Réseau sortant | Utilisation ASC | APIs Apple |
| Fichiers choisis par l'utilisateur | Upload IPA/captures, export rapports | Vous choisissez les fichiers |
| Keychain | Enregistrer / supprimer clé API | Stockage local sécurisé |
| App Group | Widgets | Partage de résumés locaux uniquement |
| Photos / share sheet (OS) | Quand vous exportez / enregistrez | Initié par l'utilisateur |

**Installation des certificats dans le Keychain système** vise **macOS**. iOS : liste / téléchargement / partage.

## Ce que nous ne faisons pas

- Pas de compte cloud iHTC Studio pour les données ASC
- Pas de pub ni trackers tiers
- Pas de vente de données personnelles
- Les widgets n'appellent pas ASC seuls

## Contact

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
