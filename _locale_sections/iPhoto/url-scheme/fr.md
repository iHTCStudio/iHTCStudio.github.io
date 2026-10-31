iPhoto prend en charge ** `iphoto://` ** liens profonds et **Apptents / Raccourcis Siri**. Les liens naviguent uniquement à l'intérieur de l'application — ils ne téléchargent pas les données.

## Régime


```
iphoto://<host>[?query]
```


| Rule | Détail |
|------|--------|
| Scheme | "iphoto" |
| Empty | Ouvre l'onglet par défaut de l'application |
| Unknown hosts | Ignoré en toute sécurité |

---

## Tabs & navigation

| URL | Ouvre |
|-----|-------|
| `iphoto://library` | Onglet Bibliothèque |
| `iphoto://capture` | onglet de capture |
| `iphoto://settings` | Onglet Paramètres |
| `iphoto://search` | Onglet Recherche (iOS 18+) |
| `iphoto://recent-projects` | Bibliothèque axée sur les travaux récents |

---

## Éditeur

| URL | Ouvre |
|-----|-------|
| `iphoto://editor?id=<projectID>` | Éditeur pour l'id du projet donné |

---

## Guides et actions

| URL | Ouvre |
|-----|-------|
| `iphoto://usage-guide` | Guide d'utilisation |
| `iphoto://widget-guide` | Guide des widgets |
| `iphoto://shortcuts-guide` | Guide Raccourcis |
| `iphoto://feature-guide` | Fonctionnalité / rejouage à bord |
| `iphoto://export-presets` | Paramètres liés aux exportations |
| `iphoto://feedback` | E-mail de commentaires |
| `iphoto://in-app-review` | Révision rapide de l'application |

---

## Siri & raccourcis

Les objectifs intégrés comprennent :

- Ouvrir la capture
- Ouvrir la bibliothèque
- Importer des photos
- Ouvrir les paramètres

Ajoutez-les dans l'application Raccourcis ou invoquez avec Siri en utilisant les phrases indiquées dans Raccourcis.

## Exemples


```
iphoto://capture
iphoto://library
iphoto://editor?id=YOUR-PROJECT-ID
iphoto://widget-guide
```


[FAQ](../faq) · [Politique de confidentialité](../privacité) · [Retour à iPhoto](../)


