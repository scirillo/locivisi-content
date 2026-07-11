#!/usr/bin/env python3
"""One-shot content polish: unique highlight images, ticket/tour URLs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "sites_base_v1.json"


def thumb(file_name: str, width: int = 960) -> str:
    canonical = file_name.replace(" ", "_")
    digest = hashlib.md5(canonical.encode("utf-8")).hexdigest()
    encoded = quote(canonical, safe="(),'")
    return (
        f"https://upload.wikimedia.org/wikipedia/commons/thumb/"
        f"{digest[0]}/{digest[0:2]}/{encoded}/{width}px-{encoded}"
    )


# Second highlight imageUrl fixes (index 1) — unique Wikimedia filenames.
HIGHLIGHT_IMAGE_FIXES: dict[str, str] = {
    "q623612_ara_pacis_museum": thumb("Museo_dell'Ara_Pacis_-_esterno.jpg"),
    "q318660_santa_maria_aracoeli": thumb("Santa_Maria_in_Aracoeli_Interno.jpg"),
    "q186282_santa_maria_maggiore": thumb("Roma_Santa_Maria_Maggiore_BW_1.jpg"),
    "q3867590_casina_delle_civette": thumb("Casina_delle_Civette_-_vetrata.jpg"),
    "q1053970_centrale_montemartini": thumb("Centrale_Montemartini_-_Museo_(3).jpg"),
    "q1465674_santignazio_church": thumb("Sant'Ignazio_di_Loyola_(Roma)_-_Volta_affrescata_da_Andrea_Pozzo.jpg"),
    "q207808_circus_maximus": thumb("Circus_Maximus_from_Palatine.jpg"),
    "q2301489_doria_pamphilj_gallery": thumb("Velázquez,_Diego_-_Portrait_of_Pope_Innocent_X_-_Google_Art_Project.jpg"),
    "q3757713_galleria_spada": thumb("Galleria_Spada_perspective_colonnade.jpg"),
    "q724816_jewish_museum_rome": thumb("Portico_d'Ottavia_-_Rome.jpg"),
    "q1283630_keats_shelley_house": thumb("Keats-Shelley_House_Interior.jpg"),
    "q1356135_macro_rome": thumb("Macro_Testaccio_Rome.jpg"),
    "q3868408_maxxi": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/MAXXI_Roma_2010.jpg/960px-MAXXI_Roma_2010.jpg",
    "q478642_mercati_traiano": thumb("Mercati_di_Traiano_-_interno.jpg"),
    "q3867587_museo_carlo_bilotti": thumb("Roma-museoBilotti02.jpg"),
    "q3868175_museo_roma_palazzo_braschi": thumb("Piazza_Navona_from_Palazzo_Braschi.jpg"),
    "q3868176_museo_napoleonico": thumb("Museo_Napoleonico_-_interno.jpg"),
    "q1074320_museum_roman_civilization": thumb("Plastico_di_Roma_Imperiale.jpg"),
    "q1094987_palazzo_massimo": thumb("Boxer_at_Rest_-_Palazzo_Massimo.jpg"),
    "q2586829_palatine_hill": thumb("Palatine_Hill_Rome.jpg"),
    "q1136615_palazzo_corsini": thumb("Caravaggio_-_San_Giovanni_Battista_-_Palazzo_Corsini.jpg"),
    "q99309_pantheon": thumb("Pantheon_Interior.jpg"),
    "q180540_roman_forum": thumb("Tempio_di_Vesta_(Foro_Romano).jpg"),
    "q112972_spanish_steps": thumb("Trinita_dei_Monti_-_Rome.jpg"),
    "q12501_st_peters_basilica": thumb("Pieta_de_Michelangelo.jpg"),
    "q502098_terme_di_caracalla": thumb("Baths_of_Caracalla_mosaic.jpg"),
    "q1741_trevi_fountain": thumb("Trevi_Fountain_at_night.jpg"),
    "q474857_villa_torlonia_rome": thumb("Casino_Nobile_-_Villa_Torlonia.jpg"),
}

TICKET_URL_FIXES: dict[str, str] = {
    "q3867587_museo_carlo_bilotti": "http://www.museocarlobilotti.it/en/visit/",
    "q1074320_museum_roman_civilization": "https://www.museociviltaromana.it/en/visit/",
}

# GetYourGuide destination pages (Places to see) — verify slug-l#### on getyourguide.com.
# Wrong IDs redirect globally (e.g. l33=Rome city, l833=Hue Vietnam, l1074=Bermuda).
TOUR_URL_FIXES: dict[str, str] = {
    "q10285_colosseum": "https://www.getyourguide.com/colosseum-l2619/",
    "q182955_vatican_museums": "https://www.getyourguide.com/vatican-museums-l2738/",
    "q841506_galleria_borghese": "https://www.getyourguide.com/borghese-gallery-l3271/",
    "q180540_roman_forum": "https://www.getyourguide.com/roman-forum-l2618/",
    "q1741_trevi_fountain": "https://www.getyourguide.com/trevi-fountain-l2898/",
    "q1971299_galleria_colonna": "https://www.getyourguide.com/galleria-colonna-l3290/",
}


def main() -> None:
    sites = json.loads(CATALOG.read_text(encoding="utf-8"))
    verified = "2026-07-04"

    for site in sites:
        sid = site["id"]
        if sid in HIGHLIGHT_IMAGE_FIXES:
            highlights = site.get("highlights") or []
            if len(highlights) >= 2:
                highlights[1]["imageUrl"] = HIGHLIGHT_IMAGE_FIXES[sid]

        vi = site.setdefault("visitingInfo", {})
        if sid in TICKET_URL_FIXES:
            vi["ticketUrl"] = TICKET_URL_FIXES[sid]
        if sid in TOUR_URL_FIXES:
            vi["tourUrl"] = TOUR_URL_FIXES[sid]

        meta = site.setdefault("_meta", {})
        if sid in HIGHLIGHT_IMAGE_FIXES or sid in TICKET_URL_FIXES or sid in TOUR_URL_FIXES:
            meta["verifiedAt"] = verified

    CATALOG.write_text(json.dumps(sites, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sync_enrichment_from_catalog(sites)
    print(f"Polished {CATALOG.name}: {len(HIGHLIGHT_IMAGE_FIXES)} highlight fixes, "
          f"{len(TICKET_URL_FIXES)} ticket URLs, {len(TOUR_URL_FIXES)} tour URLs")


def sync_enrichment_from_catalog(sites: list[dict]) -> None:
    """Keep sites_media_enrichment.py highlights in sync after manual polish."""
    import importlib.util

    enrich_path = ROOT / "tools" / "sites_media_enrichment.py"
    spec = importlib.util.spec_from_file_location("sites_media_enrichment", enrich_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    media_map: dict = dict(module.MEDIA)
    by_id = {s["id"]: s for s in sites}
    for site_id, payload in media_map.items():
        site = by_id.get(site_id)
        if site and site.get("highlights"):
            payload["highlights"] = site["highlights"]
    lines = [
        '"""Wikimedia-backed hero and highlight images for sites_base_v1.json."""',
        "",
        "from __future__ import annotations",
        "",
        "",
        "def media(hero_url: str, highlights: list[dict]) -> dict:",
        '    return {"images": [hero_url], "highlights": highlights}',
        "",
        "",
        "def hl(title: str, link: str, image_url: str) -> dict:",
        '    return {"title": title, "url": link, "imageUrl": image_url}',
        "",
        "",
        "MEDIA: dict[str, dict] = {",
    ]
    for site_id in sorted(media_map.keys()):
        payload = media_map[site_id]
        lines.append(f"    {json.dumps(site_id)}: media(")
        lines.append(f"        {json.dumps(payload['images'][0])},")
        lines.append("        [")
        for h in payload["highlights"]:
            lines.append(
                "            hl("
                f"{json.dumps(h['title'])}, "
                f"{json.dumps(h['url'])}, "
                f"{json.dumps(h['imageUrl'])}"
                "),"
            )
        lines.append("        ],")
        lines.append("    ),")
    lines.extend(
        [
            "}",
            "",
            'assert len(MEDIA) == 50, f"MEDIA must cover 50 sites, got {len(MEDIA)}"',
            "",
        ]
    )
    enrich_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Synced {enrich_path.name}")


if __name__ == "__main__":
    main()
