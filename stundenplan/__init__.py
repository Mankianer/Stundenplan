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

    expected_slot_context = None  # TODO: add expected slot context from config
    default_slot_options = None # TODO: add default slot options from config

    plans = []
    for name in names:
        plans.append(TablePlan(name, slot_mask, config, expected_slot_context, default_slot_options))
    return plans


def get_default_config():
    return {
        "slot_generator": slot_methods.global_generator_methods.copy(),
        "slot_filter": [],
        "slot_ranker": [],
    }
