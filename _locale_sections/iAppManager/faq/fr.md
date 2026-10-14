### Qu'est-ce qu'iAppManager ?

Un **poste de travail App Store Connect natif** pour iPhone, iPad et Mac. Connexion par **clé API**, gestion des versions, captures, IAP, TestFlight, certificats, rapports et avis — trafic **directement vers Apple**. Aucun compte iHTC Studio.

### Comment obtenir une clé API ?

1. Ouvrez [App Store Connect](https://appstoreconnect.apple.com) → **Users and Access** → **Integrations** → **App Store Connect API**
2. Créez une clé (Admin ou App Manager recommandé)
3. Téléchargez le `.p8` **une seule fois**, notez **Issuer ID** et **Key ID**
4. Collez dans iAppManager (ou choisissez le fichier). Le guide in-app avec captures vous accompagne.

### Ma `.p8` est-elle envoyée à iHTC Studio ?

**Non.** La clé privée reste dans le **Keychain de l'appareil**. Les requêtes sont signées localement et envoyées à `api.appstoreconnect.apple.com`. Supprimer le compte efface la clé locale.

### Faut-il le mot de passe Apple ID dans l'app ?

**Non.** Authentification **uniquement par clé API** (Issuer ID + Key ID + `.p8`). Si une fonction n'a pas d'API publique (ex. privacy nutrition labels, codes promo d'apps gratuites), l'app ouvre le site Apple — vous utilisez Apple ID dans Safari/ASC.

### Téléverser IPA / PKG sans Transporter ?

**Oui.** iAppManager utilise **Build Upload REST** d'Apple (WWDC25). Préférez le **Mac** pour les gros fichiers ; iOS supporte la même API mais les gros envois y sont moins confortables.

### Que signifie « on sale » dans les filtres / widgets ?

**Disponible dans au moins un territoire App Store.** Les buckets pipeline (waiting / in review / rejected / pending developer release) sont suivis à part. Widget **Needs attention** = waiting + in review + rejected + pending release (somme locale, pas un champ ASC).

### Checks hard vs soft avant envoi ?

Les **hard blockers** bloquent l'envoi (ex. build pas prêt, compte démo requis mais absent). Les **soft checks** avertissent (taille capture principale, copyright, classification d'âge, etc.) — vous pouvez confirmer et continuer. Voir Overview / Versions / Submissions `?` ou `iappmanager://release-guide`.

### Langues prises en charge ?

**English · 简体中文 · 繁體中文** — suivre le système ou forcer dans Réglages. Changement à chaud **sans** remonter la racine (navigation et brouillons conservés).

### Pourquoi les widgets n'affichent pas les chiffres ASC en direct ?

Les widgets **n'appellent pas ASC**. L'app principale scanne et écrit un instantané (~10 min TTL, mêmes buckets que My Apps). Ouvrez l'app et actualisez la liste (ou forcez le statut).

### macOS vs iOS ?

Les deux couvrent store, monétisation, TestFlight, Game Center, utilisateurs, rapports, avis, Webhooks. **Gros IPA** et installation des certificats dans le Keychain système — préférez le **Mac**. Icônes alternatives **iOS uniquement**.

### URL de politique de confidentialité pour App Store Connect ?

Ouvrez la [Privacy Policy](../privacy) de ce site et copiez l'URL depuis la barre d'adresse du navigateur.

### Configuration requise ?

iPhone / iPad **iOS 17.0+**, Mac **macOS 14.0+**.

### Contacter le support ?

[AppleOSer@gmail.com](mailto:AppleOSer@gmail.com) — en général sous 48 h.
