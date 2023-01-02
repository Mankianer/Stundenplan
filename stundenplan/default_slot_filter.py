import stundenplan.slot_pool as slot_pool
from stundenplan.classes import Slot

import stundenplan.options as options


@slot_pool.slot_filter_method
def ranking_above_threadhold(slot: Slot) -> bool:
    """filter out slots with a ranking below the threshold"""
    return slot.ranking < options.get_slot_ranking_threadhold()
