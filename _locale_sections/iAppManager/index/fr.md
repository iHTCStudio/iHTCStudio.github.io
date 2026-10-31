**Publiez plus vite. Quittez le labyrinthe du navigateur.**

iAppManager (爱应用者) est un **poste de travail natif App Store Connect** pour iPhone, iPad et Mac. Connectez-vous avec une **clé API**, conservez les identifiants dans le **Trousseau**, et communiquez **directement avec Apple** — versions, captures, IAP, TestFlight, certificats, rapports de ventes et avis clients au même endroit. **Pas de compte iHTC Studio. Pas de pub. Pas de SDK analytics. Pas de backend tiers pour vos données ASC.**

**En bref :** connexion multi-comptes par clé API · liste d'apps avec filtres plateforme et pipeline · checklist de préparation Overview · versions et soumissions review · Build Upload REST (IPA/PKG) · métadonnées et médias avec copie inter-locales · Custom Product Pages · In-App Events · App Clips · expériences store · nominations featuring · disponibilité et prix · classification · accessibilité · App Tags · IAP et abonnements · Game Center · TestFlight · avis clients · certificats et appareils · utilisateurs et rôles · rapports sales / finance / Analytics · Webhooks · widgets et deep links `iappmanager://` · English / 简体 / 繁體

> Conçu pour les indés et petites équipes qui vivent dans App Store Connect chaque semaine — un bureau qui ressemble à une app Mac, pas à une ferme d'onglets.

## Premiers pas

1. Créez une **clé API App Store Connect** (Admin ou App Manager recommandé) : App Store Connect → **Users and Access** → **Integrations** → **App Store Connect API** → créez une clé, téléchargez le **`.p8` une seule fois**, notez **Issuer ID** + **Key ID**.
2. Ouvrez iAppManager → collez Issuer ID / Key ID / PEM (ou choisissez le `.p8`) → vérifiez (`GET /v1/apps`). Les clés sont stockées dans le **Trousseau** de cet appareil.
3. Terminez l'**onboarding** court (certificats · rapports · widgets · confidentialité). Relisez les guides dans **Réglages → Aide**.
4. Dans **My Apps**, choisissez **liste / grille / cartes**, épinglez les favoris, filtrez par **plateforme** (iOS / macOS / tvOS / visionOS) ou **statut** (en vente · hors vente · en attente · en review · refusé · release développeur en attente).
5. Ouvrez une app → commencez par **Overview** (dernière version/build, raccourcis, checklist souple, soumissions récentes).
6. Parcours release : **Versions** → attacher un **Build** → **Metadata / Media** → **Review Detail** → soumettre via **Review Submissions** (ou « envoyer maintenant »).
7. Ajoutez des **widgets d'écran d'accueil** (Account Hub, Apps Pulse, Review Desk, Quick Actions) et testez `iappmanager://` depuis Raccourcis.

> Les guides **Release / IAP / TestFlight / Reports** intégrés sont à un tap (aussi via deep links).

## Pourquoi télécharger

- **Un bureau natif pour toute la publication** — fini les allers-retours entre onglets ASC pour versions, assets, IAP, TestFlight, certs et rapports.
- **Clé API, pas une danse de mots de passe** — Issuer ID + Key ID + `.p8` dans le Trousseau ; multi-comptes ; retirer un compte supprime la clé locale.
- **Envoyer des builds sans Transporter** — **Build Upload REST** WWDC25 pour IPA/PKG ; même pipeline sur iOS (gros fichiers de préférence sur Mac).
- **Guides détaillés dans l'app** — préparation release, IAP, TestFlight et rapports expliquent checks durs vs souples avant de brûler un cycle review.
- **Pipeline sur l'écran verrouillé** — les widgets reflètent en vente / attente / review / refusé / release en attente (mêmes seaux que My Apps).
- **Confidentialité par architecture** — le trafic ASC va vers `api.appstoreconnect.apple.com` ; iHTC Studio n'héberge pas vos apps, clés ou rapports.

## Fonctionnalités

### Connexion et comptes

- **Clé API uniquement** (Issuer ID / Key ID / `.p8`) — pas d'OAuth Apple ID dans l'app
- Stockage Trousseau ; **multi-comptes** ; déconnexion / suppression efface le secret local
- Guide illustré **« Obtenir une clé API »** dans l'app

### My Apps

- **Liste / grille / cartes** (liste par défaut) avec contrôle des colonnes
- **Épinglage** par compte ; filtres **plateforme** et **statut** avec cache catalogue ~10 min (rafraîchissement forcé avec progression)
- **En vente = disponible dans au moins un territoire** ; seaux pipeline indépendants de la présence storefront
- Menu contextuel : épingler, sauter aux modules, copier nom / Bundle ID / Apple ID / SKU / store · ASC · deep links / résumé ; ouvrir App Store ou ASC
- Icônes : artwork build ASC → iTunes Lookup → monogramme, cache disque

### Overview et préparation release

- Résumé dernière version/build, raccourcis modules, soumissions review récentes
- **Checklist souple** (taille capture principale, copyright, classification, etc.)
- Versions / Submissions appliquent des **bloqueurs durs** (état build, identifiants démo si requis)
- Guide : `iappmanager://release-guide`

### Versions, builds et soumissions

- Créer versions, attacher builds, soumettre / annuler, modes release (manuel / auto / planifié), release progressive, **Release Now** en attente développeur
- **Build Upload REST** IPA/PKG ; taille build ; diagnostics ; Beta App Clip ; conformité export
- **Background Assets** (`.aar`) créer / upload par morceaux / chemins External Beta et review App Store
- **Déclarations chiffrement** avec upload document ; vérification souple depuis Overview
- **Review Submissions** brouillon / ajouter items / soumettre ; « maintenant » ou « ajouter au brouillon »
- **Review Detail** — contact, compte démo, notes, pièces jointes, Routing App Coverage

### Fiche store et croissance

- **Metadata** — App Info vs Version Listing ; catégories, copyright, EULA, locale primaire ; mapping Android ; multi-locale avec ★ primaire ; **copie inter-locales**
- **Captures et previews** — par version / locale / taille appareil ; upload réservation ; copie inter-locales ; timecode poster ; couverture par assets réels
- **Poste batch assets** — upload captures/previews sur locales × tailles en un desk
- **Workbench taille de téléchargement** — inspecter tailles avec hints limites souples
- **Recherche SKU** dans My Apps ; barres d'action adaptatives sur écrans étroits
- **Custom Product Pages** — visibilité, deep links, promo, Search Keywords, médias, soumettre
- **In-App Events**, **App Clips**, **expériences store** (trafic séparé du review), **nominations featuring**
- **Disponibilité**, **prix** (choisir un price point puis appliquer — preview equalization incluse), **classification**, **accessibilité**, **App Tags**
- Formulaires fréquents : **⌘S** enregistrer sur Mac

### Monétisation et Game Center

- IAP / groupes d'abonnement, localisations, captures/notes review, disponibilité territoriale, price points
- Offres intro / promo / win-back ; **Offer Codes** ; images promo ; grace period ; URLs notifications serveur ; import/export CSV ; soumettre (y compris groupes abo)
- Guide : `iappmanager://iap-guide`
- **Game Center** — succès, leaderboards / sets, défis / activités, multijoueur, matchmaking

### TestFlight

- Groupes, liens publics, critères recrutement, métriques, invitations, testeurs individuels, builds, What to Test, licence bêta / review
- Boîte feedback et CSV + **export bulk captures pleine taille / crash logs** (dossier Mac / zip iOS + manifest)
- Guide : `iappmanager://testflight-guide`

### Certificats, utilisateurs, rapports, avis

- Certificats (CSR in-app / import) · profils · Bundle ID et capabilities · Merchant / Pass Type · appareils (**macOS** : installation Keychain)
- Invitations utilisateurs, rôles, visibilité app, provisioning ; testeurs Sandbox
- **Reports** — sales / finance / Analytics, scénarios, presets custom, **aperçu TSV large** (colonnes, recherche, plein écran paysage) et **graphiques résumé légers** ; `iappmanager://reports-guide`
- Avis clients — filtres, recherche, répondre / supprimer, **modèles de réponse** (max 20 par compte)
- **Webhooks** — créer / modifier / ping / livraison (nous n'hébergeons pas de callbacks publics)

### Widgets, raccourcis, finitions

- Widgets : **Account Hub**, **Apps Pulse** (S/M/L), **Review Desk**, **Quick Actions**
- `iappmanager://` + App Intents — [Shortcut Links](url-scheme)
- Apparence, accent, EN / 简 / 繁 (changement à chaud sans perdre la nav)
- **Icônes alternatives** iOS (IconStyle1–7) ; pourboire StoreKit ; e-mail feedback

### Confidentialité

- Secrets API dans le **Trousseau** de l'appareil ; API métier uniquement vers **Apple**
- Icônes optionnelles via iTunes Lookup ; vider le cache miniatures dans Réglages
- App Group pour snapshots **locaux** widgets uniquement — pas d'upload iHTC Studio
- Détails : [Privacy Policy](privacy)

## Obtenir l'app

| Canal | Lien |
|-------|------|
| App Store | [Download on the App Store](https://apps.apple.com/app/id6794497110) |

## Configuration requise

| Composant | Minimum |
|-----------|---------|
| iPhone / iPad | iOS 17.0+ |
| Mac | macOS 14.0+ |
| Widgets | iOS 17.0+ |
| Grosses IPAs | **Mac** recommandé |

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Réponse habituelle sous 48 heures.

[FAQ](faq) · [Shortcut Links](url-scheme) · [Privacy Policy](privacy)
