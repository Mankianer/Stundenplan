import stundenplan.slot_pool as slot_pool
from stundenplan.classes import Slot



class DefaultRankingOption:
    def __init__(self):
        self.name = "DefaultRankingOption"
        self.description = "Default Ranking Option"
        self.get_slot_ranking_fit_perfect = 20


@slot_pool.slot_ranking_method
def fit_perfect(slot: Slot, stundenplan_, option: DefaultRankingOption = DefaultRankingOption()) -> int:
    """Bonus für einen Slot, der perfekt passt"""
    if slot.fach.anzahl_stunden == slot.slot_size:
        return option.get_slot_ranking_fit_perfect
    return 0
