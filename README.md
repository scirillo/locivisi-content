# locivisi-content

Shared catalogue, UI strings, legal text, and planner itineraries for [Locivisi](https://github.com/scirillo/locivisi) (Android) and [locivisi-ios](https://github.com/scirillo/locivisi-ios).

**Edit JSON only in this repo.**

## Layout

| Path | Purpose |
|------|---------|
| `manifest.json` | Content version and file index (for future OTA updates) |
| `sites_base_v1.json` | Site catalogue |
| `cities/rome/collections.json` | Curated sets |
| `cities/rome/insights.json` | Map tips |
| `cities/rome/itineraries.json` | Planner trip starters |
| `cities/rome/site_content_*.json` | Language overlays |
| `i18n/ui_strings_*.json` | UI translations |
| `legal/privacy_policy_en.txt` | Privacy policy |

## App integration

- **Android:** Git submodule at `content/` in the Android repo; Gradle bundles it as assets.
- **iOS:** Run `./tools/sync_content_to_ios.sh` from the Android repo (or rsync this repo into `Locivisi/Resources/`).

After cloning app repos:

```bash
# Android
cd locivisi
git submodule update --init --recursive

# iOS — sync JSON into the app bundle
./tools/sync_content_to_ios.sh
```

## Validate

```bash
python3 tools/validate_sites_json.py
```

Bump `contentVersion` in `manifest.json` when you publish catalogue changes (for future remote sync).
