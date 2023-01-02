from stundenplan.classes import Slot, Stunde, Fach, Stundenplan
import stundenplan.slot_pool as slot_pool
import stundenplan.default_slot_generator
import stundenplan.default_slot_ranking
import stundenplan.default_slot_filter

stundenpläne: {int: Stundenplan} = {}


def slotmap(keys, value: int = 1):
    """Erstellt ein Dictionary aus einem Generator und einem Wert"""
    slots = {}
    for key in keys:
        slots[key] = value

    return slots


def init_stundenpläne(*klassenstufen: int):
    """Erstellt die Stundenpläne für alle Klassenstufen"""
    stundenpläne.clear()
    for klassenstufe in klassenstufen:
        stundenpläne[klassenstufe] = Stundenplan(klassenstufe, [], [])
    return stundenpläne


def fill_stundenpläne(stundenpläne: {int: Stundenplan} = stundenpläne):
    for stundenplan_ in stundenpläne.values():
        print("#" * 80)
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
                possible_slots = slot_pool.get_slots(stunde, stundenplan_.fächer)

                # ranking der Slots
                slot_pool.set_slot_ranking(possible_slots)
                # filtere Slots
                possible_slots = slot_pool.filter_slots(possible_slots)

                if not possible_slots:
                    stundenplan_.add_slot(Slot(stunde, Fach.not_found_fach()))
                    continue

                # sortiere Slots
                possible_slots = sorted(possible_slots, key=lambda slot: slot.ranking, reverse=True)
                stundenplan_.add_slot(possible_slots[0])
                skip_stunden_count = possible_slots[0].slot_size - 1
