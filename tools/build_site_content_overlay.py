#!/usr/bin/env python3
"""Build cities/rome/site_content_{lang}.json overlays from sites_base_v1.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sites_base_v1.json"
OUT_DIR = ROOT / "cities/rome"
IOS_OUT_DIR = ROOT.parent / "locivisi-ios/Locivisi/Resources/cities/rome"

# Italian display names where the base catalogue uses English.
NAMES_IT: dict[str, str] = {
    "q623612_ara_pacis_museum": "Museo dell'Ara Pacis",
    "q84090_san_giovanni_laterano": "Arcibasilica di San Giovanni in Laterano",
    "q1137391_santa_maria_trastevere": "Basilica di Santa Maria in Trastevere",
    "q231699_san_paolo_fuori_le_mura": "Basilica papale di San Paolo fuori le mura",
    "q486382_castel_santangelo": "Castel Sant'Angelo",
    "q1053970_centrale_montemartini": "Centrale Montemartini",
    "q207808_circus_maximus": "Circo Massimo",
    "q10285_colosseum": "Colosseo",
    "q2301489_doria_pamphilj_gallery": "Galleria Doria Pamphilj",
    "q1971299_galleria_colonna": "Galleria Colonna",
    "q724816_jewish_museum_rome": "Museo Ebraico di Roma",
    "q1283630_keats_shelley_house": "Casa museo Keats-Shelley",
    "leonardo_experience_rome": "Museo Leonardo Da Vinci Experience",
    "q1356135_macro_rome": "MACRO - Museo di Arte Contemporanea di Roma",
    "q3868408_maxxi": "MAXXI - Museo nazionale delle arti del XXI secolo",
    "q478642_mercati_traiano": "Mercati di Traiano",
    "q17636813_musei_villa_torlonia": "Musei di Villa Torlonia",
    "q3867587_museo_carlo_bilotti": "Museo Carlo Bilotti",
    "q3868175_museo_roma_palazzo_braschi": "Museo di Roma - Palazzo Braschi",
    "q3868176_museo_napoleonico": "Museo Napoleonico",
    "q1094986_palazzo_altemps": "Museo Nazionale Romano - Palazzo Altemps",
    "q1074320_museum_roman_civilization": "Museo della Civiltà Romana",
    "q15055388_villa_giulia_etruscan": "Museo Nazionale Etrusco di Villa Giulia",
    "q1492387_gnamc": "Galleria Nazionale d'Arte Moderna e Contemporanea",
    "q836108_baths_of_diocletian": "Museo Nazionale Romano - Terme di Diocleziano",
    "q1094987_palazzo_massimo": "Museo Nazionale Romano - Palazzo Massimo",
    "q2586829_palatine_hill": "Palatino",
    "q1136614_palazzo_barberini": "Palazzo Barberini",
    "q1136615_palazzo_corsini": "Palazzo Corsini - Galleria Nazionale d'Arte Antica",
    "q99309_pantheon": "Pantheon",
    "q180540_roman_forum": "Foro Romano",
    "q112972_spanish_steps": "Scalinata di Trinità dei Monti",
    "q12501_st_peters_basilica": "Basilica di San Pietro",
    "q192784_trajans_column": "Colonna Traiana",
    "q1741_trevi_fountain": "Fontana di Trevi",
    "q182955_vatican_museums": "Musei Vaticani",
    "q1126723_villa_farnesina": "Villa Farnesina",
    "q1362663_villa_medici": "Villa Medici",
    "q474857_villa_torlonia_rome": "Villa Torlonia",
}


def polish_it(text: str) -> str:
    """Fix leftover English glue words after phrase replacements."""
    replacements = [
        (" and ", " e "),
        (" with ", " con "),
        (" featuring ", ", con "),
        (" known for ", " noto per "),
        (" celebrated for ", " celebre per "),
        (" focused on ", " dedicato a "),
        (" dedicated to ", " dedicato a "),
        (" in Rome", " a Roma"),
        (" in central Rome", " nel centro di Roma"),
        (" in Trastevere", " a Trastevere"),
        (" in Vatican City", " in Città del Vaticano"),
        (" in Flaminio", " a Flaminio"),
        (" on Capitoline Hill", " sul Campidoglio"),
        (" on the Janiculum hill", " sul Gianicolo"),
        (" on Piazza Navona", " su Piazza Navona"),
        (" near the Tiber", " vicino al Tevere"),
        (" near Termini", " vicino a Termini"),
        (" amid industrial machinery", " tra i macchinari industriali"),
        (" Renaissance masterpieces", " capolavori del Rinascimento"),
        (" Renaissance architecture", " architettura rinascimentale"),
        (" medieval mosaics", " mosaici medievali"),
        (" lively piazza setting", " vivace piazza"),
        (" historical significance", " rilevanza storica"),
        (" illusionistic frescoes", " affreschi illusionistici"),
        (" Jesuit history", " storia gesuita"),
        (" panoramic terraces", " terrazze panoramiche"),
        (" aristocratic collections", " collezioni aristocratiche"),
        (" richly decorated halls", " sale riccamente decorate"),
        (" contemporary Roman and Italian art", " arte romana e italiana moderna e contemporanea"),
        (" tracing two millennia of Roman Jewish history", " che racconta duemila anni di storia ebraica romana"),
        (" inventions and reproductions", " invenzioni e riproduzioni"),
        (" everyday Roman life displays", " reperti della vita quotidiana romana"),
        (" imperial palace ruins", " rovine dei palazzi imperiali"),
        (" views over the Forum", " vista sul Foro"),
        (" river-side gardens", " giardini sul fiume"),
        (" landscaped grounds", " parchi storici"),
        (" multiple exhibition spaces", " diversi spazi espositivi"),
        (" multiple museum venues", " diverse sedi museali"),
        (" rotating exhibitions", " mostre temporanee"),
        (" separate hours", " orari separati"),
        (" feast days", " giorni festivi"),
        (" last entry ", " ultimo ingresso "),
        ("Last Sun of month", "Ultima domenica del mese"),
        ("respect liturgies", "rispetta le liturgie"),
        ("may vary on", "possono variare nei"),
        ("potrebbero richiedere biglietto", "potrebbero richiedere biglietto"),
        ("cloister and baptistery", "chiostro e battistero"),
        ("Basilica nave and apse", "Navata e abside della basilica"),
        ("Medieval cosmatesque floor", "Pavimento cosmatesco medievale"),
        ("Capitoline staircase", "Scalinata del Campidoglio"),
        ("5th-century mosaics", "Mosaici del V secolo"),
        ("Bernini's tomb", "Tomba del Bernini"),
        ("Apse mosaics", "Mosaici dell'abside"),
        ("Piazza fountain", "Fontana della piazza"),
        ("Sistine Chapel ceiling", "Volta della Cappella Sistina"),
        ("Gallery of Maps", "Galleria delle Carte geografiche"),
        ("Loggia of Psyche", "Loggia di Psiche"),
        ("Raphael frescoes", "Affreschi di Raffaello"),
        ("the Ara Pacis", "l'Ara Pacis"),
        ("an Augustan altar monument", "un altare monumentale augusteo"),
        ("an important Marian sanctuary", "un importante santuario mariano"),
        ("Saint Paul", "San Paolo"),
        ("transformed into fortress and museum", "trasformato in fortezza e museo"),
        ("displaying classical sculptures", "con sculture classiche"),
        ("reached by a monumental staircase", "raggiungibile con una scalinata monumentale"),
        ("now a public park", "oggi un parco pubblico"),
        ("with views toward the Palatine", "con vista sul Palatino"),
        ("in a noble Roman residence", "in una residenza nobiliare romana"),
        ("renowned for Bernini sculptures and Caravaggio paintings", "celebre per le sculture del Bernini e i dipinti del Caravaggio"),
        ("famous for Borromini's forced-perspective colonnade", "famoso per il colonnato prospettico del Borromini"),
        ("where John Keats spent his final months", "dove John Keats trascorse i suoi ultimi mesi"),
        ("housed in a Renaissance villa", "ospitato in una villa rinascimentale"),
        ("housed in the neoclassical Palazzo Braschi", "ospitato nel neoclassico Palazzo Braschi"),
        ("within the National Roman Museum system", "nel circuito del Museo Nazionale Romano"),
        ("integrated into the National Roman Museum itinerary", "integrato nell'itinerario del Museo Nazionale Romano"),
        ("and Roman fresco rooms", " e sale con affreschi romani"),
        ("in one archaeological park", " in un unico parco archeologico"),
        ("commemorating Trajan's Dacian campaigns", "che commemora le campagne daciche di Traiano"),
        ("Rome's civic museums", "Musei civici di Roma"),
        ("including ", "con "),
    ]
    for src, dst in replacements:
        text = text.replace(src, dst)
    return text


HIGHLIGHTS_IT: dict[str, str] = {
    "Sistine Chapel ceiling": "Volta della Cappella Sistina",
    "Gallery of Maps": "Galleria delle Carte geografiche",
    "Arena and hypogeum": "Arena e ipogei",
    "Upper tiers view": "Vista dai piani superiori",
    "Façade and nave": "Facciata e navata",
    "Holy Stairs and baptistery": "Scala Santa e battistero",
    "Ara Pacis reliefs": "Rilievi dell'Ara Pacis",
    "Richard Meier pavilion": "Padiglione di Richard Meier",
    "Apse mosaics": "Mosaici dell'abside",
    "Piazza fountain": "Fontana della piazza",
    "Basilica nave and apse": "Navata e abside della basilica",
    "Medieval cosmatesque floor": "Pavimento cosmatesco medievale",
    "Capitoline staircase": "Scalinata del Campidoglio",
    "5th-century mosaics": "Mosaici del V secolo",
    "Bernini's tomb": "Tomba del Bernini",
    "Loggia of Psyche": "Loggia di Psiche",
    "Raphael frescoes": "Affreschi di Raffaello",
    "Apollo and Daphne (Bernini)": "Apollo e Dafne (Bernini)",
    "Caravaggio and Raphael works": "Opere di Caravaggio e Raffaello",
    "Caravaggio and Titian works": "Opere di Caravaggio e Tiziano",
    "Caravaggio Saint John": "San Giovanni di Caravaggio",
    "Boxer at Rest": "Pugile a riposo",
    "Bramante's Tempietto": "Tempietto del Bramante",
    "Capitoline Wolf": "Lupa capitolina",
    "Colossus of Constantine": "Colosso di Costantino",
    "Dying Gaul": "Galata morente",
    "Discus Thrower": "Discobolo",
    "Farnese Hercules": "Ercole Farnese",
    "Frescoed rooms": "Sale affrescate",
    "Imperial rooms": "Sale imperiali",
    "Main facade": "Facciata principale",
    "Main hall": "Sala principale",
    "Main nave": "Navata principale",
    "Main staircase": "Scalinata principale",
    "Main terrace": "Terrazza principale",
    "Map room": "Sala delle mappe",
    "Octagonal courtyard": "Cortile ottagonale",
    "Portrait gallery": "Galleria dei ritratti",
    "Raphael Rooms": "Stanze di Raffaello",
    "Raphael loggias": "Logge di Raffaello",
    "Roman Forum view": "Vista sul Foro Romano",
    "Saint Peter's dome view": "Vista sulla cupola di San Pietro",
    "Spiral ramp": "Rampa a chiocciola",
    "Temple interior": "Interno del tempio",
    "Trevi view from above": "Vista su Fontana di Trevi dall'alto",
    "Vatican corridor": "Corridoio vaticano",
    "Villa gardens": "Giardini della villa",
    "Villa grounds": "Parchi della villa",
    "Villa exterior": "Esterno della villa",
    "Villa interior": "Interno della villa",
}


def translate_description(en: str) -> str:
    """Lightweight EN→IT pass for catalogue blurbs (v1 seed; refine over time)."""
    replacements = [
        ("Museum complex preserving", "Complesso museale che conserva"),
        ("Cathedral church of Rome", "Cattedrale di Roma"),
        ("one of the four papal major basilicas", "una delle quattro basiliche papali maggiori"),
        ("Historic basilica", "Storica basilica"),
        ("One of Rome's major papal basilicas", "Una delle maggiori basiliche papali di Roma"),
        ("Ancient Trastevere basilica", "Antica basilica di Trastevere"),
        ("One of the four major papal basilicas", "Una delle quattro maggiori basiliche papali"),
        ("Art Nouveau-style house museum", "Casa museo in stile Art Nouveau"),
        ("Former imperial mausoleum", "Antico mausoleo imperiale"),
        ("Former power plant", "Ex centrale elettrica"),
        ("Baroque church", "Chiesa barocca"),
        ("Historic church", "Chiesa storica"),
        ("Ancient chariot-racing stadium", "Antico stadio per le corse dei carri"),
        ("Ancient Rome's great amphitheatre", "Il grande anfiteatro dell'antica Roma"),
        ("one of the world's most recognisable monuments", "uno dei monumenti più riconoscibili al mondo"),
        ("Private palace gallery", "Galleria in palazzo privato"),
        ("Major art museum", "Importante museo d'arte"),
        ("Historic Roman palace gallery", "Storica galleria in palazzo romano"),
        ("Municipal museum", "Museo civico"),
        ("Museum beneath the Great Synagogue", "Museo sotto la Grande Sinagoga"),
        ("House museum at the Spanish Steps", "Casa museo scalinata di Trinità dei Monti"),
        ("Interactive museum", "Museo interattivo"),
        ("Contemporary art museum", "Museo d'arte contemporanea"),
        ("Imperial forum markets turned museum", "Mercati imperiali trasformati in museo"),
        ("among the oldest public museum complexes in the world", "tra i più antichi complessi museali pubblici al mondo"),
        ("Museum network inside", "Rete museale all'interno di"),
        ("Museum inside", "Museo all'interno di"),
        ("Museum of Rome's urban history", "Museo della storia urbana di Roma"),
        ("Collection on Napoleon", "Collezione dedicata a Napoleone"),
        ("Renaissance palace housing", "Palazzo rinascimentale che ospita"),
        ("EUR district museum", "Museo del quartiere EUR"),
        ("Key museum for Etruscan civilization", "Museo di riferimento per la civiltà etrusca"),
        ("Italy's national museum dedicated to modern and contemporary art", "Museo nazionale dedicato all'arte moderna e contemporanea"),
        ("Monumental late-imperial bath complex", "Monumentale complesso termale tardo-imperiale"),
        ("Outstanding classical sculpture", "Eccezionale collezione di scultura classica"),
        ("Legendary birthplace of Rome", "Leggendario luogo di fondazione di Roma"),
        ("Baroque palace museum", "Museo in palazzo barocco"),
        ("Baroque palace in Trastevere", "Palazzo barocco a Trastevere"),
        ("Best-preserved ancient Roman temple", "Tempio romano antico meglio conservato"),
        ("Heart of ancient Rome", "Cuore dell'antica Roma"),
        ("Monumental staircase linking", "Monumentale scalinata che collega"),
        ("Principal papal basilica", "Principale basilica papale"),
        ("masterpiece of Renaissance architecture", "capolavoro dell'architettura rinascimentale"),
        ("Vast imperial bath complex", "Vasto complesso termale imperiale"),
        ("Ancient Roman victory column", "Antica colonna di vittoria romana"),
        ("Baroque fountain", "Fontana barocca"),
        ("Rome's most famous wish-making landmark", "la fontana romana più famosa per esprimere un desiderio"),
        ("One of the world's largest museum complexes", "Uno dei più grandi complessi museali al mondo"),
        ("featuring major papal collections", "con le principali collezioni papali"),
        ("Renaissance villa in Trastevere", "Villa rinascimentale a Trastevere"),
        ("Historic Medici villa", "Storica villa medicea"),
        ("seat of the French Academy in Rome", "sede dell'Accademia di Francia a Roma"),
        ("Historic Roman villa complex", "Storico complesso di villa romana"),
        (" daily ", " tutti i giorni "),
        ("closed Mon", "chiuso il lunedì"),
        ("Daily ", "Tutti i giorni "),
        ("; ", "; "),
    ]
    text = en
    for src, dst in replacements:
        text = text.replace(src, dst)
    return polish_it(text)


def translate_hours(en: str) -> str:
    text = en
    replacements = [
        ("Daily", "Tutti i giorni"),
        ("closed Mon", "chiuso il lunedì"),
        ("Mon-Sat", "lun-sab"),
        ("Mon–Sat", "lun–sab"),
        ("Basilica daily", "Basilica tutti i giorni"),
        ("may require tickets", "potrebbero richiedere biglietto"),
        ("Check official site for seasonal hours", "Verifica gli orari stagionali sul sito ufficiale"),
    ]
    for src, dst in replacements:
        text = text.replace(src, dst)
    return polish_it(text)


def translate_highlight(title: str) -> str:
    if title in HIGHLIGHTS_IT:
        return HIGHLIGHTS_IT[title]
    replacements = [
        ("Façade and nave", "Facciata e navata"),
        ("Holy Stairs and baptistery", "Scala Santa e battistero"),
        ("Ara Pacis reliefs", "Rilievi dell'Ara Pacis"),
        ("Richard Meier pavilion", "Padiglione di Richard Meier"),
        ("Highlights", "In evidenza"),
        ("Permanent collection", "Collezione permanente"),
        ("Current exhibitions", "Mostre in corso"),
        ("Arena and hypogeum", "Arena e ipogei"),
        ("Upper tiers view", "Vista dai piani superiori"),
    ]
    for src, dst in replacements:
        if title == src:
            return dst
    return title


def build_overlay(site: dict) -> dict:
    sid = site["id"]
    entry: dict = {}
    name = NAMES_IT.get(sid, site.get("name"))
    if name and name != site.get("name"):
        entry["name"] = name
    elif sid in NAMES_IT:
        entry["name"] = NAMES_IT[sid]

    desc = site.get("shortDescription")
    if desc:
        entry["shortDescription"] = translate_description(desc)

    highlights = []
    for highlight in site.get("highlights", []):
        title = highlight.get("title")
        if title:
            highlights.append({"title": translate_highlight(title)})
    if highlights:
        entry["highlights"] = highlights

    vi = site.get("visitingInfo") or {}
    hours = vi.get("hoursNote")
    if hours:
        entry["visitingInfo"] = {"hoursNote": translate_hours(hours)}

    return entry


def main() -> int:
    lang = sys.argv[1] if len(sys.argv) > 1 else "it"
    if lang != "it":
        print("Only 'it' overlay generation is implemented. Add translations in build_site_content_overlay.py.")
        return 1
    sites = json.loads(BASE.read_text(encoding="utf-8"))
    overlay = {site["id"]: build_overlay(site) for site in sites}

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"site_content_{lang}.json"
    out_path.write_text(json.dumps(overlay, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} ({len(overlay)} sites)")

    if IOS_OUT_DIR.parent.exists():
        IOS_OUT_DIR.mkdir(parents=True, exist_ok=True)
        ios_path = IOS_OUT_DIR / f"site_content_{lang}.json"
        try:
            ios_path.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"Wrote {ios_path}")
        except OSError as error:
            print(f"Skipped iOS copy ({error})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
