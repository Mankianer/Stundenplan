import stundenplan.slot_pool as slot_pool
from stundenplan.classes import Slot

import stundenplan.options as options


@slot_pool.slot_ranking_method
def fit_perfect(slot: Slot, stundenplan) -> int:
    """Bonus für einen Slot, der perfekt passt"""
    if slot.fach.anzahl_stunden == slot.slot_size:
        return options.get_slot_ranking_fit_perfect()
    return 0
