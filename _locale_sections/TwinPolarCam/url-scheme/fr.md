TwinPolarCam prend en charge les liens de raccourci ** `twinpolarcam://` **. Utilisez-les dans **Safari signets**, l'application **Shortcuts**, ou à partir de **Home Screen actions rapides** et **Spotlight** pour sauter directement dans les guides et les écrans clés.

## Format de lien


```
twinpolarcam://{host}
```


Il n'y a pas de chemin ou de composant de requête — le routage est par **nom de l'hôte seulement** (insensible au cas par cas).

---

## Guides

| URL | Ouvre |
|-----|-------|
| `twinpolarcam://usage-guide` | **Comment utiliser le guide** |
| `twinpolarcam://recording-guide` | **Enregistrement et fiabilité** |
| `twinpolarcam://export-guide` | **Exportation et en attente** |
| `twinpolarcam://feature-guide` | **Visite à l'honneur** (6 pages de replay à bord) |

Mêmes destinations que **App Paramètres → Aide**.

---

## Écrans App

| URL | Ouvre |
|-----|-------|
| `twinpolarcam://settings` | Panneau de paramètres de l' application |
| `twinpolarcam://pending` | Directeur des exportations en attente |
| `twinpolarcam://feedback` | Envoyer des commentaires (compositeur de courriel) |
| `twinpolarcam://recording` | Application principale (activité en direct / retour sur l'île dynamique) |

---

## Actions rapides de l'écran d'accueil

**Appuyez sur l'icône TwinPolarCam** — quatre raccourcis fixes (les mêmes hôtes que ci-dessus):

| Quick action | URL |
|--------------|-----|
| Usage Guide | 'twinpolarcam://guide-usage' |
| Recording Tips | 'twinpolarcam://recording-guide' |
| Export Guide | 'twinpolarcam://export-guide' |
| Feature Tour | 'twinpolarcam://feature-guide' |

Les actions rapides fonctionnent sur **cold launch** et lorsque l'application est déjà en cours d'exécution. Si à bord n'a pas encore terminé, le lien est **queued** et livré après avoir terminé le guide de bienvenue.

---

## Pleins feux

Guide des index TwinPolarCam dans **Spotlight**. Rechercher :

- TwinPolarCam
- Guide d'utilisation / Enregistrement et fiabilité / Exportation et en attente / Visite en vedette

Le tapotage d'un résultat ouvre la feuille de guidage correspondante.

---

## Notes

- **Unsupported devices** can still open guide links from the unsupported screen — utile pour les exigences de lecture avant remboursement.
- Les hôtes inconnus sont **ignorés en toute sécurité** (pas de crash).
- Les guides exigent que l'interface utilisateur principale soit prête; les URL de démarrage à froid sont tamponnées jusqu'à la fin de l'initialisation.

[Guide de l'utilisateur](index) · [FAQ](../faq) · [Politique de confidentialité](../privacy)


