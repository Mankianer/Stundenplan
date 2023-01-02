from typing import Callable, TypeVar, List

import stundenplan.classes

Slot = TypeVar("Slot", bound=stundenplan.classes.Slot)
Stunde = TypeVar("Stunde", bound=stundenplan.classes.Stunde)
Fach = TypeVar("Fach", bound=stundenplan.classes.Fach)

slot_generator_methods: [Callable[[Stunde, List[Fach]], List[Slot]]] = []
slot_ranking_methods: [Callable[[Slot], int]] = []


def slot_generator_method(func: Callable[[Stunde, List[Fach]], List[Slot]]) -> [Callable[[[Stunde, List[Fach]]], List[Slot]]]:
    """Fügt eine Methode der Liste der Methoden hinzu"""
    slot_generator_methods.append(func)

    print(f"Possible method: {slot_generator_methods}")
    return func

def slot_ranking_method(func: Callable[[Slot], int]) -> [Callable[[Slot], int]]:
    """Fügt eine Methode der Liste der Methoden hinzu
    Die Methode muss eine Zahl zurückgeben, die einen Booster für die Rangfolge des Slots bestimmt"""
    slot_ranking_methods.append(func)
    return func

def get_ranking(slot: Slot) -> int:
    """Ruft alle slot_ranking_methods auf und gibt das Ergebnis als Liste zurück"""
    ranking = sum(method(slot) for method in slot_ranking_methods)
    return ranking

def set_slot_ranking(slots: [Slot]):
    """Setzt den Rang der Slots"""
    for slot in slots:
        slot.ranking = get_ranking(slot)


def get_slots(stunde: Stunde, fächer: List[Fach]) -> [Slot]:
    """Ruft alle slot_generator_methods auf und gibt das Ergebnis als Liste zurück"""
    slots = []
    for method in slot_generator_methods:
        slots.extend(method(stunde, fächer))
    return slots

