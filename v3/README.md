# GuessUs dictionaries (v3)

For app clients whose updater reads `main/v3` and migrates the saved `dirty` opt-out into six Uncensored IDs. The current content release is 2.4.0, with independent EN/RU/ES/UA selections.

- Family: 17 visible categories, 5,325 localized card rows.
- Adult: 24 visible categories, 8,412 localized card rows. The hidden empty `dirty` marker is required for merging older dictionaries.
- Classic/Premium purchases retain their existing products; all added culture topics are Premium.
- `<variant>.json` and `<variant>-version.json` have matching versions. A client downloads only when the manifest is newer than its current dictionary.

Publish dictionary payloads first, verify their public URLs, then announce them in the manifests. Existing v2 clients use the compatible aggregate in `v2`; they cannot read this channel merely because new files were published. Root-level legacy files remain unchanged.

Automated structure, localization-ledger and gameplay checks and independent agent editorial review passed. Native-speaker playtesting is a separate step and has not been claimed.

