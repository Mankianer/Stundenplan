

global_generator_methods = []


def slot_generator_method(expected_slot_context, default_option=None):
    """Fügt eine Methode der Liste der Methoden hinzu
    func: (slot_context, slot_options) -> [Slot]
    """
    # expected_slot_context = kwargs.get("expected_slot_context")
    # default_option = kwargs.get("default_option")

    def decorator(func):
        global_generator_methods.append((func, expected_slot_context, default_option))
        return func

    return decorator

