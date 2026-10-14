iStore supporte les liens de raccourci ** `istore://` **. Utilisez-les dans **Shortcuts**, signets Safari, ou à partir de **widgets**, **Control Center**, **Spotlight** et l'extension **Share** vers **switch une région**, **switchez votre dernière région**, **ouvrez un onglet** ou **jump vers un guide**.

## Format de lien


```
istore://{host}?{params}
```


Les hôtes sont **insensibles aux cas**. Les codes régionaux utilisent la norme **Valeurs alpha-2** ( `istore://` , `us` , `cn` , `jp` , `hk` , ...).

| What you want | Lien |
|---------------|------|
| Switch to a region | `istore://switch?region={code}` |
| Switch to your last region | `istore://switch-last' |
| Open the Store / Favorites / Settings tab | "IStore://store" · "IStore://favorites" · "IStore://settings" |
| Open App Availability | 'estore://disponibilité' |

---

## Passer à une région

Demande un changement vers la région donnée (racheminée par la confirmation de l'application, si activé).


```
istore://switch?region={code}
```


| Parameter | Required | Désignation des marchandises |
|-----------|----------|-------------|
| `region` | **Yes** | Code régional, par exemple `us`, `cn`, `jp`, `hk`, `tw` |

**Exemple**


```
istore://switch?region=us
```


Utilisé par : ** widgets interactifs**, **Spotlight** et **Shortcuts / Siri**.

---

## Passez à votre dernière région


```
istore://switch-last
```


Lis ta cible de commutation la plus récente et change à nouveau. Fonctionne sur la commande **Switch Last** Control Center (iOS 18+) et l'action Shortcut / Siri correspondante.

---

## Tabs & pages (aucune requête)

| URL | Ouvre |
|-----|-------|
| `istore://store` | Onglet Enregistrer |
| `istore://favorites` | Onglet Favoris |
| `istore://settings` | Onglet Paramètres |
| `istore://availability` | Paramètres → Disponibilité de l'application (également utilisée par l'extension de partage) |
| `istore://switch-history` | Historique du commutateur |
| `istore://quick-regions` | Paramètres des régions rapides |
| `istore://feature-guide` | Guide des fonctionnalités |
| `istore://widget-guide` | Guide des widgets |
| `istore://shortcuts-guide` | Guide Raccourcis |
| `istore://usage-guide` | Guide d'utilisation |
| `istore://feedback` | E-mail de commentaires |
| `istore://in-app-review` | Note App Store in-app |

---

## Widgets, Control Center & Spotlight

Ces liens génèrent automatiquement `istore://` lorsque vous appuyez sur :

| Source | Tap target | Effet |
|--------|------------|--------|
| **Quick Regions / Recent / Custom widget** | A region tile | `estore://switch?region=...` |
| **Switch Last control** (iOS 18+) | The control | `istore://switch-last' |
| **Spotlight** | A region result | `estore://switch?region=...` |

La commutation interactive depuis les widgets et Control Center ouvre l'application pour compléter la redirection officielle de l'App Store.

---

## Extension du partage

Partager un lien **App Store** dans iStore. L'extension de partage vérifie la disponibilité dans les régions populaires, puis peut ouvrir l'application via `istore://` afin que vous puissiez examiner le résultat et changer.

---

## Siri & raccourcis

Trouvez des actions intégrées dans l'application **Shortcuts** ou demandez **Siri**. Les titres et les phrases sont localisés en anglais / 简体中文 / 简ш中文.

| Action | What you can set | Effet |
|--------|------------------|--------|
| Switch region | Region | Passons à cette région |
| Switch last region | — | Commutation vers votre dernière cible |
| Switch favorite region | A favorite | Passage à une région préférée |
| Open store | — | Ouvre iStore |
| Check availability | App link or ID | Vérifier où l'application est disponible |

---

## Codes régionaux en liens

Les liens profonds et les URL générées par widget utilisent toujours des codes stables **region** ( `istore://` , `us` , `cn` , `jp` , ...) — les noms d'affichage non localisés.

**Exemples**


```
istore://switch?region=jp
istore://switch?region=hk
```


[Retour à l'aperçu](..) · [FAQ](../faq) · [Confidentialité](../privacité)


