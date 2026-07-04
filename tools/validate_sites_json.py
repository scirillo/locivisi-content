#!/usr/bin/env python3
"""Validate sites_base_v1.json structure and media completeness."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "sites_base_v1.json"
CONTENT_DIR = ROOT / "cities/rome"
ITINERARIES = CONTENT_DIR / "itineraries.json"


def main() -> int:
    sites = json.loads(CATALOG.read_text(encoding="utf-8"))
    errors: list[str] = []

    if len(sites) != 50:
        errors.append(f"Expected 50 sites, found {len(sites)}")

    ids = [s.get("id") for s in sites]
    if len(set(ids)) != len(ids):
        errors.append("Duplicate site ids detected")

    for site in sites:
        sid = site.get("id", "<unknown>")
        if not site.get("shortDescription"):
            errors.append(f"{sid}: missing shortDescription")
        if not site.get("images"):
            errors.append(f"{sid}: missing images")
        elif not site["images"][0]:
            errors.append(f"{sid}: empty hero image")
        for h in site.get("highlights", []):
            if not h.get("title"):
                errors.append(f"{sid}: highlight missing title")
            if not h.get("imageUrl"):
                errors.append(f"{sid}: highlight '{h.get('title')}' missing imageUrl")
            if not h.get("url"):
                errors.append(f"{sid}: highlight '{h.get('title')}' missing url")
        highlight_urls = [h.get("imageUrl") for h in site.get("highlights", []) if h.get("imageUrl")]
        if len(highlight_urls) != len(set(highlight_urls)):
            errors.append(f"{sid}: duplicate highlight imageUrl")
        vi = site.get("visitingInfo") or {}
        if not (vi.get("hoursNote") or vi.get("officialUrl") or vi.get("ticketUrl")):
            errors.append(f"{sid}: visitingInfo has no hoursNote/officialUrl/ticketUrl")

    if errors:
        print("Validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    featured = sum(1 for s in sites if s.get("featuredOnMap"))
    commons_heroes = sum(
        1
        for s in sites
        if s["images"][0].startswith("https://upload.wikimedia.org/")
    )
    upload_urls = sum(
        1
        for s in sites
        for h in s.get("highlights", [])
        if (h.get("imageUrl") or "").startswith("https://upload.wikimedia.org/")
    )
    print(
        f"OK: {len(sites)} sites, {featured} featured, "
        f"{commons_heroes} upload hero URLs, {upload_urls} upload highlight URLs"
    )

    overlay_errors = validate_content_overlays(ids)
    if overlay_errors:
        print("Content overlay validation FAILED:")
        for err in overlay_errors:
            print(f"  - {err}")
        return 1

    itinerary_errors = validate_itineraries(ids)
    if itinerary_errors:
        print("Itinerary validation FAILED:")
        for err in itinerary_errors:
            print(f"  - {err}")
        return 1

    return 0


def validate_itineraries(base_ids: list[str]) -> list[str]:
    errors: list[str] = []
    if not ITINERARIES.exists():
        errors.append(f"Missing {ITINERARIES.name}")
        return errors
    templates = json.loads(ITINERARIES.read_text(encoding="utf-8"))
    if not isinstance(templates, list) or not templates:
        errors.append("itineraries.json must be a non-empty array")
        return errors
    seen_ids: set[str] = set()
    for template in templates:
        tid = template.get("id", "<unknown>")
        if tid in seen_ids:
            errors.append(f"Duplicate itinerary id: {tid}")
        seen_ids.add(tid)
        for key in ("titleKey", "subtitleKey", "daySiteIds"):
            if key not in template:
                errors.append(f"{tid}: missing {key}")
        for day_index, day in enumerate(template.get("daySiteIds", []), start=1):
            if not day:
                errors.append(f"{tid}: day {day_index} is empty")
            for site_id in day:
                if site_id not in base_ids:
                    errors.append(f"{tid}: unknown site id {site_id}")
    return errors


def validate_content_overlays(base_ids: list[str]) -> list[str]:
    errors: list[str] = []
    for path in sorted(CONTENT_DIR.glob("site_content_*.json")):
        overlay = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(overlay, dict):
            errors.append(f"{path.name}: root must be an object")
            continue
        unknown = sorted(set(overlay.keys()) - set(base_ids))
        if unknown:
            errors.append(f"{path.name}: unknown site ids: {', '.join(unknown[:5])}")
        for site_id, entry in overlay.items():
            if site_id not in base_ids:
                continue
            if not isinstance(entry, dict):
                errors.append(f"{path.name}:{site_id}: entry must be an object")
                continue
            if not any(
                entry.get(key)
                for key in ("name", "shortDescription", "neighborhood", "highlights", "visitingInfo", "audio")
            ):
                errors.append(f"{path.name}:{site_id}: empty overlay entry")
    return errors


if __name__ == "__main__":
    sys.exit(main())
