global_generator_methods = []
global_rating_methods = []
global_filter_methods = []


def __get_slot_decorator(target_list: [], expected_slot_context, default_option):
    def decorator(func):
        target_list.append((func, expected_slot_context, default_option))
        return func

    return decorator


def slot_generator_method(expected_slot_context, default_option=None):
    """Decorator for slot generator methods
    func: (slot_context, slot_options) -> [Slot]

    :param expected_slot_context: expected context for the slot generator method - used for documentation of expected
    context
    :param default_option: default option for the slot generator method - used for documentation of options
    """
    return __get_slot_decorator(global_generator_methods, expected_slot_context, default_option)


def slot_rating_method(expected_slot_context, default_option=None):
    """Decorator for slot rating methods
    func: (slot, table_plan) -> int

    :param expected_slot_context: expected context for the slot rating method - used for documentation of expected
    context
    :param default_option: default option for the slot rating method - used for documentation of options
    """
    return __get_slot_decorator(global_rating_methods, expected_slot_context, default_option)


def slot_filter_method(expected_slot_context, default_option=None):
    """Decorator for slot filter methods
    func: (slot, table_plan) -> bool

    :param expected_slot_context: expected context for the slot filter method - used for documentation of expected
    context
    :param default_option: default option for the slot filter method - used for documentation of options
    """
    return __get_slot_decorator(global_filter_methods, expected_slot_context, default_option)
