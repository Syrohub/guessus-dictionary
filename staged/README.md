# Staged dictionary updates

A folder here holds a complete, already tested dictionary version that is not live yet.
The workflow `.github/workflows/publish-staged.yml` copies it over `v2/` and `v3/` on its
scheduled date (or when run by hand from the Actions tab): data files first, version files a
few minutes later, so that no client sees the new version number before the new data.

Nothing is staged at the moment. The 2.6.0 New Year's add-on was withdrawn on 16 November 2026: the owner found its cards out of style with the game, so the scheduled run on 10 December will find nothing and do nothing.

The workflow only moves the live version up and does nothing when the staged version is not
higher than the live one. To cancel a scheduled update, delete its folder. If another version is
published before the date, rebuild the staged folder from the app repository first (the staged
files would otherwise overwrite the newer content).
