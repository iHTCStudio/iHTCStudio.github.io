**Dernière mise à jour :** 31 juillet 2026 

iHTC Studio ("nous", "notre" ou "notre") a construit **iThree** (également connu sous le nom de "爱三字经" / "愛三字經", ID de bundle `com.iHTCboy.iThree`). Cette politique de confidentialité explique quelles données sont (et ne sont pas) traitées lorsque vous utilisez l'application. **Apple App Review** et les utilisateurs peuvent s'appuyer sur **cette page** comme politique de confidentialité publique pour l'application. Pour App Store Connect, ouvrez cette politique de confidentialité dans votre navigateur et copiez l'adresse de la barre d'adresse (le domaine public du site peut changer au fil du temps). 

## Résumé (alignement sur l'étiquette nutritionnelle de confidentialité Apple)

| Sujet | Notre pratique | 
|-------|----------------| 
| Compte | **Non requis** — pas d'inscription, de connexion par e-mail ou de numéro de téléphone | 
| Collecte de données par iHTC Studio | **Données non collectées** — nous n'exploitons **pas** de backend qui reçoit vos données personnelles | 
| Réseau | La bibliothèque, la lecture, la récitation, l'étude, la chasse, les widgets et les notifications quotidiennes fonctionnent **hors ligne** après l'installation | 
| Analyses / publicités / suivi | **Aucun** — pas de SDK tiers d'analyse, de publicité ou de suivi ; pas d'utilisation de la transparence du suivi des applications | 
| Services Apple en option | **iCloud** (votre KVS privé), **Photothèque (ajout uniquement)** pour les cartes de partage, **StoreKit** pour les pourboires facultatifs, **notifications locales**, **Activités en direct** en option | 

## Collecte de données 

Nous ne collectons, vendons ou partageons **pas** d'informations personnelles à des fins publicitaires ou analytiques.

- **Aucun compte** — Vous pouvez utiliser toutes les fonctionnalités principales sans créer de compte chez nous. 
- **Aucune analyse ni publicité** — Le binaire de l'application n'intègre pas de SDK tiers d'analyse, de publicité ou de rapport d'erreur qui nous contactent. 
- **Aucun téléchargement de contenu** — Votre historique de lecture, vos favoris (y compris les histoires préférées), vos listes de lignes, vos progrès dans les études, vos séquences et vos préférences restent sur votre appareil (et éventuellement dans **votre** iCloud). Ils ne sont jamais téléchargés sur les serveurs iHTC Studio car **nous n'exécutons pas de tels serveurs pour cette application**. 

## Comment fonctionne l'application

- **Bibliothèque groupée** — Passage JSON, caractères pinyin, vernaculaire/anglais, histoires, index classiques et dynasties sont livrés dans l'ensemble d'applications/widgets. La navigation et l'étude ne nécessitent pas de requête réseau. 
- **Discours sur l'appareil** — La récitation utilise le système **AVSpeechSynthesizer** (TTS) d'Apple. Nous n'envoyons pas de texte de passage à iHTC Studio. 
- **Widgets et groupe d'applications** — Les widgets et l'application partagent les préférences et l'état léger via le groupe d'applications `group.com.iHTCboy.iThree` sur votre appareil. 
- **Notifications quotidiennes** — Planifiées localement avec les notifications utilisateur. Appuyer sur une notification ouvre un lien profond vers un identifiant de passage sur l'appareil ; pas de distribution du serveur. 
- **Partager des cartes** : les images sont rendues sur l'appareil. L'enregistrement utilise **le module complémentaire Photothèque** uniquement lorsque vous appuyez sur Enregistrer. System Share Sheet peut envoyer l'image à une application **que** vous choisissez ; la politique de confidentialité de cette destination s’applique alors. 
- **Conseil facultatif** — « Tip Developer » est un achat de consommable **StoreKit** traité par Apple. Nous ne recevons pas les détails de votre carte de paiement. 
- **Siri / Raccourcis / Centre de contrôle** — Les intégrations système facultatives ouvrent des liens profonds sur l'appareil ; ils ne nous envoient pas votre bibliothèque. 
- **Spotlight facultatif** — Si vous activez l'indexation, le contenu est indexé par le système sur l'appareil pour la recherche locale ; nous n'exploitons pas de backend de recherche.

## Données stockées sur votre appareil 

| Données | Où | Objectif | 
|------|-------|--------------| 
| Base de données de passages (y compris pinyin) | Offre groupée d'applications/widgets | Lecture et étude hors ligne | 
| Favoris et listes de lignes | Paramètres par défaut du groupe d'applications | Passages / histoires favoris et listes d'utilisateurs | 
| Historique de lecture / dernière lecture | Paramètres par défaut du groupe d'applications | Continuer la lecture, historique de l'interface utilisateur | 
| Avancement et maîtrise des études | Paramètres par défaut du groupe d'applications | Etat de la classe, quiz / Progression de la chasse | 
| Séquence d'entraînement / enregistrement | Paramètres par défaut du groupe d'applications | Habitude quotidienne | 
| Apparence et préférences de lecture | Paramètres par défaut du groupe d'applications | Thème, accent, langue, mise en page, TTS, onglets, widgets | 
| Préférences de cache et de notification de la ligne quotidienne | Paramètres par défaut du groupe d'applications | ID du jour, heure de programmation, bascule contextuelle | 
| Préférences de carte partagée | Paramètres par défaut du groupe d'applications | Derniers choix de style/ratio | 
| État d’intégration et de TipKit | Paramètres utilisateur standard (appareil) | Guide d'accueil / conseils découverte | 
| Actions rapides sur l'écran d'accueil | Système + préférences locales | Raccourcis que vous configurez | 
| Widget / Instantanés d'activité en direct | Groupe d'applications / ActivityKit | Afficher le texte que vous avez déjà ouvert |

La désinstallation de l'application supprime les données du bac à sable et du groupe d'applications associées à l'application (selon le comportement d'iOS/macOS). Les copies facultatives dans iCloud restent dans **votre** iCloud jusqu'à ce que vous les supprimiez ou que vous désactiviez la synchronisation et supprimiez ailleurs.

## Synchronisation iCloud (Facultative)

Si vous activez **la synchronisation iCloud** dans les Réglages, l'application reflète les données utilisateur sélectionnées via le **`NSUbiquitousKeyValueStore`** d'Apple lié à **votre identifiant Apple** :

- Favoris de passages
- Favoris d'histoires
- Listes de lignes
- Historique de lecture
- Progression / maîtrise des études
- Séries de pratique

Le trafic de synchronisation passe par **Apple iCloud**, et non par iHTC Studio. Vous pouvez désactiver la synchronisation dans les Réglages. Nous ne pouvons pas lire le contenu de votre iCloud.

## Autorisations

iThree demande des autorisations uniquement lorsqu'une fonctionnalité en a besoin :

| Autorisation | Quand | Pourquoi | 
|------------|------|-----| 
| Notifications | Vous activez les rappels Daily Line | Planification locale des notifications de rappel | 
| Bibliothèque de photos (Ajouter uniquement) | Vous enregistrez une carte de partage | Écrivez l'image rendue ; nous n'avons pas besoin d'un accès complet en lecture à la bibliothèque | 
| iCloud | Vous activez la synchronisation | Synchroniser les favoris/listes/historique/progression/séries | 
| Activités en direct (iOS) | Vous activez l'activité de lecture en direct | Affichez le passage que vous lisez sur l'écran de verrouillage / Dynamic Island | 
| Audio de fond (capacité) | Vous activez la récitation en arrière-plan | Continuer TTS lorsque l'application n'est pas au premier plan | 

Nous ne demandons **pas** de contacts, de localisation précise, de caméra, de microphone (au-delà de la lecture TTS du système) ou de suivi. 

## Ce que nous ne faisons pas 

- Nous ne vendons **pas** de données personnelles. 
- Nous ne créons **pas** de profils publicitaires. 
- Nous n'exigeons **pas** de compte ou de connexion sociale. 
- Nous n'intégrons **pas** de publicités tierces, d'analyses ou de SDK sociaux pour la collecte de données. 
- Nous n'accédons **pas** à votre photothèque au-delà du **ajout uniquement** lorsque vous choisissez d'enregistrer une carte. 
- Nous ne recevons **pas** de numéros de carte de paiement StoreKit (Apple traite les paiements). 

## Confidentialité des enfants

iThree ne collecte pas sciemment de données personnelles auprès de quiconque, y compris les enfants de moins de 13 ans (ou l'âge équivalent dans votre région). Comme nous n'exploitons pas de système de collecte de données, aucun profil enfant n'est stocké chez nous. Les familles peuvent utiliser les fonctionnalités de lecture et d'étude hors ligne sur leurs propres appareils.

## Tiers

- **Apple** — Distribution via l'App Store, achats facultatifs via StoreKit, KVS iCloud facultatif, synthèse vocale système, destinations du partage choisies par vous, et notifications / Live Activity / Siri / Raccourcis au niveau du système d'exploitation.
- **Aucun autre SDK tiers** pour la publicité, l'analyse ou la connexion sociale n'est inclus pour la collecte de données.

## Utilisateurs internationaux

L'application est conçue pour fonctionner hors ligne sur votre appareil. Les services Apple optionnels suivent les conditions et la disponibilité régionale d'Apple.

## Conservation et suppression des données

- **Sur l'appareil** — Les préférences locales et la progression restent jusqu'à ce que vous les effaciez dans l'application (lorsque disponible), que vous réinitialisiez l'appareil ou que vous désinstalliez l'application.
- **iCloud (facultatif)** — Les données que vous avez synchronisées restent dans **votre** compte iCloud selon les politiques d’Apple jusqu’à ce que vous désactiviez la synchronisation et/ou les effaciez via les outils d’Apple.
- **iHTC Studio** — Comme nous ne collectons pas de données personnelles sur nos serveurs, il n’existe aucun jeu de données de compte que nous puissions supprimer sur demande, hormis répondre à vos questions par email.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre. La date « Dernière mise à jour » en haut changera, et la politique révisée sera publiée sur cette page de politique de confidentialité.

## Contactez-nous

Si vous avez des questions concernant cette politique de confidentialité ou nos pratiques en matière de confidentialité :

- **Email :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)

Nous répondons généralement sous 48 heures.
