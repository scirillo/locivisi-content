# locivisi-content

Shared catalogue, UI strings, legal text, and planner itineraries for [Locivisi](https://github.com/scirillo/locivisi) (Android) and [locivisi-ios](https://github.com/scirillo/locivisi-ios).

**Edit JSON only in this repo.** App repos should not track these files.

## Expected checkout layout

```
StudioProjects/
├── locivisi/           # Android app
├── locivisi-ios/       # iOS app
└── locivisi-content/   # this repo
```

## Layout

| Path | Purpose |
|------|---------|
| `manifest.json` | Content version and file index |
| `sites_base_v1.json` | Site catalogue |
| `cities/rome/collections.json` | Curated sets |
| `cities/rome/insights.json` | Map tips |
| `cities/rome/itineraries.json` | Planner trip starters |
| `cities/rome/site_content_*.json` | Language overlays |
| `i18n/ui_strings_*.json` | UI translations |
| `legal/privacy_policy_en.txt` | Privacy policy |
| `tools/` | Validation and catalogue generation scripts |

## App integration

Android and iOS fetch catalogue JSON on launch from:

`https://raw.githubusercontent.com/scirillo/locivisi-content/main/`

Files are cached on device. **Bump `contentVersion` in `manifest.json` and push to `main`** to ship catalogue updates without an app store release.

Optional: enable GitHub Pages (`.github/workflows/pages.yml`) for CDN-style hosting at `https://scirillo.github.io/locivisi-content/`.

## Validate

```bash
python3 tools/validate_sites_json.py
```

## CI and branch protection

Every pull request to `main` runs **Validate content** (`.github/workflows/validate.yml`). The Pages deploy workflow also validates before publishing.

After pushing the workflow files, enable branch protection on GitHub:

1. **Settings → Branches → Add rule** for `main`
2. Enable **Require a pull request before merging**
3. Enable **Require status checks to pass before merging**
4. Select the **validate** check (from *Validate content*)
5. Save

Use feature branches and open PRs for JSON edits so broken content cannot merge to `main`.

## Regenerate catalogue (optional)

```bash
python3 tools/generate_sites_base_v1.py
python3 tools/build_site_content_overlay.py it
python3 tools/validate_sites_json.py
```

Bump `contentVersion` in `manifest.json` when you publish catalogue changes.
