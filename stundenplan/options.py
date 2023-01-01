fächer = {
    'empty_fach_name': 'N/A',
    'not_included_fach_name': 'NOT INCLUDED',
}

options = {
    'slot_length': 1,
    'fächer': fächer
}


def get_default_min_slot_size():
    return options['fächer']['min_slot_size']


def get_default_empty_fach_name():
    return options['fächer']['empty_fach_name']


def get_default_not_include_fach_name():
    return options['fächer']['not_included_fach_name']