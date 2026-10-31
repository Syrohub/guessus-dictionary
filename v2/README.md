# Guess Us dictionaries (v2)

Read by app builds with packs (Classic / Premium / Uncensored). Older builds keep reading the files in the repo root.

- `family.json`, `adult.json` — subcategories: `id` (a-z0-9_-), `pack` (`classic` | `premium` | `uncensored`, the last one only in adult), `order`, `names` (en/ru/es/ua), `words` (en/ru/es/ua, 10+ each). `"hidden": true` removes a built-in subcategory.
- `family-version.json`, `adult-version.json` — `{"version": "x.y.z"}`. Apps download only when this is higher than what they already have (bundled version: 2.0.0).

To publish: edit `<variant>.json`, bump `"version"` in it and in `<variant>-version.json` to the same higher value, commit and push. Players get it on the next app launch with internet.

## Compatibility for 2.4.0 content updates

This channel stays usable by the existing v2 app without an app release. Family has 17 topics. Adult has the same 17, Party and the existing `dirty` topic (19 total). The six reviewed Uncensored lists are combined under that original ID, preserving a saved `dirty` opt-out; do not publish the split IDs to this feed.

Both variants include the independently curated EN/RU/ES/UA content and all nine added Premium topics since 2.0.0 (Singers & actors plus eight culture topics). Keep root-level legacy files unchanged. Publish dictionary payloads first, verify their public URLs, then update version manifests.

