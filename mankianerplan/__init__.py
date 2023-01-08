from mankianerplan.classes import Slot, TablePlan
import mankianerplan.slot_methods as slot_methods
from mergedeep import merge


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

    default_slot_options = get_default_slot_options(config)

    plans = []
    for name in names:
        plans.append(TablePlan(name, slot_mask, config, default_slot_options))
    return plans


def get_default_slot_options(config):
    """Returns a dict of default slot options for each slot method type
    """
    slot_config = {}
    for slot_method_type in "slot_generator", "slot_filter", "slot_rating":
        for entry in config[slot_method_type]:
            if entry[1] is not None:
                slot_config = merge(slot_config, entry[1])

    return slot_config


def get_default_config():
    return {
        "slot_generator": slot_methods.global_generator_methods.copy(),
        "slot_filter": slot_methods.global_filter_methods.copy(),
        "slot_rating": slot_methods.global_rating_methods.copy(),
    }
