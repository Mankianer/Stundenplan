from stundenplan.classes import Slot, TablePlan
import stundenplan.slot_methods as slot_methods


def create_plans(*names, slot_mask, config=None) -> [TablePlan]:
    """Creates a list of TablePlans

    :param names: list of names for the plans
    :param slot_mask: {day: [slot_number, slot_number, ...], ...} mask of slots that are available per day
    :param config: config object
        {
        "slot_generator": [(slot_generator_method, expected_context, default_slot_options)],
        "slot_filter": [(slot_filter_method, expected_context, default_slot_options)],
        "slot_ranker": [(slot_ranker_method, expected_context, default_slot_options)],
        }
    """

    if config is None:
        config = get_default_config()

    expected_slot_context = get_expected_slot_context(config)
    default_slot_options = get_default_slot_options(config)

    plans = []
    for name in names:
        plans.append(TablePlan(name, slot_mask, config, expected_slot_context, default_slot_options))
    return plans


def get_expected_slot_context(config) -> {}:
    """Returns a dict of expected slot context for each slot method type
    """
    expected_slot_context = {}
    for slot_method_type in "slot_generator", "slot_filter", "slot_rating":
        for method, context, options in config[slot_method_type]:
            if context is not None:
                expected_slot_context.update(context)

    return expected_slot_context


def get_default_slot_options(config) -> {}:
    """Returns a dict of default slot options for each slot method type
    """
    default_slot_options = {}
    for slot_method_type in "slot_generator", "slot_filter", "slot_rating":
        for method, context, options in config[slot_method_type]:
            if options is not None:
                default_slot_options.update(options)

    return default_slot_options


def get_default_config():
    return {
        "slot_generator": slot_methods.global_generator_methods.copy(),
        "slot_filter": slot_methods.global_filter_methods.copy(),
        "slot_rating": slot_methods.global_rating_methods.copy(),
    }
