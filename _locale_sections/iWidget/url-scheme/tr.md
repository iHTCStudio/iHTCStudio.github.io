iWidget, **iPhone, iPad ve Mac** üzerinde **`iwidget://`** kullanır. Safari, Kısayollar, başka bir uygulama veya QR. Uygulamayı açmadan ay/tatil sorusu için Siri. İş günü için ayrı Workday intent; URL değildir.

`iwidget://<host>[?query]` — bilinmeyen host yok sayılır.

| Host | Açar | Query |
|------|------|-------|
| `today` | Bugün | — |
| `day` | Bugün → gün ayrıntısı | `y` `m` `d` |
| `library` | Kitaplık | `preset=` / `set=`, `detail=1` |
| `mine` | Widget’larım | `design=` / `id=`, `preset=` / `set=` |
| `editor` | Düzenleyici | `design=` / `id=` (yoksa en son) |
| `import` | İçe aktarma | — |
| `settings` | Ayarlar | `scroll=festivals` · `weather` · `editor` · `access` |
| `membership` | Üyelik | duraklatılmış widget’lar bunu açar |
| `launch` | Kısayol handoff (iOS) | widget sağlar |

Örnekler: `iwidget://today` · `iwidget://library?set=small.calendar&detail=1` · `iwidget://membership`

[Desteğe dön](../) · [FAQ](../faq) · [Üyelik](../membership) · [Gizlilik](../privacy)
