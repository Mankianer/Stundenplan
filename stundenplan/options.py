fächer = {
    'min_slot_size': 1,
    'empty_fach_name': 'N/A',
    'not_included_fach_name': 'NOT INCLUDED',
    'not_found_fach_name': 'NOT FOUND',
}

default_slot = {
    'fit_perfect': 20,
    'ranking_threshold': 0,
}

options = {
    'fächer': fächer
}


def get_default_min_slot_size():
    return options['fächer']['min_slot_size']


def get_default_empty_fach_name():
    return options['fächer']['empty_fach_name']


def get_default_not_include_fach_name():
    return options['fächer']['not_included_fach_name']


def get_default_not_found_fach_name():
    return options['fächer']['not_found_fach_name']


### default_slot_ranking.py


def get_slot_ranking_fit_perfect():
    return default_slot['fit_perfect']


def get_slot_ranking_threshold():
    return default_slot['ranking_threshold']