from typing import Callable, TypeVar, List

import stundenplan.classes

Slot = TypeVar("Slot", bound=stundenplan.classes.Slot)
Stunde = TypeVar("Stunde", bound=stundenplan.classes.Stunde)
Fach = TypeVar("Fach", bound=stundenplan.classes.Fach)

slot_generator_methods: [Callable[[Stunde, List[Fach]], List[Slot]]] = []


def slot_generator_method(func: Callable[[Stunde, List[Fach]], List[Slot]]) -> [Callable[[[Stunde, List[Fach]]], List[Slot]]]:
    """Fügt eine Methode der Liste der Methoden hinzu"""
    slot_generator_methods.append(func)

    print(f"Possible method: {slot_generator_methods}")
    return func


def call_slot_generator_methods(stunde: Stunde, fächer: List[Fach]) -> [List[Slot]]:
    """Ruft alle slot_generator_methods auf und gibt das Ergebnis als Liste zurück"""
    slots = []
    for method in slot_generator_methods:
        slots.append(method(stunde, fächer)) # klappt das mit mehreren Slots?
    return slots

