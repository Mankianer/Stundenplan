import stundenplan

# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':

    stundenpläne = stundenplan.init_stundenpläne(5, 6)

    früh_slots = stundenplan.slotmap(list(range(-2, 1)), 1)
    morgen_slots = stundenplan.slotmap(list(range(1, 7)), 1)
    spät_slots = stundenplan.slotmap(list(range(8, 11)), 1)
    slotmap = {**morgen_slots, **spät_slots, **früh_slots}

    for i, stundenplan in stundenpläne.items():
        stundenplan.add_wochentag("Montag", slotmap)
        stundenplan.add_wochentag("Dienstag", slotmap)
        stundenplan.add_wochentag("Mittwoch", morgen_slots)
        stundenplan.add_wochentag("Donnerstag", slotmap)
        stundenplan.add_wochentag("Freitag", slotmap)
        stundenplan.fächer = [stundenplan.classes.Fach("Mathe", 6), stundenplan.classes.Fach("Deutsch", 6)]

    for i, stundenplan in stundenpläne.items():
        print("\n\nStundenplan für Klasse " + str(i))
        print(stundenplan.get_as_table())
