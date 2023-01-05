import stundenplan.slot_pool as slot_pool
from stundenplan import Stundenplan, Fach, Slot


def init_stundenpläne(*klassenstufen: any) -> {any: Stundenplan}:
    """Erstellt die Stundenpläne für alle Klassenstufen"""
    stundenpläne: {any: Stundenplan} = {}
    for klassenstufe in klassenstufen:
        stundenpläne[klassenstufe] = Stundenplan(klassenstufe, [], [])
    return stundenpläne


def fill_stundenpläne(stundenpläne: {any: Stundenplan}):
    for stundenplan_ in stundenpläne.values():
        print("#" * 80, " Klassenstufe: ", stundenplan_.klassenstufe)
        for wochentag in stundenplan_.wochentage:
            skip_stunden_count = 0
            for stunde_nr in wochentag.get_stunden():
                stunde = stundenplan_.plan[wochentag.name][stunde_nr].stunde
                print(stunde)
                if skip_stunden_count > 0:
                    skip_stunden_count -= 1
                    continue
                # print(stundenplan_.get_as_table())
                # hole mögliche Slots
                possible_slots = slot_pool.get_slots(stunde, stundenplan_.fächer, stundenplan_)

                # ranking der Slots
                slot_pool.set_slot_ranking(possible_slots, stundenplan_)
                # filtere Slots
                possible_slots = slot_pool.filter_slots(possible_slots, stundenplan_)

                if not possible_slots:
                    stundenplan_.add_slot(
                        Slot(stunde, Fach.not_found_fach(stundenplan_.options.get_default_not_found_fach_name())))
                    continue

                # sortiere Slots
                possible_slots = sorted(possible_slots, key=lambda slot: slot.ranking, reverse=True)
                stundenplan_.add_slot(possible_slots[0])
                skip_stunden_count = possible_slots[0].slot_size - 1
