"""Wikimedia-backed hero and highlight images for sites_base_v1.json."""

from __future__ import annotations


def media(hero_url: str, highlights: list[dict]) -> dict:
    return {"images": [hero_url], "highlights": highlights}


def hl(title: str, link: str, image_url: str) -> dict:
    return {"title": title, "url": link, "imageUrl": image_url}


MEDIA: dict[str, dict] = {
    "leonardo_experience_rome": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg/1280px-Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg",
        [
            hl("Machine inventions", "https://www.leonardodavincimuseo.com/en/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg/960px-Leonardo_da_Vinci_-_Vitruvian_Man_-_Google_Art_Project.jpg"),
            hl("Anatomy studies", "https://www.leonardodavincimuseo.com/en/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Leonardo_da_Vinci_-_Study_of_an_old_man.jpg/960px-Leonardo_da_Vinci_-_Study_of_an_old_man.jpg"),
        ],
    ),
    "q10285_colosseum": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg",
        [
            hl("Arena and hypogeum", "https://colosseo.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Colosseum_in_Rome%2C_Italy_-_April_2007.jpg/640px-Colosseum_in_Rome%2C_Italy_-_April_2007.jpg"),
            hl("Upper tiers and views", "https://colosseo.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg"),
        ],
    ),
    "q1053970_centrale_montemartini": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Le_mus%C3%A9e_de_la_centrale_Montemartini_(Rome)_(33828659930).jpg/1280px-Le_mus%C3%A9e_de_la_centrale_Montemartini_(Rome)_(33828659930).jpg",
        [
            hl("Sculpture in turbine hall", "https://museonazionaleromano.beniculturali.it/en/centrale-montemartini/", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Le_mus%C3%A9e_de_la_centrale_Montemartini_(Rome)_(33828659930).jpg/1280px-Le_mus%C3%A9e_de_la_centrale_Montemartini_(Rome)_(33828659930).jpg"),
            hl("Mosaic and portrait rooms", "https://museonazionaleromano.beniculturali.it/en/centrale-montemartini/", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Centrale_Montemartini_-_Museo_(3).jpg/960px-Centrale_Montemartini_-_Museo_(3).jpg"),
        ],
    ),
    "q1074320_museum_roman_civilization": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Museo_della_Civilt%C3%A0_Romana.jpg/1280px-Museo_della_Civilt%C3%A0_Romana.jpg",
        [
            hl("Plastico di Roma Imperiale", "https://www.museociviltaromana.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Museo_della_Civilt%C3%A0_Romana.jpg/1280px-Museo_della_Civilt%C3%A0_Romana.jpg"),
            hl("Daily life collections", "https://www.museociviltaromana.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Plastico_di_Roma_Imperiale.jpg/960px-Plastico_di_Roma_Imperiale.jpg"),
        ],
    ),
    "q1094986_palazzo_altemps": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Roma_2011_08_07_Palazzo_Altemps.jpg/1280px-Roma_2011_08_07_Palazzo_Altemps.jpg",
        [
            hl("Ludovisi Battle sarcophagus", "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Ludovisi_Battle_sarcophagus_(Altemps).jpg/960px-Ludovisi_Battle_sarcophagus_(Altemps).jpg"),
            hl("Renaissance courtyard", "https://museonazionaleromano.beniculturali.it/en/palazzo-altemps/", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Roma_2011_08_07_Palazzo_Altemps.jpg/960px-Roma_2011_08_07_Palazzo_Altemps.jpg"),
        ],
    ),
    "q1094987_palazzo_massimo": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Roma09_flickr.jpg/1280px-Roma09_flickr.jpg",
        [
            hl("Boxer at Rest", "https://museonazionaleromano.beniculturali.it/en/palazzo-massimo/", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Roma09_flickr.jpg/1280px-Roma09_flickr.jpg"),
            hl("Garden Villa frescoes", "https://museonazionaleromano.beniculturali.it/en/palazzo-massimo/", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Boxer_at_Rest_-_Palazzo_Massimo.jpg/960px-Boxer_at_Rest_-_Palazzo_Massimo.jpg"),
        ],
    ),
    "q1126723_villa_farnesina": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/La_villa_Farnesina_(Rome)_(34029492720).jpg/1280px-La_villa_Farnesina_(Rome)_(34029492720).jpg",
        [
            hl("Loggia of Psyche", "http://www.villafarnesina.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Galatea_(Raphael)_Villa_Farnesina.jpg/960px-Galatea_(Raphael)_Villa_Farnesina.jpg"),
            hl("Raphael frescoes", "http://www.villafarnesina.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/La_villa_Farnesina_(Rome)_(34029492720).jpg/960px-La_villa_Farnesina_(Rome)_(34029492720).jpg"),
        ],
    ),
    "q112972_spanish_steps": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Piazza_di_Spagna_(Rome)_0004.jpg/1280px-Piazza_di_Spagna_(Rome)_0004.jpg",
        [
            hl("Piazza di Spagna", "https://en.wikipedia.org/wiki/Spanish_Steps", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Piazza_di_Spagna_(Rome)_0004.jpg/1280px-Piazza_di_Spagna_(Rome)_0004.jpg"),
            hl("Trinit\u00e0 dei Monti church", "https://www.trinitamonti.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Trinita_dei_Monti_-_Rome.jpg/960px-Trinita_dei_Monti_-_Rome.jpg"),
        ],
    ),
    "q1136614_palazzo_barberini": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Palazzo_Barberini_-_esterno.jpg/1280px-Palazzo_Barberini_-_esterno.jpg",
        [
            hl("Pietro da Cortona ceiling", "http://www.barberinicorsini.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Palazzo_Barberini_-_Il_trionfo_della_Divina_Provvidenza.jpg/960px-Palazzo_Barberini_-_Il_trionfo_della_Divina_Provvidenza.jpg"),
            hl("Caravaggio and Raphael works", "http://www.barberinicorsini.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Palazzo_Barberini_-_esterno.jpg/960px-Palazzo_Barberini_-_esterno.jpg"),
        ],
    ),
    "q1136615_palazzo_corsini": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Palazzo_Corsini_%28Rome%29.jpg/1280px-Palazzo_Corsini_%28Rome%29.jpg",
        [
            hl("Caravaggio Saint John", "https://www.barberinicorsini.org/en/palazzo-corsini/", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Palazzo_Corsini_%28Rome%29.jpg/1280px-Palazzo_Corsini_%28Rome%29.jpg"),
            hl("Botanical garden access", "https://www.barberinicorsini.org/en/palazzo-corsini/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Caravaggio_-_San_Giovanni_Battista_-_Palazzo_Corsini.jpg/960px-Caravaggio_-_San_Giovanni_Battista_-_Palazzo_Corsini.jpg"),
        ],
    ),
    "q1137391_santa_maria_trastevere": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/01_Santa_Maria_in_Trastevere_Facade.jpg/1280px-01_Santa_Maria_in_Trastevere_Facade.jpg",
        [
            hl("Apse mosaics", "https://www.santamariaintrastevere.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/01_Santa_Maria_in_Trastevere_Facade.jpg/960px-01_Santa_Maria_in_Trastevere_Facade.jpg"),
            hl("Piazza fountain", "https://www.santamariaintrastevere.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Piazza_di_Santa_Maria_in_Trastevere.jpg/960px-Piazza_di_Santa_Maria_in_Trastevere.jpg"),
        ],
    ),
    "q1192577_santagnese_in_agone": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Fa%C3%A7ade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg/1280px-Fa%C3%A7ade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg",
        [
            hl("Borromini fa\u00e7ade", "https://www.santagneseinagone.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Fa%C3%A7ade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg/960px-Fa%C3%A7ade_of_Sant'Agnese_in_Agone,_Rome,_Italy.jpg"),
            hl("Dome frescoes", "https://www.santagneseinagone.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Sant'Agnese_in_Agone_(Rome)_esterno.jpg/960px-Sant'Agnese_in_Agone_(Rome)_esterno.jpg"),
        ],
    ),
    "q12501_st_peters_basilica": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg/1280px-Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg",
        [
            hl("Michelangelo's Piet\u00e0", "https://www.vatican.va/content/vatican/en.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg/1280px-Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg"),
            hl("Dome climb", "https://www.vatican.va/content/vatican/en.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Pieta_de_Michelangelo.jpg/960px-Pieta_de_Michelangelo.jpg"),
        ],
    ),
    "q1258576_san_pietro_in_montorio": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/San_Pietro_in_Montorio_-_esterno.jpg/1280px-San_Pietro_in_Montorio_-_esterno.jpg",
        [
            hl("Bramante's Tempietto", "http://www.sanpietroinmontorio.it/home.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Tempietto_del_Bramante_(2).jpg/960px-Tempietto_del_Bramante_(2).jpg"),
            hl("Janiculum views", "http://www.sanpietroinmontorio.it/home.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/San_Pietro_in_Montorio_-_esterno.jpg/960px-San_Pietro_in_Montorio_-_esterno.jpg"),
        ],
    ),
    "q1283630_keats_shelley_house": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Keats-Shelley_House.jpg/1280px-Keats-Shelley_House.jpg",
        [
            hl("Keats's room", "https://ksh.roma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Keats-Shelley_House.jpg/1280px-Keats-Shelley_House.jpg"),
            hl("Romantic poets library", "https://ksh.roma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Keats-Shelley_House_Interior.jpg/960px-Keats-Shelley_House_Interior.jpg"),
        ],
    ),
    "q1356135_macro_rome": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Macro_Rome.jpg/1280px-Macro_Rome.jpg",
        [
            hl("Temporary exhibitions", "https://www.macro.roma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Macro_Rome.jpg/1280px-Macro_Rome.jpg"),
            hl("Permanent collection", "https://www.macro.roma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Macro_Testaccio_Rome.jpg/960px-Macro_Testaccio_Rome.jpg"),
        ],
    ),
    "q1362663_villa_medici": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Villa_Medici_Roma_01.jpg/1280px-Villa_Medici_Roma_01.jpg",
        [
            hl("French Academy gardens", "http://www.villamedici.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Villa_Medici_Roma_01.jpg/960px-Villa_Medici_Roma_01.jpg"),
            hl("Guided palace tours", "http://www.villamedici.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Villa_Medici_-_Rome.jpg/960px-Villa_Medici_-_Rome.jpg"),
        ],
    ),
    "q1465674_santignazio_church": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Church_of_Sant'Ignazio_di_Loyola.jpg/1280px-Church_of_Sant'Ignazio_di_Loyola.jpg",
        [
            hl("Andrea Pozzo ceiling fresco", "http://santignazio.gesuiti.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Church_of_Sant'Ignazio_di_Loyola.jpg/960px-Church_of_Sant'Ignazio_di_Loyola.jpg"),
            hl("Illusionistic dome", "http://santignazio.gesuiti.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Sant'Ignazio_di_Loyola_(Roma)_-_Volta_affrescata_da_Andrea_Pozzo.jpg/960px-Sant'Ignazio_di_Loyola_(Roma)_-_Volta_affrescata_da_Andrea_Pozzo.jpg"),
        ],
    ),
    "q1492387_gnamc": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg/1280px-Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg",
        [
            hl("19th\u201321st century masterpieces", "https://gnamc.cultura.gov.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg/960px-Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg"),
            hl("De Chirico and Morandi rooms", "https://gnamc.cultura.gov.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg/960px-Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg"),
        ],
    ),
    "q15055388_villa_giulia_etruscan": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Villa_Giulia_modified.jpg/1280px-Villa_Giulia_modified.jpg",
        [
            hl("Sarcophagus of the Spouses", "https://www.museoetru.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Sarcophagus_of_the_Spouses_-_National_Etruscan_Museum.jpg/960px-Sarcophagus_of_the_Spouses_-_National_Etruscan_Museum.jpg"),
            hl("Villa Giulia gardens", "https://www.museoetru.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Villa_Giulia_modified.jpg/960px-Villa_Giulia_modified.jpg"),
        ],
    ),
    "q1741_trevi_fountain": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/1280px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg",
        [
            hl("Oceanus fa\u00e7ade", "https://en.wikipedia.org/wiki/Trevi_Fountain", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/1280px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg"),
            hl("Evening illumination", "https://en.wikipedia.org/wiki/Trevi_Fountain", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Trevi_Fountain_at_night.jpg/960px-Trevi_Fountain_at_night.jpg"),
        ],
    ),
    "q17636813_musei_villa_torlonia": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Casino_Nobile_-_Villa_Torlonia.jpg/1280px-Casino_Nobile_-_Villa_Torlonia.jpg",
        [
            hl("Casino Nobile", "http://www.museivillatorlonia.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Casino_Nobile_-_Villa_Torlonia.jpg/960px-Casino_Nobile_-_Villa_Torlonia.jpg"),
            hl("Casina delle Civette", "http://www.museivillatorlonia.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Casina_delle_Civette.jpg/960px-Casina_delle_Civette.jpg"),
        ],
    ),
    "q180540_roman_forum": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Foro_Romano_-_panoramio.jpg/1280px-Foro_Romano_-_panoramio.jpg",
        [
            hl("Via Sacra and temples", "https://colosseo.it/en/area/foro-romano/", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Foro_Romano_-_panoramio.jpg/1280px-Foro_Romano_-_panoramio.jpg"),
            hl("House of the Vestals", "https://colosseo.it/en/area/foro-romano/", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Tempio_di_Vesta_(Foro_Romano).jpg/960px-Tempio_di_Vesta_(Foro_Romano).jpg"),
        ],
    ),
    "q182955_vatican_museums": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Vatican_Museums_Spiral_Staircase_2012.jpg/1280px-Vatican_Museums_Spiral_Staircase_2012.jpg",
        [
            hl("Sistine Chapel ceiling", "https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/cappella-sistina.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_(cropped).jpg/960px-Michelangelo_-_Creation_of_Adam_(cropped).jpg"),
            hl("Gallery of Maps", "https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/galleria-delle-carte-geografiche.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Vatican_Museums_-_Gallery_of_Maps_-_Sala_bella.jpg/960px-Vatican_Museums_-_Gallery_of_Maps_-_Sala_bella.jpg"),
        ],
    ),
    "q186282_santa_maria_maggiore": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg/1280px-Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg",
        [
            hl("5th-century mosaics", "https://www.basilicasantamariamaggiore.va/it.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg/960px-Basilica_di_Santa_Maria_Maggiore_-_Roma.jpg"),
            hl("Bernini's tomb", "https://www.basilicasantamariamaggiore.va/it.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Roma_Santa_Maria_Maggiore_BW_1.jpg/960px-Roma_Santa_Maria_Maggiore_BW_1.jpg"),
        ],
    ),
    "q192784_trajans_column": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Trajan's_Column_HD.jpg/1280px-Trajan's_Column_HD.jpg",
        [
            hl("Spiral relief frieze", "https://en.wikipedia.org/wiki/Trajan%27s_Column", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Trajan's_Column_HD.jpg/960px-Trajan's_Column_HD.jpg"),
            hl("Forum of Trajan setting", "https://www.mercatiditraiano.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Mercati_di_Traiano_-_Roma.jpg/960px-Mercati_di_Traiano_-_Roma.jpg"),
        ],
    ),
    "q1971299_galleria_colonna": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG/1280px-Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG",
        [
            hl("Great Hall", "http://www.galleriacolonna.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Galleria_Colonna,_Rome.jpg/960px-Galleria_Colonna,_Rome.jpg"),
            hl("Palace apartments", "http://www.galleriacolonna.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG/960px-Trevi_-_palazzo_colonna_e_basilica_santi_apostoli_01.JPG"),
        ],
    ),
    "q207808_circus_maximus": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/CircusMaximusSO.jpg/1280px-CircusMaximusSO.jpg",
        [
            hl("Track and spina ruins", "https://en.wikipedia.org/wiki/Circus_Maximus", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/CircusMaximusSO.jpg/1280px-CircusMaximusSO.jpg"),
            hl("Palatine Hill backdrop", "https://en.wikipedia.org/wiki/Circus_Maximus", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Circus_Maximus_from_Palatine.jpg/960px-Circus_Maximus_from_Palatine.jpg"),
        ],
    ),
    "q2301489_doria_pamphilj_gallery": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Palazzo_Doria_Pamphilj.jpg/1280px-Palazzo_Doria_Pamphilj.jpg",
        [
            hl("Vel\u00e1zquez papal portrait", "https://www.doriapamphilj.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Palazzo_Doria_Pamphilj.jpg/1280px-Palazzo_Doria_Pamphilj.jpg"),
            hl("Gallery of Mirrors", "https://www.doriapamphilj.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Vel%C3%A1zquez,_Diego_-_Portrait_of_Pope_Innocent_X_-_Google_Art_Project.jpg/960px-Vel%C3%A1zquez,_Diego_-_Portrait_of_Pope_Innocent_X_-_Google_Art_Project.jpg"),
        ],
    ),
    "q231699_san_paolo_fuori_le_mura": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/StPaul.jpg/1280px-StPaul.jpg",
        [
            hl("Basilica nave and apse", "http://www.vatican.va/various/basiliche/san_paolo/index_en.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/StPaul.jpg/960px-StPaul.jpg"),
            hl("Cloister and mosaics", "http://www.vatican.va/various/basiliche/san_paolo/index_en.html", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Saint_Paul_Outside_the_Walls_-_Cloister.jpg/960px-Saint_Paul_Outside_the_Walls_-_Cloister.jpg"),
        ],
    ),
    "q2586829_palatine_hill": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Foro_Romano_-_panoramio.jpg/1280px-Foro_Romano_-_panoramio.jpg",
        [
            hl("Domus Augustana ruins", "https://colosseo.it/en/area/palatino/", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Foro_Romano_-_panoramio.jpg/1280px-Foro_Romano_-_panoramio.jpg"),
            hl("Views over Circus Maximus", "https://colosseo.it/en/area/palatino/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Palatine_Hill_Rome.jpg/960px-Palatine_Hill_Rome.jpg"),
        ],
    ),
    "q318660_santa_maria_aracoeli": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg/1280px-Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg",
        [
            hl("Medieval cosmatesque floor", "https://en.wikipedia.org/wiki/Santa_Maria_in_Aracoeli", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg/960px-Santa_Maria_in_Aracoeli_(Rome)_-_Facade.jpg"),
            hl("Capitoline staircase", "https://en.wikipedia.org/wiki/Santa_Maria_in_Aracoeli", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Santa_Maria_in_Aracoeli_Interno.jpg/960px-Santa_Maria_in_Aracoeli_Interno.jpg"),
        ],
    ),
    "q333906_capitoline_museums": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/0_Cordonata_-_Dioscuri_-_Palazzo_Senatorio.JPG/1280px-0_Cordonata_-_Dioscuri_-_Palazzo_Senatorio.JPG",
        [
            hl("Capitoline Wolf", "https://museicapitolini.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Capitoline_she-wolf_Musei_Capitolini_MC1181.jpg/960px-Capitoline_she-wolf_Musei_Capitolini_MC1181.jpg"),
            hl("Colossus of Constantine", "https://museicapitolini.org/", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Statua_colossale_di_Costantino_I.jpg/960px-Statua_colossale_di_Costantino_I.jpg"),
        ],
    ),
    "q3757712_galleria_arte_moderna_roma": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg/1280px-Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg",
        [
            hl("19th-century Roman art", "http://www.galleriaartemodernaroma.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg/960px-Galleria_d'arte_moderna_di_roma_capitale,_esterno_01.jpg"),
            hl("Temporary exhibitions", "http://www.galleriaartemodernaroma.it", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg/960px-Galleria_nazionale_d'arte_moderna_-_Rome,_Italy_-_DSC05142.jpg"),
        ],
    ),
    "q3757713_galleria_spada": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/938RomaPalazzoSpada.JPG/1280px-938RomaPalazzoSpada.JPG",
        [
            hl("Borromini perspective gallery", "https://www.barberinicorsini.org/en/galleria-spada/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/938RomaPalazzoSpada.JPG/1280px-938RomaPalazzoSpada.JPG"),
            hl("Caravaggio and Titian works", "https://www.barberinicorsini.org/en/galleria-spada/", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Galleria_Spada_perspective_colonnade.jpg/960px-Galleria_Spada_perspective_colonnade.jpg"),
        ],
    ),
    "q3867587_museo_carlo_bilotti": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Roma-museoBilotti01.jpg/1280px-Roma-museoBilotti01.jpg",
        [
            hl("Carlo Bilotti collection", "http://www.museocarlobilotti.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Roma-museoBilotti01.jpg/960px-Roma-museoBilotti01.jpg"),
            hl("Orangery exhibitions", "http://www.museocarlobilotti.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Roma-museoBilotti02.jpg/960px-Roma-museoBilotti02.jpg"),
        ],
    ),
    "q3867590_casina_delle_civette": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Casina_delle_Civette.jpg/1280px-Casina_delle_Civette.jpg",
        [
            hl("Stained-glass rooms", "http://www.museivillatorlonia.it/casina_delle_civette", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Casina_delle_Civette.jpg/960px-Casina_delle_Civette.jpg"),
            hl("Art Nouveau interiors", "http://www.museivillatorlonia.it/casina_delle_civette", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Casina_delle_Civette_-_vetrata.jpg/960px-Casina_delle_Civette_-_vetrata.jpg"),
        ],
    ),
    "q3868175_museo_roma_palazzo_braschi": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg/1280px-Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg",
        [
            hl("Rome city history", "http://www.museodiroma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg/960px-Palais_Braschi_-_Rome_(IT62)_-_2021-08-29_-_3.jpg"),
            hl("Views over Piazza Navona", "http://www.museodiroma.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Piazza_Navona_from_Palazzo_Braschi.jpg/960px-Piazza_Navona_from_Palazzo_Braschi.jpg"),
        ],
    ),
    "q3868176_museo_napoleonico": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Museo_Napoleonico.jpg/1280px-Museo_Napoleonico.jpg",
        [
            hl("Bonaparte family portraits", "https://www.museonapoleonico.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Museo_Napoleonico.jpg/1280px-Museo_Napoleonico.jpg"),
            hl("Period furnishings", "https://www.museonapoleonico.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Museo_Napoleonico_-_interno.jpg/960px-Museo_Napoleonico_-_interno.jpg"),
        ],
    ),
    "q3868408_maxxi": media(
        "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/MAXXI_%2827483747665%29.jpg/1280px-MAXXI_%2827483747665%29.jpg",
        [
            hl("Permanent collections", "https://www.maxxi.art/", "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/MAXXI_%2827483747665%29.jpg/1280px-MAXXI_%2827483747665%29.jpg"),
            hl("Architecture gallery", "https://www.maxxi.art/", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/MAXXI_Roma_2010.jpg/960px-MAXXI_Roma_2010.jpg"),
        ],
    ),
    "q474857_villa_torlonia_rome": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Villa_Torlonia_01304.JPG/1280px-Villa_Torlonia_01304.JPG",
        [
            hl("Historic park", "http://www.museivillatorlonia.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Villa_Torlonia_01304.JPG/960px-Villa_Torlonia_01304.JPG"),
            hl("Casino Nobile exterior", "http://www.museivillatorlonia.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Casino_Nobile_-_Villa_Torlonia.jpg/960px-Casino_Nobile_-_Villa_Torlonia.jpg"),
        ],
    ),
    "q478642_mercati_traiano": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg/1280px-Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg",
        [
            hl("Great Hall and brick vaults", "https://www.mercatiditraiano.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg/1280px-Mercati_di_Traiano_e_foro_di_Traiano%2C_Roma.jpg"),
            hl("Forum of Trajan views", "https://www.mercatiditraiano.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Mercati_di_Traiano_-_interno.jpg/960px-Mercati_di_Traiano_-_interno.jpg"),
        ],
    ),
    "q486382_castel_santangelo": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Castel_Sant'Angelo_at_Night.jpg/1280px-Castel_Sant'Angelo_at_Night.jpg",
        [
            hl("Ramparts and terraces", "https://castelsantangelo.beniculturali.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Castel_Sant'Angelo_at_Night.jpg/960px-Castel_Sant'Angelo_at_Night.jpg"),
            hl("Papal apartments", "https://castelsantangelo.beniculturali.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Castel_Sant'Angelo_-_Rome.jpg/960px-Castel_Sant'Angelo_-_Rome.jpg"),
        ],
    ),
    "q502098_terme_di_caracalla": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Baths_of_Caracalla,_facing_Caldarium.jpg/1280px-Baths_of_Caracalla,_facing_Caldarium.jpg",
        [
            hl("Monumental halls", "https://colosseo.it/en/area/terme-di-caracalla/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Baths_of_Caracalla,_facing_Caldarium.jpg/960px-Baths_of_Caracalla,_facing_Caldarium.jpg"),
            hl("Summer opera season", "https://colosseo.it/en/area/terme-di-caracalla/", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Baths_of_Caracalla_mosaic.jpg/960px-Baths_of_Caracalla_mosaic.jpg"),
        ],
    ),
    "q623612_ara_pacis_museum": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Ara_Pacis_(SW).jpg/1280px-Ara_Pacis_(SW).jpg",
        [
            hl("Ara Pacis reliefs", "https://www.arapacis.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Ara_Pacis_(SW).jpg/960px-Ara_Pacis_(SW).jpg"),
            hl("Richard Meier pavilion", "https://www.arapacis.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Museo_dell'Ara_Pacis_-_esterno.jpg/960px-Museo_dell'Ara_Pacis_-_esterno.jpg"),
        ],
    ),
    "q724816_jewish_museum_rome": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Great_Synagogue_of_Rome.jpg/1280px-Great_Synagogue_of_Rome.jpg",
        [
            hl("Synagogue and museum tour", "https://www.museoebraico.roma.it/en/", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Great_Synagogue_of_Rome.jpg/1280px-Great_Synagogue_of_Rome.jpg"),
            hl("Jewish Ghetto context", "https://www.museoebraico.roma.it/en/", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Portico_d'Ottavia_-_Rome.jpg/960px-Portico_d'Ottavia_-_Rome.jpg"),
        ],
    ),
    "q836108_baths_of_diocletian": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Baths_of_Diocletian-Antmoose1.jpg/1280px-Baths_of_Diocletian-Antmoose1.jpg",
        [
            hl("Great hall of baths", "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Baths_of_Diocletian-Antmoose1.jpg/960px-Baths_of_Diocletian-Antmoose1.jpg"),
            hl("Garden cloister", "https://museonazionaleromano.beniculturali.it/en/terme-di-diocleziano/", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Michelangelo_Cloister_-_Museum_of_Roman_Civilization.jpg/960px-Michelangelo_Cloister_-_Museum_of_Roman_Civilization.jpg"),
        ],
    ),
    "q84090_san_giovanni_laterano": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/San_Giovanni_in_Laterano_2021.jpg/1280px-San_Giovanni_in_Laterano_2021.jpg",
        [
            hl("Fa\u00e7ade and nave", "https://www.basilicasangiovanni.va/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/San_Giovanni_in_Laterano_2021.jpg/960px-San_Giovanni_in_Laterano_2021.jpg"),
            hl("Holy Stairs and baptistery", "https://www.basilicasangiovanni.va/", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Rom,_die_Heilige_Treppe.JPG/960px-Rom,_die_Heilige_Treppe.JPG"),
        ],
    ),
    "q841506_galleria_borghese": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Roma_Museo_Borghese.jpg/1280px-Roma_Museo_Borghese.jpg",
        [
            hl("Apollo and Daphne (Bernini)", "https://galleriaborghese.beniculturali.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Apollo_and_Daphne_by_Bernini_(Galleria_Borghese).jpg/960px-Apollo_and_Daphne_by_Bernini_(Galleria_Borghese).jpg"),
            hl("The Rape of Proserpina (Bernini)", "https://galleriaborghese.beniculturali.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Rape_of_Prosepina_September_2015-3a.jpg/960px-Rape_of_Prosepina_September_2015-3a.jpg"),
            hl("David with the Head of Goliath (Caravaggio)", "https://galleriaborghese.beniculturali.it/", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/David_with_the_Head_of_Goliath-Caravaggio_%281610%29.jpg/960px-David_with_the_Head_of_Goliath-Caravaggio_%281610%29.jpg"),
        ],
    ),
    "q99309_pantheon": media(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pantheon_Rom_1_cropped.jpg/1280px-Pantheon_Rom_1_cropped.jpg",
        [
            hl("Dome and oculus", "https://www.pantheonroma.com/", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pantheon_Rom_1_cropped.jpg/1280px-Pantheon_Rom_1_cropped.jpg"),
            hl("Raphael's tomb", "https://www.pantheonroma.com/", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Pantheon_Interior.jpg/960px-Pantheon_Interior.jpg"),
        ],
    ),
}

assert len(MEDIA) == 50, f"MEDIA must cover 50 sites, got {len(MEDIA)}"
