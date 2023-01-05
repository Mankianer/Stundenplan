class Options:
    def __init__(self, options):
        self.options = options

    def get_default_min_slot_size(self):
        return self.options['fächer']['min_slot_size']

    def get_default_empty_fach_name(self):
        return self.options['fächer']['empty_fach_name']

    def get_default_not_include_fach_name(self):
        return self.options['fächer']['not_included_fach_name']

    def get_default_not_found_fach_name(self):
        return self.options['fächer']['not_found_fach_name']



def get_default_options():
    return Options({
        'fächer': {
            'min_slot_size': 1,
            'empty_fach_name': 'N/A',
            'not_included_fach_name': 'NOT INCLUDED',
            'not_found_fach_name': 'NOT FOUND',
        },
    })











