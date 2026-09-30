# Guess Us dictionaries (v2)

Read by app builds with packs (Classic / Premium / Uncensored). Older builds keep reading the files in the repo root.

- `family.json`, `adult.json` — subcategories: `id` (a-z0-9_-), `pack` (`classic` | `premium` | `uncensored`, the last one only in adult), `order`, `names` (en/ru/es/ua), `words` (en/ru/es/ua, 10+ each). `"hidden": true` removes a built-in subcategory.
- `family-version.json`, `adult-version.json` — `{"version": "x.y.z"}`. Apps download only when this is higher than what they already have (bundled version: 2.0.0).

To publish: edit `<variant>.json`, bump `"version"` in it and in `<variant>-version.json` to the same higher value, commit and push. Players get it on the next app launch with internet.
