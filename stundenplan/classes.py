import stundenplan.options as options
from tabulate import tabulate


class Wochentag:
    def __init__(self, name, slot_size_map: {int: int}):
        self.name = name
        self.slot_size_map = slot_size_map
        self.max_stunden = max(slot_size_map.keys())


class Stunde:
    def __init__(self, nummer, wochentag: Wochentag, klassenstufe: int):
        self.nummer = nummer
        self.wochentag = wochentag
        self.klassenstufe = klassenstufe

    def __str__(self):
        return self.wochentag.name + ", " + str(self.nummer) + ". Stunde, " + str(self.klassenstufe) + ". Klasse"


class Fach:
    def __init__(self, name, anzahl_stunden: int, min_slot_size: int = options.get_default_min_slot_size()):
        self.name = name
        self.anzahl_stunden = anzahl_stunden
        self.min_slot_size = min_slot_size
        self.muss_zusammen = min_slot_size > 1

    def __str__(self):
        return self.name + " (" + str(self.anzahl_stunden) + " Stunden)" + (
            " (muss zusammen)" if self.muss_zusammen else "")

    def __repr__(self):
        return self.__str__()

    def EMPTY_FACH():
        return Fach(options.get_default_empty_fach_name(), 0, 0)


class Slot:
    def __init__(self, stunde: Stunde, fach: Fach, slot_size: int = options.get_default_slot_length()):
        self.slot_size = slot_size
        self.fach = fach
        self.stunde = stunde

    def __str__(self):
        return f"{self.stunde}-({self.fach}))"

    def __repr__(self):
        return self.__str__()


class Stundenplan:
    def __init__(self, klassenstufe: int, fächer: [Fach], wochentage: [Wochentag]):
        self.klassenstufe = klassenstufe
        self.fächer = fächer
        self.wochentage = wochentage
        self.plan = {Wochentag: {int: Slot}}
        for wochentag in wochentage:
            self.plan[wochentag] = {}
            for stunde in range(1, wochentag.max_stunden + 1):
                self.plan[wochentag][stunde] = Slot(Stunde(stunde, wochentag, klassenstufe), Fach.EMPTY_FACH())

    def get_max_stundenprotag(self):
        return max(wochentag.max_stunden for wochentag in self.wochentage)

    def get_as_table(self):
        # erzeugt 1. Zeile
        stundenplan = {"Stunde": list(range(1, self.get_max_stundenprotag() + 1))}
        # füge die Wochentage als Spalten hinzu
        for wochentag in self.wochentage:
            stundenplan[str(wochentag.name)] = map(lambda slot: slot.fach.name, sorted(self.plan[wochentag].values(),
                                                                                       key=lambda
                                                                                           slot: slot.stunde.nummer))

        return tabulate(stundenplan, headers="keys")
