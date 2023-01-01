import stundenplan.options as options
from tabulate import tabulate


class Wochentag:
    """
    Repräsentiert einen Wochentag und die Stunden mit der bevorzugten Slotgröße.
    """

    def __init__(self, name, slot_size_map: {int: int}):
        self.name = name
        self.slot_size_map: {int: int} = slot_size_map
        self.latest_stunden = max(slot_size_map.keys())
        self.earliest_stunden = min(slot_size_map.keys())


class Stunde:
    """
    Repräsentiert eine Stunde, die die Position im Stundenplan(nummer, tag, stufe)
    """

    def __init__(self, nummer, wochentag: Wochentag, klassenstufe: int):
        self.nummer = nummer
        self.wochentag = wochentag
        self.klassenstufe = klassenstufe

    def __str__(self):
        return self.wochentag.name + ", " + str(self.nummer) + ". Stunde, " + str(self.klassenstufe) + ". Klasse"


class Fach:
    """
    Repräsentiert ein Fach mit seinen Bedingungen zur Belegung eines Slots im Stundenplan
    """

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

    @classmethod
    def empty_fach(cls):
        """Repräsentiert eine noch nicht belegte Stunde"""
        return cls(options.get_default_empty_fach_name(), 0, 0)

    @classmethod
    def not_include_fach(cls):
        """Repräsentiert eine Stunde, die nicht belegt werden soll"""
        return cls(options.get_default_not_include_fach_name(), 0, 0)


class Slot:
    """
    Repräsentiert einen Slot im Stundenplan, der eine Stunde und ein Fach beinhaltet.
    So wie eine Bevorzugte/Maximale Slotgröße.
    """

    def __init__(self, stunde: Stunde, fach: Fach):
        self.fach = fach
        self.stunde = stunde
        self.max_slot_size = stunde.wochentag.slot_size_map[
            stunde.nummer] if stunde.nummer in stunde.wochentag.slot_size_map else 1

    def __str__(self):
        return f"{self.stunde}-({self.fach}))"

    def __repr__(self):
        return self.__str__()


class Stundenplan:
    """
    Repräsentiert einen Stundenplan pro Klassenstufe.
    Und beinhalet die Fächer, die Wochentage und die Slots.
    """
    def __init__(self, klassenstufe: int, fächer: [Fach], wochentage: [Wochentag]):
        self.klassenstufe = klassenstufe
        self.fächer = fächer
        self.wochentage = wochentage
        self.plan = {Wochentag: {int: Slot}}
        # erstelle leeren Stundenplan
        for wochentag in wochentage:
            self.plan[wochentag] = {}
            for stunde in range(self.get_earliest_stunden(), self.get_latest_stunden() + 1):
                if stunde in wochentag.slot_size_map.keys():
                    self.plan[wochentag][stunde] = Slot(Stunde(stunde, wochentag, klassenstufe), Fach.empty_fach())
                else:
                    self.plan[wochentag][stunde] = Slot(Stunde(stunde, wochentag, klassenstufe),
                                                        Fach.not_include_fach())

    def get_latest_stunden(self):
        return max(wochentag.latest_stunden for wochentag in self.wochentage)

    def get_earliest_stunden(self):
        return min(wochentag.earliest_stunden for wochentag in self.wochentage)

    def get_as_table(self):
        # erzeugt 1. Zeile
        stundenplan = {"Stunde": list(range(self.get_earliest_stunden(), self.get_latest_stunden() + 1))}
        # füge die Wochentage als Spalten hinzu
        for wochentag in self.wochentage:
            stundenplan[wochentag.name] = map(lambda slot: slot.fach.name, sorted(self.plan[wochentag].values(),
                                                                                  key=lambda
                                                                                      slot: slot.stunde.nummer))

        return tabulate(stundenplan, headers="keys")
