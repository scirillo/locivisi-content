#!/usr/bin/env python3
"""Generate sites_base_v1.json (50 Rome sites, enriched)."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sites_media_enrichment import MEDIA

VERIFIED = "2026-06-23"
OUTPUT = Path(__file__).resolve().parents[1] / "sites_base_v1.json"

FEATURED_IDS = {
    "q182955_vatican_museums",
    "q12501_st_peters_basilica",
    "q10285_colosseum",
    "q180540_roman_forum",
    "q99309_pantheon",
    "q1741_trevi_fountain",
    "q486382_castel_santangelo",
    "q333906_capitoline_museums",
    "q841506_galleria_borghese",
    "q1136614_palazzo_barberini",
    "q623612_ara_pacis_museum",
    "q15055388_villa_giulia_etruscan",
    "q502098_terme_di_caracalla",
    "q478642_mercati_traiano",
    "q112972_spanish_steps",
    "q1094987_palazzo_massimo",
    "q2301489_doria_pamphilj_gallery",
    "q84090_san_giovanni_laterano",
    "q186282_santa_maria_maggiore",
    "q3868408_maxxi",
}

REMOVE_IDS = {"q2047593_palazzo_pamphilj"}


def site(
    id_: str,
    name: str,
    type_: str,
    lat: float,
    lng: float,
    short_description: str,
    images: list[str],
    highlights: list[dict],
    visiting_info: dict,
    *,
    neighborhood: str | None = None,
    address: str | None = None,
    wikidata_id: str | None = None,
    source_urls: list[str] | None = None,
    featured: bool | None = None,
) -> dict:
    return {
        "id": id_,
        "name": name,
        "type": type_,
        "lat": lat,
        "lng": lng,
        "neighborhood": neighborhood,
        "address": address,
        "featuredOnMap": featured if featured is not None else id_ in FEATURED_IDS,
        "images": images,
        "shortDescription": short_description,
        "highlights": highlights,
        "visitingInfo": visiting_info,
        "audio": None,
        "_meta": {
            "wikidataId": wikidata_id,
            "sourceUrls": source_urls or [],
            "verifiedAt": VERIFIED,
        },
    }


def hi(title: str, url: str | None = None, image_url: str | None = None) -> dict:
    row: dict = {"title": title}
    if image_url:
        row["imageUrl"] = image_url
    if url:
        row["url"] = url
    return row


def vi(
    *,
    ticket_required: bool = False,
    reservation_recommended: bool = False,
    official_url: str | None = None,
    ticket_url: str | None = None,
    hours_note: str | None = None,
    minutes: int = 60,
) -> dict:
    return {
        "ticketRequired": ticket_required,
        "reservationRecommended": reservation_recommended,
        "officialUrl": official_url,
        "ticketUrl": ticket_url,
        "hoursNote": hours_note,
        "timeToVisitMinutes": minutes,
    }


NEW_SITES = [
    site(
        "q10285_colosseum",
        "Colosseum",
        "ARCHAEOLOGY",
        41.89021,
        12.492231,
        "Ancient Rome's great amphitheatre and one of the world's most recognisable monuments.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg"],
        [
            hi("Arena and hypogeum", "https://colosseo.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg/640px-Colosseum_in_Rome%2C_Italy_-_April_2007.jpg"),
            hi("Upper tiers and views", "https://colosseo.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://colosseo.it/",
            ticket_url="https://colosseo.it/en/tickets/",
            hours_note="Daily 9:00–19:15; last entry varies by season. Closed 1 Jan and 25 Dec.",
            minutes=90,
        ),
        neighborhood="Monti",
        address="Piazza del Colosseo, 00184 Roma",
        wikidata_id="Q10285",
        source_urls=["https://www.wikidata.org/wiki/Q10285", "https://colosseo.it/"],
    ),
    site(
        "q180540_roman_forum",
        "Roman Forum",
        "ARCHAEOLOGY",
        41.8925,
        12.4853,
        "Heart of ancient Rome with temples, basilicas, and imperial ruins in one archaeological park.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Roman_Forum_West_End_Looking_East_2013.jpg/1280px-Roman_Forum_West_End_Looking_East_2013.jpg"],
        [
            hi("Via Sacra and temples", "https://colosseo.it/en/area/foro-romano/"),
            hi("House of the Vestals", "https://colosseo.it/en/area/foro-romano/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://colosseo.it/en/area/foro-romano/",
            ticket_url="https://colosseo.it/en/tickets/",
            hours_note="Same ticket and hours as the Colosseum archaeological park.",
            minutes=120,
        ),
        neighborhood="Monti",
        address="Via della Salara Vecchia, 00186 Roma",
        wikidata_id="Q180540",
        source_urls=["https://www.wikidata.org/wiki/Q180540", "https://colosseo.it/"],
    ),
    site(
        "q2586829_palatine_hill",
        "Palatine Hill",
        "ARCHAEOLOGY",
        41.8883,
        12.4872,
        "Legendary birthplace of Rome with imperial palace ruins and views over the Forum.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/View_from_Palatine_Hill.jpg/1280px-View_from_Palatine_Hill.jpg"],
        [
            hi("Domus Augustana ruins", "https://colosseo.it/en/area/palatino/"),
            hi("Views over Circus Maximus", "https://colosseo.it/en/area/palatino/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://colosseo.it/en/area/palatino/",
            ticket_url="https://colosseo.it/en/tickets/",
            hours_note="Included with Colosseum/Forum combined ticket.",
            minutes=75,
        ),
        neighborhood="Monti",
        address="Via di San Gregorio, 00186 Roma",
        wikidata_id="Q2586829",
        source_urls=["https://www.wikidata.org/wiki/Q2586829", "https://colosseo.it/"],
        featured=False,
    ),
    site(
        "q99309_pantheon",
        "Pantheon",
        "CHURCH",
        41.8986108,
        12.4768729,
        "Best-preserved ancient Roman temple, now a church with its famous coffered dome and oculus.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pantheon_Rom_1_cropped.jpg/1280px-Pantheon_Rom_1_cropped.jpg"],
        [
            hi("Dome and oculus", "https://www.pantheonroma.com/"),
            hi("Raphael's tomb", "https://www.pantheonroma.com/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.pantheonroma.com/",
            ticket_url="https://www.pantheonroma.com/en/visit/tickets/",
            hours_note="Mon–Sat 9:00–19:00; Sun 9:00–18:00. Mass times may limit visits.",
            minutes=45,
        ),
        neighborhood="Pigna",
        address="Piazza della Rotonda, 00186 Roma",
        wikidata_id="Q99309",
        source_urls=["https://www.wikidata.org/wiki/Q99309", "https://www.pantheonroma.com/"],
    ),
    site(
        "q12501_st_peters_basilica",
        "St Peter's Basilica",
        "CHURCH",
        41.902167,
        12.453937,
        "Principal papal basilica and masterpiece of Renaissance architecture in Vatican City.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg/1280px-Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg"],
        [
            hi("Michelangelo's Pietà", "https://www.vatican.va/content/vatican/en.html"),
            hi("Dome climb", "https://www.vatican.va/content/vatican/en.html"),
        ],
        vi(
            ticket_required=False,
            reservation_recommended=True,
            official_url="https://www.vatican.va/content/vatican/en.html",
            ticket_url=None,
            hours_note="Basilica generally 7:00–19:00; dome and grottoes have separate hours and fees.",
            minutes=90,
        ),
        neighborhood="Vatican",
        address="Piazza San Pietro, 00120 Città del Vaticano",
        wikidata_id="Q12501",
        source_urls=["https://www.wikidata.org/wiki/Q12501", "https://www.vatican.va/"],
    ),
    site(
        "q1741_trevi_fountain",
        "Trevi Fountain",
        "HISTORICAL",
        41.900932,
        12.483313,
        "Baroque fountain and Rome's most famous wish-making landmark.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/1280px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg"],
        [
            hi("Oceanus façade", None),
            hi("Evening illumination", None),
        ],
        vi(
            hours_note="Outdoor monument; accessible 24 hours. Expect crowds midday and evening.",
            minutes=20,
        ),
        neighborhood="Trevi",
        address="Piazza di Trevi, 00187 Roma",
        wikidata_id="Q1741",
        source_urls=["https://www.wikidata.org/wiki/Q1741"],
    ),
    site(
        "q112972_spanish_steps",
        "Spanish Steps",
        "HISTORICAL",
        41.905837,
        12.482361,
        "Monumental staircase linking Piazza di Spagna to Trinità dei Monti.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Spanish_Steps-Rome-Italy.jpg/1280px-Spanish_Steps-Rome-Italy.jpg"],
        [
            hi("Piazza di Spagna", None),
            hi("Trinità dei Monti church", "https://www.trinitamonti.org/"),
        ],
        vi(
            hours_note="Outdoor site; sitting on steps may be restricted at times—check local rules.",
            minutes=30,
        ),
        neighborhood="Tridente",
        address="Piazza di Spagna, 00187 Roma",
        wikidata_id="Q112972",
        source_urls=["https://www.wikidata.org/wiki/Q112972"],
    ),
    site(
        "q478642_mercati_traiano",
        "Mercati di Traiano",
        "MUSEUM",
        41.8956,
        12.4864,
        "Imperial forum markets turned museum with panoramic terraces over the ancient city.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg/1280px-Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg"],
        [
            hi("Great Hall and brick vaults", "https://www.mercatiditraiano.it/"),
            hi("Forum of Trajan views", "https://www.mercatiditraiano.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.mercatiditraiano.it/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/mercati-di-traiano-museum-of-the-imperial-fora/",
            hours_note="Daily 9:30–19:30; last entry 18:30.",
            minutes=75,
        ),
        neighborhood="Monti",
        address="Via IV Novembre, 94, 00187 Roma",
        wikidata_id="Q478642",
        source_urls=["https://www.wikidata.org/wiki/Q478642", "https://www.mercatiditraiano.it/"],
    ),
    site(
        "q3868408_maxxi",
        "MAXXI - National Museum of 21st Century Arts",
        "MUSEUM",
        41.9283,
        12.4689,
        "Zaha Hadid-designed museum for contemporary art and architecture in Flaminio.",
        ["https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/MAXXI_%2827483747665%29.jpg/1280px-MAXXI_%2827483747665%29.jpg"],
        [
            hi("Permanent collections", "https://www.maxxi.art/"),
            hi("Architecture gallery", "https://www.maxxi.art/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.maxxi.art/",
            ticket_url="https://www.maxxi.art/en/visits/opening-times-and-tickets/",
            hours_note="Tue–Sun 11:00–19:00; closed Mon.",
            minutes=90,
        ),
        neighborhood="Flaminio",
        address="Via Guido Reni, 4A, 00196 Roma",
        wikidata_id="Q3868408",
        source_urls=["https://www.wikidata.org/wiki/Q3868408", "https://www.maxxi.art/"],
    ),
    site(
        "q1094987_palazzo_massimo",
        "National Roman Museum - Palazzo Massimo",
        "MUSEUM",
        41.9004,
        12.4982,
        "Outstanding classical sculpture and Roman fresco rooms near Termini.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Roma09_flickr.jpg/1280px-Roma09_flickr.jpg"],
        [
            hi("Boxer at Rest", "https://museonazionaleromano.beniculturali.it/en/palazzo-massimo/"),
            hi("Garden Villa frescoes", "https://museonazionaleromano.beniculturali.it/en/palazzo-massimo/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://museonazionaleromano.beniculturali.it/en/palazzo-massimo/",
            ticket_url="https://museonazionaleromano.beniculturali.it/en/acquista-online/",
            hours_note="Tue–Sun 11:00–18:00; closed Mon.",
            minutes=120,
        ),
        neighborhood="Esquilino",
        address="Largo di Villa Peretti, 2, 00185 Roma",
        wikidata_id="Q1094987",
        source_urls=["https://www.wikidata.org/wiki/Q1094987", "https://museonazionaleromano.beniculturali.it/"],
    ),
    site(
        "q2301489_doria_pamphilj_gallery",
        "Doria Pamphilj Gallery",
        "MUSEUM",
        41.8962,
        12.4812,
        "Private palace gallery with Velázquez, Caravaggio, and Bernini in a noble Roman residence.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Galleria_Doria_Pamphilj_%28Rome%29.jpg/1280px-Galleria_Doria_Pamphilj_%28Rome%29.jpg"],
        [
            hi("Velázquez papal portrait", "https://www.doriapamphilj.it/"),
            hi("Gallery of Mirrors", "https://www.doriapamphilj.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.doriapamphilj.it/",
            ticket_url="https://www.doriapamphilj.it/en/visit/book-your-visit/",
            hours_note="Mon–Thu and Sat–Sun 9:00–19:00; Fri 11:00–19:00.",
            minutes=90,
        ),
        neighborhood="Centro Storico",
        address="Via del Corso, 305, 00186 Roma",
        wikidata_id="Q2301489",
        source_urls=["https://www.wikidata.org/wiki/Q2301489", "https://www.doriapamphilj.it/"],
    ),
    site(
        "q3757713_galleria_spada",
        "Galleria Spada",
        "MUSEUM",
        41.8947,
        12.4722,
        "Baroque palace gallery famous for Borromini's forced-perspective colonnade.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Galleria_Spada_%28Rome%29.jpg/1280px-Galleria_Spada_%28Rome%29.jpg"],
        [
            hi("Borromini perspective gallery", "https://www.barberinicorsini.org/en/galleria-spada/"),
            hi("Caravaggio and Titian works", "https://www.barberinicorsini.org/en/galleria-spada/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.barberinicorsini.org/en/galleria-spada/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/galleria-spada/",
            hours_note="Tue–Sun 10:00–18:00; closed Mon.",
            minutes=60,
        ),
        neighborhood="Centro Storico",
        address="Piazza Capo di Ferro, 13, 00186 Roma",
        wikidata_id="Q3757713",
        source_urls=["https://www.wikidata.org/wiki/Q3757713", "https://www.barberinicorsini.org/"],
        featured=False,
    ),
    site(
        "q1053970_centrale_montemartini",
        "Centrale Montemartini",
        "MUSEUM",
        41.8722,
        12.4786,
        "Former power plant displaying classical sculptures amid industrial machinery.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Centrale_Montemartini_Roma.jpg/1280px-Centrale_Montemartini_Roma.jpg"],
        [
            hi("Sculpture in turbine hall", "https://museonazionaleromano.beniculturali.it/en/centrale-montemartini/"),
            hi("Mosaic and portrait rooms", "https://museonazionaleromano.beniculturali.it/en/centrale-montemartini/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://museonazionaleromano.beniculturali.it/en/centrale-montemartini/",
            ticket_url="https://museonazionaleromano.beniculturali.it/en/acquista-online/",
            hours_note="Tue–Sun 9:00–19:00; closed Mon.",
            minutes=90,
        ),
        neighborhood="Ostiense",
        address="Via Ostiense, 106, 00154 Roma",
        wikidata_id="Q1053970",
        source_urls=["https://www.wikidata.org/wiki/Q1053970", "https://museonazionaleromano.beniculturali.it/"],
        featured=False,
    ),
    site(
        "q1356135_macro_rome",
        "MACRO - Museum of Contemporary Art of Rome",
        "MUSEUM",
        41.9242,
        12.5012,
        "Contemporary art museum in a former Peroni brewery in Salario/Nomentano.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/MACRO_Roma.jpg/1280px-MACRO_Roma.jpg"],
        [
            hi("Temporary exhibitions", "https://www.macro.roma.it/"),
            hi("Permanent collection", "https://www.macro.roma.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.macro.roma.it/",
            ticket_url="https://www.macro.roma.it/en/visit/",
            hours_note="Tue–Sun 10:00–19:00; closed Mon.",
            minutes=75,
        ),
        neighborhood="Salario",
        address="Via Nizza, 138, 00198 Roma",
        wikidata_id="Q1356135",
        source_urls=["https://www.wikidata.org/wiki/Q1356135", "https://www.macro.roma.it/"],
        featured=False,
    ),
    site(
        "q724816_jewish_museum_rome",
        "Jewish Museum of Rome",
        "MUSEUM",
        41.8914,
        12.4772,
        "Museum beneath the Great Synagogue tracing two millennia of Roman Jewish history.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Great_Synagogue_of_Rome.jpg/1280px-Great_Synagogue_of_Rome.jpg"],
        [
            hi("Synagogue and museum tour", "https://www.museoebraico.roma.it/en/"),
            hi("Jewish Ghetto context", "https://www.museoebraico.roma.it/en/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://www.museoebraico.roma.it/en/",
            ticket_url="https://www.museoebraico.roma.it/en/visit/booking/",
            hours_note="Sun–Thu guided visits; hours vary—book ahead.",
            minutes=60,
        ),
        neighborhood="Ghetto",
        address="Lungotevere de' Cenci, 00186 Roma",
        wikidata_id="Q724816",
        source_urls=["https://www.wikidata.org/wiki/Q724816", "https://www.museoebraico.roma.it/"],
        featured=False,
    ),
    site(
        "q1283630_keats_shelley_house",
        "Keats-Shelley Memorial House",
        "MUSEUM",
        41.9056,
        12.4822,
        "House museum at the Spanish Steps where John Keats spent his final months.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Keats-Shelley_House.jpg/1280px-Keats-Shelley_House.jpg"],
        [
            hi("Keats's room", "https://ksh.roma.it/"),
            hi("Romantic poets library", "https://ksh.roma.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://ksh.roma.it/",
            ticket_url="https://ksh.roma.it/visit/",
            hours_note="Mon–Sat 10:00–13:00 and 14:00–18:00; closed Sun.",
            minutes=45,
        ),
        neighborhood="Tridente",
        address="Piazza di Spagna, 26, 00187 Roma",
        wikidata_id="Q1283630",
        source_urls=["https://www.wikidata.org/wiki/Q1283630", "https://ksh.roma.it/"],
        featured=False,
    ),
    site(
        "q1136615_palazzo_corsini",
        "Palazzo Corsini - National Gallery of Ancient Art",
        "MUSEUM",
        41.8894,
        12.4675,
        "Baroque palace in Trastevere with Caravaggio, Rubens, and river-side gardens.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Palazzo_Corsini_%28Rome%29.jpg/1280px-Palazzo_Corsini_%28Rome%29.jpg"],
        [
            hi("Caravaggio Saint John", "https://www.barberinicorsini.org/en/palazzo-corsini/"),
            hi("Botanical garden access", "https://www.barberinicorsini.org/en/palazzo-corsini/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.barberinicorsini.org/en/palazzo-corsini/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/palazzo-corsini/",
            hours_note="Tue–Sun 10:00–18:00; closed Mon.",
            minutes=90,
        ),
        neighborhood="Trastevere",
        address="Via della Lungara, 10, 00165 Roma",
        wikidata_id="Q1136615",
        source_urls=["https://www.wikidata.org/wiki/Q1136615", "https://www.barberinicorsini.org/"],
        featured=False,
    ),
    site(
        "q3868176_museo_napoleonico",
        "Museo Napoleonico",
        "MUSEUM",
        41.9031,
        12.4692,
        "Collection on Napoleon and his family in a Renaissance palace near Piazza Navona.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Museo_Napoleonico_Roma.jpg/1280px-Museo_Napoleonico_Roma.jpg"],
        [
            hi("Bonaparte family portraits", "https://www.museonapoleonico.it/"),
            hi("Period furnishings", "https://www.museonapoleonico.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.museonapoleonico.it/",
            ticket_url="https://www.museonapoleonico.it/en/visit/",
            hours_note="Tue–Sun 10:00–18:00; closed Mon.",
            minutes=60,
        ),
        neighborhood="Centro Storico",
        address="Piazza di Ponte Umberto I, 1, 00186 Roma",
        wikidata_id="Q3868176",
        source_urls=["https://www.wikidata.org/wiki/Q3868176", "https://www.museonapoleonico.it/"],
        featured=False,
    ),
    site(
        "q1074320_museum_roman_civilization",
        "Museum of Roman Civilization",
        "MUSEUM",
        41.8325,
        12.4678,
        "EUR district museum with a vast model of ancient Rome and everyday Roman life displays.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Museo_della_Civilt%C3%A0_Romana.jpg/1280px-Museo_della_Civilt%C3%A0_Romana.jpg"],
        [
            hi("Plastico di Roma Imperiale", "https://www.museociviltaromana.it/"),
            hi("Daily life collections", "https://www.museociviltaromana.it/"),
        ],
        vi(
            ticket_required=True,
            reservation_recommended=False,
            official_url="https://www.museociviltaromana.it/",
            ticket_url=None,
            hours_note="Check official site for current opening—hours have changed during renovations.",
            minutes=90,
        ),
        neighborhood="EUR",
        address="Piazza Giovanni Agnelli, 10, 00144 Roma",
        wikidata_id="Q1074320",
        source_urls=["https://www.wikidata.org/wiki/Q1074320", "https://www.museociviltaromana.it/"],
        featured=False,
    ),
    site(
        "q207808_circus_maximus",
        "Circus Maximus",
        "ARCHAEOLOGY",
        41.8859,
        12.4857,
        "Ancient chariot-racing stadium now a public park with views toward the Palatine.",
        ["https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Circo_Massimo_%28Roma%29.jpg/1280px-Circo_Massimo_%28Roma%29.jpg"],
        [
            hi("Track and spina ruins", None),
            hi("Palatine Hill backdrop", None),
        ],
        vi(
            hours_note="Outdoor archaeological area; walkable park open daily.",
            minutes=30,
        ),
        neighborhood="Circo Massimo",
        address="Via del Circo Massimo, 00186 Roma",
        wikidata_id="Q207808",
        source_urls=["https://www.wikidata.org/wiki/Q207808"],
        featured=False,
    ),
]

# Patches applied to retained existing sites (by id).
PATCHES: dict[str, dict] = {
    "q182955_vatican_museums": {
        "neighborhood": "Vatican",
        "address": "Viale Vaticano, 00120 Città del Vaticano",
    },
    "q841506_galleria_borghese": {
        "neighborhood": "Pinciano",
        "address": "Piazzale Scipione Borghese, 5, 00197 Roma",
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://galleriaborghese.beniculturali.it/",
            ticket_url="https://ticketvisit.pierreci.it/categoria/galleria-borghese",
            hours_note="Tue–Sun by timed entry; closed Mon.",
            minutes=120,
        ),
    },
    "q84090_san_giovanni_laterano": {
        "neighborhood": "Laterano",
        "address": "Piazza di San Giovanni in Laterano, 00184 Roma",
        "highlights": [
            hi("Façade and nave", "https://www.basilicasangiovanni.va/"),
            hi("Holy Stairs and baptistery", "https://www.basilicasangiovanni.va/"),
        ],
        "visitingInfo": vi(
            official_url="https://www.basilicasangiovanni.va/",
            hours_note="Basilica daily 7:00–18:30; cloister and baptistery may require tickets.",
            minutes=60,
        ),
    },
    "q186282_santa_maria_maggiore": {
        "neighborhood": "Esquilino",
        "address": "Piazza di Santa Maria Maggiore, 00185 Roma",
        "highlights": [
            hi("5th-century mosaics", "https://www.basilicasantamariamaggiore.va/"),
            hi("Bernini's tomb", "https://www.basilicasantamariamaggiore.va/"),
        ],
        "visitingInfo": vi(
            official_url="https://www.basilicasantamariamaggiore.va/it.html",
            hours_note="Daily 7:00–18:45; papal museum has separate hours.",
            minutes=60,
        ),
    },
    "q1971299_galleria_colonna": {
        "neighborhood": "Centro Storico",
        "address": "Via della Pilotta, 17, 00187 Roma",
        "highlights": [
            hi("Great Hall", "http://www.galleriacolonna.it"),
            hi("Colonna family apartments", "http://www.galleriacolonna.it"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="http://www.galleriacolonna.it",
            ticket_url="http://www.galleriacolonna.it/visit/",
            hours_note="Sat 9:00–13:15; some Fri mornings—check official calendar.",
            minutes=90,
        ),
    },
    "q1465674_santignazio_church": {
        "neighborhood": "Pigna",
        "address": "Via del Caravita, 8a, 00186 Roma",
        "highlights": [
            hi("Andrea Pozzo ceiling", "http://santignazio.gesuiti.it/"),
            hi("Illusionistic dome", "http://santignazio.gesuiti.it/"),
        ],
        "visitingInfo": vi(
            official_url="http://santignazio.gesuiti.it/",
            hours_note="Daily 7:30–19:00; respect services.",
            minutes=45,
        ),
    },
    "q333906_capitoline_museums": {
        "neighborhood": "Campidoglio",
        "address": "Piazza del Campidoglio, 00186 Roma",
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://museicapitolini.org/",
            ticket_url="https://www.ticketing.museicapitolini.org/",
            hours_note="Daily 9:30–19:30; last entry 18:30.",
            minutes=120,
        ),
    },
    "q318660_santa_maria_aracoeli": {
        "neighborhood": "Campidoglio",
        "address": "Scala dell'Arce Capitolina, 12, 00186 Roma",
        "highlights": [
            hi("Medieval cosmatesque floor", None),
            hi("Capitoline staircase", None),
        ],
        "visitingInfo": vi(
            official_url="https://www.basilicasantamariamaggiore.va/",
            hours_note="Daily 9:00–17:30; hours may vary on feast days.",
            minutes=45,
        ),
    },
    "q192784_trajans_column": {
        "neighborhood": "Monti",
        "address": "Via dei Fori Imperiali, 00186 Roma",
        "highlights": [
            hi("Spiral relief frieze", None),
            hi("Forum of Trajan setting", "https://www.mercatiditraiano.it/"),
        ],
    },
    "q1094986_palazzo_altemps": {
        "neighborhood": "Ponte",
        "address": "Piazza di Sant'Apollinare, 46, 00186 Roma",
        "highlights": [
            hi("Ludovisi Battle sarcophagus", "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/"),
            hi("Renaissance courtyard", "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/",
            ticket_url="https://museonazionaleromano.beniculturali.it/en/acquista-online/",
            hours_note="Tue–Sun 11:00–18:00; closed Mon.",
            minutes=90,
        ),
    },
    "q3757712_galleria_arte_moderna_roma": {
        "neighborhood": "Nomentano",
        "address": "Via Francesco Crispi, 24, 00187 Roma",
        "highlights": [
            hi("19th-century Roman art", "http://www.galleriaartemodernaroma.it"),
            hi("Temporary exhibitions", "http://www.galleriaartemodernaroma.it"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.galleriaartemodernaroma.it",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/galleria-d-arte-moderna/",
            hours_note="Tue–Sun 10:00–18:30; closed Mon.",
            minutes=75,
        ),
    },
    "q1362663_villa_medici": {
        "neighborhood": "Pinciano",
        "address": "Viale della Trinità dei Monti, 1, 00187 Roma",
        "highlights": [
            hi("French Academy gardens", "http://www.villamedici.it/"),
            hi("Guided palace tours", "http://www.villamedici.it/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="http://www.villamedici.it/",
            ticket_url="https://www.villamedici.it/en/visit/",
            hours_note="Guided tours on set schedule—book on official site.",
            minutes=90,
        ),
    },
    "q1136614_palazzo_barberini": {
        "neighborhood": "Trevi",
        "address": "Via delle Quattro Fontane, 13, 00187 Roma",
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="http://www.barberinicorsini.org/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/palazzo-barberini/",
            hours_note="Tue–Sun 10:00–18:00; closed Mon.",
            minutes=100,
        ),
    },
    "q836108_baths_of_diocletian": {
        "neighborhood": "Esquilino",
        "address": "Viale Enrico de Nicola, 78, 00185 Roma",
        "highlights": [
            hi("Great hall of baths", "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/"),
            hi("Garden cloister", "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/",
            ticket_url="https://museonazionaleromano.beniculturali.it/en/acquista-online/",
            hours_note="Tue–Sun 11:00–18:00; closed Mon.",
            minutes=90,
        ),
    },
    "q15055388_villa_giulia_etruscan": {
        "neighborhood": "Pinciano",
        "address": "Piazzale di Villa Giulia, 9, 00196 Roma",
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://www.museoetru.it/",
            ticket_url="https://www.museoetru.it/en/visit/tickets/",
            hours_note="Tue–Sun 9:00–20:00; closed Mon.",
            minutes=90,
        ),
    },
    "q1492387_gnamc": {
        "neighborhood": "Pinciano",
        "address": "Viale delle Belle Arti, 131, 00197 Roma",
        "highlights": [
            hi("19th–21st century masterpieces", "https://gnamc.cultura.gov.it/"),
            hi("De Chirico and Morandi rooms", "https://gnamc.cultura.gov.it/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="https://gnamc.cultura.gov.it/",
            ticket_url="https://gnamc.cultura.gov.it/en/visit/",
            hours_note="Tue–Sun 9:00–19:00; closed Mon.",
            minutes=90,
        ),
    },
    "q3867587_museo_carlo_bilotti": {
        "neighborhood": "Pinciano",
        "address": "Viale Fiorello La Guardia, 6, 00197 Roma",
        "highlights": [
            hi("Carlo Bilotti collection", "http://www.museocarlobilotti.it/"),
            hi("Orangery exhibitions", "http://www.museocarlobilotti.it/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.museocarlobilotti.it/",
            hours_note="Tue–Sun 10:00–16:00; closed Mon.",
            minutes=60,
        ),
    },
    "q486382_castel_santangelo": {
        "neighborhood": "Borgo",
        "address": "Lungotevere Castello, 50, 00193 Roma",
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://castelsantangelo.beniculturali.it/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/castel-sant-angelo/",
            hours_note="Tue–Sun 9:00–19:30; closed Mon.",
            minutes=90,
        ),
    },
    "leonardo_experience_rome": {
        "neighborhood": "Borgo",
        "visitingInfo": vi(
            ticket_required=True,
            official_url="https://www.leonardodavincimuseo.com/en/",
            ticket_url="https://www.leonardodavincimuseo.com/en/prodotto/leonardo-da-vinci-experience-museum/",
            hours_note="Daily 9:00–19:00.",
            minutes=60,
        ),
        "highlights": [
            hi("Machine inventions", "https://www.leonardodavincimuseo.com/en/"),
            hi("Anatomy studies", "https://www.leonardodavincimuseo.com/en/"),
        ],
    },
    "q1137391_santa_maria_trastevere": {
        "neighborhood": "Trastevere",
        "address": "Piazza di Santa Maria in Trastevere, 00153 Roma",
        "highlights": [
            hi("Apse mosaics", "https://www.santamariaintrastevere.it/"),
            hi("Piazza fountain", "https://www.santamariaintrastevere.it/"),
        ],
        "visitingInfo": vi(
            official_url="https://www.santamariaintrastevere.it/",
            hours_note="Daily 8:00–20:00; respect liturgies.",
            minutes=45,
        ),
    },
    "q623612_ara_pacis_museum": {
        "neighborhood": "Campo Marzio",
        "address": "Lungotevere in Augusta, 00186 Roma",
        "highlights": [
            hi("Ara Pacis reliefs", "https://www.arapacis.it/"),
            hi("Richard Meier pavilion", "https://www.arapacis.it/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="https://www.arapacis.it/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/ara-pacis-museum/",
            hours_note="Daily 9:30–19:30; closed Mon.",
            minutes=60,
        ),
    },
    "q3868175_museo_roma_palazzo_braschi": {
        "neighborhood": "Parione",
        "address": "Piazza di San Pantaleo, 10, 00186 Roma",
        "highlights": [
            hi("Rome city history", "http://www.museodiroma.it/"),
            hi("Views over Piazza Navona", "http://www.museodiroma.it/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.museodiroma.it/",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/museo-di-roma-palazzo-braschi/",
            hours_note="Tue–Sun 10:00–19:00; closed Mon.",
            minutes=75,
        ),
    },
    "q1192577_santagnese_in_agone": {
        "neighborhood": "Parione",
        "address": "Via di Santa Maria dell'Anima, 30, 00186 Roma",
        "highlights": [
            hi("Borromini façade", "https://www.santagneseinagone.org/"),
            hi("Dome frescoes", "https://www.santagneseinagone.org/"),
        ],
        "visitingInfo": vi(
            official_url="https://www.santagneseinagone.org/",
            hours_note="Daily 9:00–13:00 and 15:00–19:00; hours may vary.",
            minutes=40,
        ),
    },
    "q1126723_villa_farnesina": {
        "neighborhood": "Trastevere",
        "address": "Via della Lungara, 230, 00165 Roma",
        "highlights": [
            hi("Loggia of Psyche", "http://www.villafarnesina.it"),
            hi("Raphael frescoes", "http://www.villafarnesina.it"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.villafarnesina.it",
            ticket_url="https://www.villafarnesina.it/en/visit/booking/",
            hours_note="Mon–Sat 9:00–17:00; closed Sun.",
            minutes=75,
        ),
    },
    "q1258576_san_pietro_in_montorio": {
        "neighborhood": "Trastevere",
        "address": "Piazza San Pietro in Montorio, 2, 00153 Roma",
        "highlights": [
            hi("Bramante's Tempietto", "http://www.sanpietroinmontorio.it/home.html"),
            hi("Janiculum views", "http://www.sanpietroinmontorio.it/home.html"),
        ],
        "visitingInfo": vi(
            official_url="http://www.sanpietroinmontorio.it/home.html",
            hours_note="Daily 8:30–12:00 and 15:00–18:00; Tempietto in cloister.",
            minutes=45,
        ),
    },
    "q502098_terme_di_caracalla": {
        "neighborhood": "Appio Latino",
        "address": "Viale delle Terme di Caracalla, 52, 00179 Roma",
        "highlights": [
            hi("Monumental halls", "https://colosseo.it/en/area/terme-di-caracalla/"),
            hi("Summer opera season", "https://colosseo.it/en/area/terme-di-caracalla/"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            reservation_recommended=True,
            official_url="https://colosseo.it/en/area/terme-di-caracalla/",
            ticket_url="https://colosseo.it/en/tickets/",
            hours_note="Tue–Sun 9:00 until sunset; closed Mon.",
            minutes=90,
        ),
    },
    "q231699_san_paolo_fuori_le_mura": {
        "neighborhood": "Ostiense",
        "address": "Piazzale San Paolo, 1, 00146 Roma",
        "highlights": [
            hi("Basilica nave and apse", "http://www.vatican.va/various/basiliche/san_paolo/index_en.html"),
            hi("Cloister and mosaics", "http://www.vatican.va/various/basiliche/san_paolo/index_en.html"),
        ],
        "visitingInfo": vi(
            official_url="http://www.vatican.va/various/basiliche/san_paolo/index_en.html",
            hours_note="Daily 7:00–18:30; cloister ticket separate.",
            minutes=60,
        ),
    },
    "q474857_villa_torlonia_rome": {
        "neighborhood": "Nomentano",
        "address": "Via Nomentana, 70, 00161 Roma",
        "highlights": [
            hi("Historic park", "http://www.museivillatorlonia.it/"),
            hi("Casino Nobile exterior", "http://www.museivillatorlonia.it/"),
        ],
        "visitingInfo": vi(
            official_url="http://www.museivillatorlonia.it/",
            hours_note="Park open daily; museum buildings have separate hours.",
            minutes=90,
        ),
    },
    "q17636813_musei_villa_torlonia": {
        "neighborhood": "Nomentano",
        "address": "Via Nomentana, 70, 00161 Roma",
        "highlights": [
            hi("Casino Nobile", "http://www.museivillatorlonia.it"),
            hi("Casina delle Civette", "http://www.museivillatorlonia.it"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.museivillatorlonia.it",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/villa-torlonia-museums/",
            hours_note="Tue–Sun 9:00–19:00; closed Mon.",
            minutes=90,
        ),
    },
    "q3867590_casina_delle_civette": {
        "neighborhood": "Nomentano",
        "address": "Via Nomentana, 70, 00161 Roma",
        "highlights": [
            hi("Stained-glass rooms", "http://www.museivillatorlonia.it/casina_delle_civette"),
            hi("Art Nouveau interiors", "http://www.museivillatorlonia.it/casina_delle_civette"),
        ],
        "visitingInfo": vi(
            ticket_required=True,
            official_url="http://www.museivillatorlonia.it/casina_delle_civette",
            ticket_url="https://www.coopculture.it/en/events/museums-and-places/casina-delle-civette/",
            hours_note="Tue–Sun 9:00–19:00; closed Mon.",
            minutes=60,
        ),
    },
}


def normalize_highlight(h: dict) -> dict:
    url = h.get("url") or h.get(",url")
    out = {"title": h["title"]}
    if h.get("imageUrl"):
        out["imageUrl"] = h["imageUrl"]
    if url:
        out["url"] = url
    return out


def apply_media(s: dict) -> None:
    media = MEDIA.get(s["id"])
    if not media:
        return
    s["images"] = media["images"]
    s["highlights"] = media["highlights"]


def normalize_site(raw: dict) -> dict:
    s = deepcopy(raw)
    s.pop(",url", None)
    s["highlights"] = [normalize_highlight(h) for h in s.get("highlights", [])]
    s["_meta"]["verifiedAt"] = VERIFIED
    patch = PATCHES.get(s["id"], {})
    for key, value in patch.items():
        s[key] = value
    apply_media(s)
    s["featuredOnMap"] = s["id"] in FEATURED_IDS
    return s


def finalize_new_site(s: dict) -> dict:
    out = deepcopy(s)
    out["highlights"] = [normalize_highlight(h) for h in out.get("highlights", [])]
    out["_meta"]["verifiedAt"] = VERIFIED
    apply_media(out)
    out["featuredOnMap"] = out["id"] in FEATURED_IDS
    return out


def main() -> None:
    current_path = OUTPUT
    with current_path.open(encoding="utf-8") as f:
        current = json.load(f)

    new_ids = {s["id"] for s in NEW_SITES}
    retained = [
        normalize_site(s)
        for s in current
        if s["id"] not in REMOVE_IDS and s["id"] not in new_ids
    ]
    combined = retained + [finalize_new_site(s) for s in NEW_SITES]
    combined.sort(key=lambda s: s["name"].lower())

    assert len(combined) == 50, f"Expected 50 sites, got {len(combined)}"
    assert len(FEATURED_IDS) == 20
    featured_count = sum(1 for s in combined if s.get("featuredOnMap"))
    assert featured_count == 20, f"Expected 20 featured, got {featured_count}"

    for s in combined:
        assert s.get("shortDescription"), s["id"]
        assert s.get("images") and s["images"][0], s["id"]
        assert len(s.get("highlights", [])) >= 2, s["id"]
        for h in s["highlights"]:
            assert h.get("imageUrl"), f"{s['id']} highlight '{h.get('title')}' missing imageUrl"
            assert h.get("url"), f"{s['id']} highlight '{h.get('title')}' missing url"
        assert s.get("visitingInfo"), s["id"]
        vi_obj = s["visitingInfo"]
        assert vi_obj.get("hoursNote") or vi_obj.get("officialUrl") or vi_obj.get("ticketUrl"), s["id"]

    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(combined)} sites to {OUTPUT}")
    print(f"Featured on map: {featured_count}")
    print(f"Removed: {', '.join(sorted(REMOVE_IDS))}")


if __name__ == "__main__":
    main()
