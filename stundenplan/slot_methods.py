global_generator_methods = []
global_rating_methods = []
global_filter_methods = []


def __get_slot_decorator(target_list: [], default_option):
    def decorator(func):
        target_list.append((func, default_option))
        return func

    return decorator


def slot_generator_method(default_option=None):
    """Decorator for slot generator methods
    func: (slot_context, slot_options) -> [Slot]

    :param default_option: default option for the slot generator method - used for documentation of options
    """
    return __get_slot_decorator(global_generator_methods, default_option)


def slot_rating_method(default_option=None):
    """Decorator for slot rating methods
    func: (slot, table_plan) -> int

    :param default_option: default option for the slot rating method - used for documentation of options
    """
    return __get_slot_decorator(global_rating_methods, default_option)


def slot_filter_method(default_option=None):
    """Decorator for slot filter methods
    func: (slot, table_plan) -> bool

    :param default_option: default option for the slot filter method - used for documentation of options
    """
    return __get_slot_decorator(global_filter_methods, default_option)
