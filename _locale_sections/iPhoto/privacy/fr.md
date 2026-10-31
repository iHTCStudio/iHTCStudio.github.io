iHTC Studio (« nous » ; anciennement iHTCTeam) développe **iVeil** (爱修图 / 愛修圖 ; les versions antérieures s’appelaient iPhoto). Cette politique explique ce qu’il advient de vos données lorsque vous utilisez l’app, son extension de partage, l’extension de retouche Photos, les widgets, les commandes du Centre de contrôle et l’appareil photo de l’écran verrouillé.

*Dernière mise à jour : 18 octobre 2026*

## En bref

- **Pas de compte, pas de publicité, pas d’analyse, pas de suivi.** iVeil ne contient aucun SDK tiers d’analyse, de publicité ou de suivi.
- **Vos photos et vidéos ne quittent jamais votre appareil par iVeil.** La détection, la retouche et l’exportation s’exécutent sur l’appareil. Nous n’exploitons aucun serveur qui reçoit vos contenus.
- **Vous décidez de ce qui est partagé.** iVeil crée de nouvelles copies. Vos originaux dans Photos ne changent que si vous enregistrez une retouche avec l’extension de retouche Photos, et cette retouche peut être annulée dans Photos.

## Ce qu’iVeil traite sur votre appareil

| Données | Pourquoi | Ce qui est conservé |
|------|-----|--------------|
| Photos et vidéos que vous choisissez (Photos, le menu Partager, Fichiers ou l’appareil) | Pour les vérifier, les masquer et les retoucher | Stockées dans le bac à sable de l’app jusqu’à ce que vous les supprimiez. Les photos transmises par l’extension de partage passent brièvement par le conteneur App Group, puis sont déplacées dans l’app. |
| Visages et personnes (Apple Vision) | Trouver et masquer des visages, garder les personnes choisies, incliner un voile emoji avec la tête, détourer une personne gardée, et retouche de portrait facultative | Les rectangles ou contours nécessaires pour redessiner vos masques sont enregistrés avec le projet. Les points du visage restent uniquement en mémoire. |
| Texte dans les images (reconnaissance de texte Vision et détecteurs de données Apple) | Trouver numéros de téléphone, e-mails, adresses, numéros de carte et de pièce d’identité, lignes de passeport, numéros de commande, identifiants de compte et liens | Seuls la zone et le type sont enregistrés. Le texte reconnu lui-même n’est pas enregistré. |
| Codes QR et codes-barres | Les masquer et, avec « Ce que cache le code », indiquer quel type d’information ils contiennent | Seuls la catégorie et les noms de champs (par exemple « carte d’embarquement : siège ») sont enregistrés, jamais le contenu. |
| Détails du fichier (lieu, date de prise de vue, appareil, objectif, numéros de série) | Montrer ce qu’un fichier révèle et le retirer des copies que vous partagez | Lus dans votre fichier. Les copies ne gardent que ce que vous choisissez ; les numéros de série et les noms de propriétaire sont toujours retirés. |
| Images potentiellement sensibles (analyse de contenu sensible d’Apple) | Flouter la nudité ou un contenu choquant avant le partage, seulement si vous avez activé l’avertissement de contenu sensible ou la sécurité des communications dans Réglages | L’analyse s’exécute sur l’appareil, dans le cadre d’Apple. Les résultats ne sont ni stockés ni envoyés. |
| Apple Intelligence (facultatif, iOS 26) | « Regarder à nouveau avec Apple Intelligence » et « Décrire un look » | S’exécute sur le modèle d’Apple sur l’appareil. Il ne reçoit que les lignes de texte reconnues et leur nombre, ou la phrase que vous saisissez, jamais d’images ni de données de visage. |
| Marque invisible (facultatif) | Vérifier plus tard à qui vous avez envoyé une photo | Un code de 32 bits est caché dans la luminosité de l’image. Les noms de destinataires que vous saisissez restent dans une liste sur votre appareil (jusqu’à 500 entrées), que vous pouvez modifier ou effacer dans Réglages → Marque invisible. |
| Détourages et voiles Genmoji | Réutiliser les personnes détourées et les emoji personnalisés | Enregistrés comme images dans le conteneur App Group de votre appareil jusqu’à ce que vous les retiriez. |
| Récemment supprimés | Annuler une suppression | Les projets supprimés sont conservés 30 jours, puis retirés définitivement. |
| Préférences | Langue, apparence, options de capture et d’exportation | Stockées dans le conteneur App Group de votre appareil. |

## Données de visage

iVeil utilise le cadre Vision d’Apple sur votre appareil pour **localiser** les visages et les personnes. Ce n’est **pas** de la reconnaissance faciale : iVeil n’identifie personne, ne compare pas les visages et ne crée pas de modèles biométriques.

- **Usage :** masquer des visages, garder les personnes que vous choisissez, aligner les voiles emoji, détourer une personne gardée et retouche de portrait facultative.
- **Stockage :** les rectangles de visage normalisés, les contours de personne et vos réglages de retouche sont enregistrés dans le projet, dans le bac à sable de l’app. Les points complets du visage ne sont jamais écrits sur le disque.
- **Partage :** les données de visage ne sont jamais téléversées, jamais transmises à nous ni à un tiers, et ne sont pas synchronisées avec iCloud.
- **Conservation :** les données de visage ne durent que le temps du projet. Supprimer un projet (après 30 jours dans Récemment supprimés) ou désinstaller l’app les retire.

## Utilisation du réseau

iVeil n’a pas de serveurs propres. Les seules requêtes réseau viennent des services Apple :

- **Plans.** Lorsqu’une photo a un lieu, iVeil l’affiche sur un plan Apple Plans, qui charge auprès d’Apple les tuiles de cette zone. Si vous choisissez **Pâté de maisons**, le nom du lieu est demandé à Apple à partir du centre d’une cellule d’environ 5 km, et non des coordonnées exactes. Aucun contenu d’image n’est envoyé. Apple traite ces requêtes selon la [politique de confidentialité d’Apple](https://www.apple.com/fr/legal/privacy/).
- **Pourboire facultatif.** « Pourboire au développeur » est un achat intégré consommable traité par Apple via StoreKit. Il ne débloque rien, et nous ne recevons aucune information personnelle.
- **Synchronisation iCloud facultative (désactivée par défaut).** Lorsque vous l’activez, quelques préférences (langue, apparence, options de capture ou d’exportation) se synchronisent via votre propre stockage clé-valeur iCloud. Les photos, les vidéos, les données de visage et la liste de la marque invisible ne sont jamais synchronisées.

## Autorisations

| Autorisation | Objet |
|------------|---------|
| Photos | Ouvrir les photos choisies et afficher leur lieu et les détails de l’appareil |
| Photos (ajout uniquement) | Enregistrer les copies exportées |
| Appareil photo | Onglet Capture, Voile en direct et l’appareil à voile sur l’écran verrouillé |

iVeil ne demande pas l’autorisation du microphone, du lieu, des contacts ni du suivi. Le voile vidéo utilise le son déjà présent dans la vidéo choisie et peut le retirer.

## Travail en arrière-plan et Live Activities

Les partages sûrs groupés et les exportations de voile vidéo que **vous lancez** peuvent se poursuivre brièvement en arrière-plan. Une Live Activity peut afficher le titre de la tâche et sa progression sur l’écran verrouillé. Elle ne montre jamais le contenu de l’image.

## Enfants

iVeil ne collecte sciemment aucune donnée personnelle de quiconque, y compris des enfants, parce que le contenu est traité sur l’appareil et que nous n’avons pas de serveur de collecte.

## Avertissement

iVeil est une app indépendante et **n’est pas affiliée à Apple Inc.** La détection automatique est une première passe, pas une garantie. Veuillez relire une photo avant de la partager.

## Modifications

Si nos pratiques changent, nous mettrons cette page à jour et réviserons la date ci-dessus.

## Contact

- **E-mail :** [AppleOSer@gmail.com](mailto:AppleOSer@gmail.com)
