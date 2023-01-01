import stundenplan.classes

stundenpläne = {}


def slotmap(keys, value: int = 1):
    """Erstellt ein Dictionary aus einem Generator und einem Wert"""
    slots = {}
    for key in keys:
        slots[key] = value

    return slots


def init_stundenpläne(*klassenstufen: int):
    """Erstellt die Stundenpläne für alle Klassenstufen"""
    stundenpläne: {int: stundenplan.classes.Stundenplan} = {}
    for klassenstufe in klassenstufen:
        stundenpläne[klassenstufe] = stundenplan.classes.Stundenplan(klassenstufe)
    return stundenpläne
