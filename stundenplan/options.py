fächer = {
    'min_slot_size': 1,
    'empty_fach_name': 'N/A',
}

options = {
    'slot_length': 1,
    'fächer': fächer
}


def get_default_slot_length():
    return options['slot_length']

def get_default_min_slot_size():
    return options['fächer']['min_slot_size']

def get_default_empty_fach_name():
    return options['fächer']['empty_fach_name']
