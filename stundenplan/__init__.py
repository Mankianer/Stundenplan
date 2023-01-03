from stundenplan.classes import Slot, Stunde, Fach, Stundenplan
import stundenplan.slot_pool as slot_pool
import stundenplan.default_slot_generator
import stundenplan.default_slot_ranking
import stundenplan.default_slot_filter
from stundenplan import stundenplan_builder



def slotmap(keys, value: int = 1):
    """Erstellt ein Dictionary aus einem Generator und einem Wert"""
    slots = {}
    for key in keys:
        slots[key] = value

    return slots


def init_stundenpläne(*klassenstufen: int):
    """Erstellt die Stundenpläne für alle Klassenstufen"""
    return stundenplan_builder.init_stundenpläne(*klassenstufen)


def fill_stundenpläne(stundenpläne: {int: Stundenplan}):
    return stundenplan_builder.fill_stundenpläne(stundenpläne)
