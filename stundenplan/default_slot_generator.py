import stundenplan.slot_pool as slot_pool
from stundenplan.classes import Slot, Stunde, Fach


@slot_pool.slot_generator_method
def default_slot_generator(stunde: Stunde, fächer: [Fach]) -> Slot:
    """Generiert einen Slot mit den Standardwerten"""
    slots = []
    for fach in fächer:
        if fach.anzahl_stunden > 0:
            slot_size = min(stunde.max_slot_size, fach.anzahl_stunden)
            slots.append(Slot(stunde, fach, slot_size))

    return slots
