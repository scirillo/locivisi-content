#!/usr/bin/env python3
"""Regenerate sites_media_enrichment.py with verified upload.wikimedia.org thumb URLs."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN_PATH = ROOT / "tools" / "generate_sites_base_v1.py"
OUT_PATH = ROOT / "tools" / "sites_media_enrichment.py"
CATALOG_PATH = ROOT / "sites_base_v1.json"


def load_generate_module():
    spec = importlib.util.spec_from_file_location("generate_sites_base_v1", GEN_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def commons_thumb(file_name: str, width: int = 1280) -> str:
    canonical = file_name.replace(" ", "_")
    digest = hashlib.md5(canonical.encode("utf-8")).hexdigest()
    # Commons keeps common punctuation unescaped in the path.
    from urllib.parse import quote

    encoded = quote(canonical, safe="(),'")
    return (
        f"https://upload.wikimedia.org/wikipedia/commons/thumb/"
        f"{digest[0]}/{digest[0:2]}/{encoded}/{width}px-{encoded}"
    )


def thumb(file_name: str, width: int = 1280) -> str:
    return commons_thumb(file_name, width)


def url(raw: str) -> str:
    return raw


def hl(title: str, link: str, image: str) -> dict:
    return {"title": title, "url": link, "imageUrl": image}


def media(hero: str, highlights: list[dict]) -> dict:
    return {"images": [hero], "highlights": highlights}


# Verified Commons filenames for retained (pre-50) sites.
RETAINED: dict[str, dict] = {
    "q182955_vatican_museums": media(
        thumb("Vatican_Museums_Spiral_Staircase_2012.jpg"),
        [
            hl(
                "Sistine Chapel ceiling",
                "https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/cappella-sistina.html",
                thumb("Michelangelo_-_Creation_of_Adam_(cropped).jpg", 960),
            ),
            hl(
                "Gallery of Maps",
                "https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/galleria-delle-carte-geografiche.html",
                thumb("Vatican_Museums_-_Gallery_of_Maps_-_Sala_bella.jpg", 960),
            ),
        ],
    ),
    "q841506_galleria_borghese": media(
        thumb("Roma_Museo_Borghese.jpg"),
        [
            hl(
                "Apollo and Daphne (Bernini)",
                "https://galleriaborghese.beniculturali.it/",
                thumb("Apollo_and_Daphne_by_Bernini_(Galleria_Borghese).jpg", 960),
            ),
            hl(
                "The Rape of Proserpina (Bernini)",
                "https://galleriaborghese.beniculturali.it/",
                thumb("Rape_of_Prosepina_September_2015-3a.jpg", 960),
            ),
            hl(
                "David with the Head of Goliath (Caravaggio)",
                "https://galleriaborghese.beniculturali.it/",
                thumb("David_with_the_Head_of_Goliath-Caravaggio_(1610).jpg", 960),
            ),
        ],
    ),
    "q84090_san_giovanni_laterano": media(
        thumb("San_Giovanni_in_Laterano_2021.jpg"),
        [
            hl(
                "Façade and nave",
                "https://www.basilicasangiovanni.va/",
                thumb("San_Giovanni_in_Laterano_2021.jpg", 960),
            ),
            hl(
                "Holy Stairs and baptistery",
                "https://www.basilicasangiovanni.va/",
                thumb("Rom,_die_Heilige_Treppe.JPG", 960),
            ),
        ],
    ),
    "q186282_santa_maria_maggiore": media(
        thumb("Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg"),
        [
            hl(
                "5th-century mosaics",
                "https://www.basilicasantamariamaggiore.va/it.html",
                thumb("Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg", 960),
            ),
            hl(
                "Bernini's tomb",
                "https://www.basilicasantamariamaggiore.va/it.html",
                thumb("Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg", 960),
            ),
        ],
    ),
    "q1971299_galleria_colonna": media(
        thumb("Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG"),
        [
            hl("Great Hall", "http://www.galleriacolonna.it", thumb("Galleria_Colonna,_Rome.jpg", 960)),
            hl("Palace apartments", "http://www.galleriacolonna.it", thumb("Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG", 960)),
        ],
    ),
    "q1465674_santignazio_church": media(
        thumb("Church_of_Sant'Ignazio_di_Loyola.jpg"),
        [
            hl("Andrea Pozzo ceiling fresco", "http://santignazio.gesuiti.it/", thumb("Church_of_Sant'Ignazio_di_Loyola.jpg", 960)),
            hl("Illusionistic dome", "http://santignazio.gesuiti.it/", thumb("Church_of_Sant'Ignazio_di_Loyola.jpg", 960)),
        ],
    ),
    "q333906_capitoline_museums": media(
        thumb("0_Cordonata_-_Dioscuri_-_Palazzo_Senatorio.JPG"),
        [
            hl("Capitoline Wolf", "https://museicapitolini.org/", thumb("Capitoline_she-wolf_Musei_Capitolini_MC1181.jpg", 960)),
            hl("Colossus of Constantine", "https://museicapitolini.org/", thumb("Statua_colossale_di_Costantino_I.jpg", 960)),
        ],
    ),
    "q318660_santa_maria_aracoeli": media(
        thumb("Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg"),
        [
            hl(
                "Medieval cosmatesque floor",
                "https://en.wikipedia.org/wiki/Santa_Maria_in_Aracoeli",
                thumb("Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg", 960),
            ),
            hl(
                "Capitoline staircase",
                "https://en.wikipedia.org/wiki/Santa_Maria_in_Aracoeli",
                thumb("Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg", 960),
            ),
        ],
    ),
    "q192784_trajans_column": media(
        thumb("Trajan's_Column_HD.jpg"),
        [
            hl("Spiral relief frieze", "https://en.wikipedia.org/wiki/Trajan%27s_Column", thumb("Trajan's_Column_HD.jpg", 960)),
            hl("Forum of Trajan setting", "https://www.mercatiditraiano.it/", thumb("Mercati_di_Traiano_-_Roma.jpg", 960)),
        ],
    ),
    "q1094986_palazzo_altemps": media(
        thumb("Roma_2011_08_07_Palazzo_Altemps.jpg"),
        [
            hl(
                "Ludovisi Battle sarcophagus",
                "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/",
                thumb("Ludovisi_Battle_sarcophagus_(Altemps).jpg", 960),
            ),
            hl(
                "Renaissance courtyard",
                "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/",
                thumb("Roma_2011_08_07_Palazzo_Altemps.jpg", 960),
            ),
        ],
    ),
    "q3757712_galleria_arte_moderna_roma": media(
        thumb("Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg"),
        [
            hl("19th-century Roman art", "http://www.galleriaartemodernaroma.it", thumb("Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg", 960)),
            hl("Temporary exhibitions", "http://www.galleriaartemodernaroma.it", thumb("Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg", 960)),
        ],
    ),
    "q1362663_villa_medici": media(
        thumb("Villa_Medici_Roma_01.jpg"),
        [
            hl("French Academy gardens", "http://www.villamedici.it/", thumb("Villa_Medici_Roma_01.jpg", 960)),
            hl("Guided palace tours", "http://www.villamedici.it/", thumb("Villa_Medici_-_Rome.jpg", 960)),
        ],
    ),
    "q1136614_palazzo_barberini": media(
        thumb("Palazzo_Barberini_-_esterno.jpg"),
        [
            hl("Pietro da Cortona ceiling", "http://www.barberinicorsini.org/", thumb("Palazzo_Barberini_-_Il_trionfo_della_Divina_Provvidenza.jpg", 960)),
            hl("Caravaggio and Raphael works", "http://www.barberinicorsini.org/", thumb("Palazzo_Barberini_-_esterno.jpg", 960)),
        ],
    ),
    "q836108_baths_of_diocletian": media(
        thumb("Baths_of_Diocletian-Antmoose1.jpg"),
        [
            hl(
                "Great hall of baths",
                "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/",
                thumb("Baths_of_Diocletian-Antmoose1.jpg", 960),
            ),
            hl(
                "Garden cloister",
                "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/",
                thumb("Michelangelo_Cloister_-_Museum_of_Roman_Civilization.jpg", 960),
            ),
        ],
    ),
    "q15055388_villa_giulia_etruscan": media(
        thumb("Villa_Giulia_modified.jpg"),
        [
            hl("Sarcophagus of the Spouses", "https://www.museoetru.it/", thumb("Sarcophagus_of_the_Spouses_-_National_Etruscan_Museum.jpg", 960)),
            hl("Villa Giulia gardens", "https://www.museoetru.it/", thumb("Villa_Giulia_modified.jpg", 960)),
        ],
    ),
    "q1492387_gnamc": media(
        thumb("Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg"),
        [
            hl("19th–21st century masterpieces", "https://gnamc.cultura.gov.it/", thumb("Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg", 960)),
            hl("De Chirico and Morandi rooms", "https://gnamc.cultura.gov.it/", thumb("Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg", 960)),
        ],
    ),
    "q3867587_museo_carlo_bilotti": media(
        thumb("Roma-museoBilotti01.jpg"),
        [
            hl("Carlo Bilotti collection", "http://www.museocarlobilotti.it/", thumb("Roma-museoBilotti01.jpg", 960)),
            hl("Orangery exhibitions", "http://www.museocarlobilotti.it/", thumb("Roma-museoBilotti01.jpg", 960)),
        ],
    ),
    "q486382_castel_santangelo": media(
        thumb("Castel_Sant'Angelo_at_Night.jpg"),
        [
            hl("Ramparts and terraces", "https://castelsantangelo.beniculturali.it/", thumb("Castel_Sant'Angelo_at_Night.jpg", 960)),
            hl("Papal apartments", "https://castelsantangelo.beniculturali.it/", thumb("Castel_Sant'Angelo_-_Rome.jpg", 960)),
        ],
    ),
    "leonardo_experience_rome": media(
        thumb("Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg"),
        [
            hl("Machine inventions", "https://www.leonardodavincimuseo.com/en/", thumb("Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg", 960)),
            hl("Anatomy studies", "https://www.leonardodavincimuseo.com/en/", thumb("Leonardo_da_Vinci_-_Study_of_an_old_man.jpg", 960)),
        ],
    ),
    "q1137391_santa_maria_trastevere": media(
        thumb("01_Santa_Maria_in_Trastevere_Facade.jpg"),
        [
            hl("Apse mosaics", "https://www.santamariaintrastevere.it/", thumb("01_Santa_Maria_in_Trastevere_Facade.jpg", 960)),
            hl("Piazza fountain", "https://www.santamariaintrastevere.it/", thumb("Piazza_di_Santa_Maria_in_Trastevere.jpg", 960)),
        ],
    ),
    "q623612_ara_pacis_museum": media(
        thumb("Ara_Pacis_(SW).jpg"),
        [
            hl("Ara Pacis reliefs", "https://www.arapacis.it/", thumb("Ara_Pacis_(SW).jpg", 960)),
            hl("Richard Meier pavilion", "https://www.arapacis.it/", thumb("Ara_Pacis_(SW).jpg", 960)),
        ],
    ),
    "q3868175_museo_roma_palazzo_braschi": media(
        thumb("Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg"),
        [
            hl("Rome city history", "http://www.museodiroma.it/", thumb("Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg", 960)),
            hl("Views over Piazza Navona", "http://www.museodiroma.it/", thumb("Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg", 960)),
        ],
    ),
    "q1192577_santagnese_in_agone": media(
        thumb("Façade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg"),
        [
            hl("Borromini façade", "https://www.santagneseinagone.org/", thumb("Façade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg", 960)),
            hl("Dome frescoes", "https://www.santagneseinagone.org/", thumb("Sant'Agnese_in_Agone_(Rome)_esterno.jpg", 960)),
        ],
    ),
    "q1126723_villa_farnesina": media(
        thumb("La_villa_Farnesina_(Rome)_(34029492720).jpg"),
        [
            hl("Loggia of Psyche", "http://www.villafarnesina.it", thumb("Galatea_(Raphael)_Villa_Farnesina.jpg", 960)),
            hl("Raphael frescoes", "http://www.villafarnesina.it", thumb("La_villa_Farnesina_(Rome)_(34029492720).jpg", 960)),
        ],
    ),
    "q1258576_san_pietro_in_montorio": media(
        thumb("San_Pietro_in_Montorio_-_esterno.jpg"),
        [
            hl("Bramante's Tempietto", "http://www.sanpietroinmontorio.it/home.html", thumb("Tempietto_del_Bramante_(2).jpg", 960)),
            hl("Janiculum views", "http://www.sanpietroinmontorio.it/home.html", thumb("San_Pietro_in_Montorio_-_esterno.jpg", 960)),
        ],
    ),
    "q502098_terme_di_caracalla": media(
        thumb("Baths_of_Caracalla,_facing_Caldarium.jpg"),
        [
            hl("Monumental halls", "https://colosseo.it/en/area/terme-di-caracalla/", thumb("Baths_of_Caracalla,_facing_Caldarium.jpg", 960)),
            hl("Summer opera season", "https://colosseo.it/en/area/terme-di-caracalla/", thumb("Baths_of_Caracalla,_facing_Caldarium.jpg", 960)),
        ],
    ),
    "q231699_san_paolo_fuori_le_mura": media(
        thumb("StPaul.jpg"),
        [
            hl(
                "Basilica nave and apse",
                "http://www.vatican.va/various/basiliche/san_paolo/index_en.html",
                thumb("StPaul.jpg", 960),
            ),
            hl(
                "Cloister and mosaics",
                "http://www.vatican.va/various/basiliche/san_paolo/index_en.html",
                thumb("Saint_Paul_Outside_the_Walls_-_Cloister.jpg", 960),
            ),
        ],
    ),
    "q474857_villa_torlonia_rome": media(
        thumb("Villa_Torlonia_01304.JPG"),
        [
            hl("Historic park", "http://www.museivillatorlonia.it/", thumb("Villa_Torlonia_01304.JPG", 960)),
            hl("Casino Nobile exterior", "http://www.museivillatorlonia.it/", thumb("Villa_Torlonia_01304.JPG", 960)),
        ],
    ),
    "q17636813_musei_villa_torlonia": media(
        thumb("Casino_Nobile_-_Villa_Torlonia.jpg"),
        [
            hl("Casino Nobile", "http://www.museivillatorlonia.it", thumb("Casino_Nobile_-_Villa_Torlonia.jpg", 960)),
            hl("Casina delle Civette", "http://www.museivillatorlonia.it", thumb("Casina_delle_Civette.jpg", 960)),
        ],
    ),
    "q3867590_casina_delle_civette": media(
        thumb("Casina_delle_Civette.jpg"),
        [
            hl("Stained-glass rooms", "http://www.museivillatorlonia.it/casina_delle_civette", thumb("Casina_delle_Civette.jpg", 960)),
            hl("Art Nouveau interiors", "http://www.museivillatorlonia.it/casina_delle_civette", thumb("Casina_delle_Civette.jpg", 960)),
        ],
    ),
}


NEW_SITE_HERO_FILES: dict[str, str] = {
    "q180540_roman_forum": "Foro_Romano_-_panoramio.jpg",
    "q2586829_palatine_hill": "Foro_Romano_-_panoramio.jpg",
    "q112972_spanish_steps": "Piazza_di_Spagna_(Rome)_0004.jpg",
    "q2301489_doria_pamphilj_gallery": "Palazzo_Doria_Pamphilj.jpg",
    "q3757713_galleria_spada": "938RomaPalazzoSpada.JPG",
    "q1356135_macro_rome": "Macro_Rome.jpg",
    "q1283630_keats_shelley_house": "Keats-Shelley_House.jpg",
    "q207808_circus_maximus": "CircusMaximusSO.jpg",
    "q1053970_centrale_montemartini": "Le_musée_de_la_centrale_Montemartini_(Rome)_(33828659930).jpg",
    "q3868176_museo_napoleonico": "Museo_Napoleonico.jpg",
}

NEW_SITE_HERO_URLS: dict[str, str] = {
    "q3868408_maxxi": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/MAXXI_%2827483747665%29.jpg/1280px-MAXXI_%2827483747665%29.jpg",
    "q1094987_palazzo_massimo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Roma09_flickr.jpg/1280px-Roma09_flickr.jpg",
}


def media_from_new_site(entry: dict) -> dict:
    site_id = entry["id"]
    old_hero = entry["images"][0]
    if site_id in NEW_SITE_HERO_URLS:
        hero = NEW_SITE_HERO_URLS[site_id]
    elif site_id in NEW_SITE_HERO_FILES:
        hero = thumb(NEW_SITE_HERO_FILES[site_id])
    else:
        hero = old_hero
    highlights = []
    for h in entry["highlights"]:
        image = h.get("imageUrl") or hero
        if image == old_hero:
            image = hero
        url_ = h.get("url") or "https://en.wikipedia.org/wiki/Rome"
        highlights.append(hl(h["title"], url_, image))
    return media(hero, highlights)


def render_python(media_map: dict[str, dict]) -> str:
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
    return "\n".join(lines)


def main() -> None:
    gen = load_generate_module()
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    titles_by_id = {s["id"]: s for s in catalog}

    media_map: dict[str, dict] = dict(RETAINED)

    for entry in gen.NEW_SITES:
        site_id = entry["id"]
        base = titles_by_id[site_id]
        merged = media_from_new_site(entry)
        # Preserve official highlight links from the live catalogue patches.
        patched_highlights = []
        for merged_h, base_h in zip(merged["highlights"], base["highlights"], strict=True):
            patched_highlights.append(
                hl(
                    merged_h["title"],
                    base_h.get("url") or merged_h["url"],
                    merged_h["imageUrl"],
                )
            )
        media_map[site_id] = media(merged["images"][0], patched_highlights)

    assert len(media_map) == 50, len(media_map)
    OUT_PATH.write_text(render_python(media_map), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(media_map)} sites)")


if __name__ == "__main__":
    main()
