import stundenplan.slot_pool as slot_pool
from stundenplan.classes import Slot

import stundenplan.options as options


class DefaultFilterOption:
    def __init__(self):
        self.name = "DefaultFilterOption"
        self.description = "Default Filter Option"
        self.slot_ranking_threshold = options.get_slot_ranking_threshold()


@slot_pool.slot_filter_method
def ranking_above_threshold(slot: Slot, option: DefaultFilterOption = DefaultFilterOption()) -> bool:
    """filter out slots with a ranking below the threshold"""

    def test():
        return "test"

    return slot.ranking < option.slot_ranking_threshold
