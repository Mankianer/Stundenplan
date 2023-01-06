class Slot:
    def __init__(self, context, options, day, start, end, rating=0):
        self.context = context
        self.options = options
        self.day = day
        self.start = start
        self.end = end
        self.rating = rating

    def __str__(self):
        return f"{self.day}:({self.start}-{self.end})"

    def __repr__(self):
        return self.__str__()


class TablePlan:
    def __init__(self, name, slot_mask, config, expected_slot_context, slot_options):
        """
        :param name: str
        :param slot_mask: {day: [slot_number, slot_number, ...], ...} mask of slots that are available per day
        :param slot_context:
        :param slot_options:

        """
        self.name = name
        self.slot_mask = slot_mask
        self.slot_context = {}
        self.expected_slot_context = expected_slot_context
        self.slot_options = slot_options
        self.config = config
        self.__plan = {}
        self.status = ""
        self.init_plan()

    def init_plan(self):
        self.__plan.clear()
        for day, slots in self.slot_mask.items():
            self.__plan[day] = {}
            for slot in slots:
                self.__plan[day][slot] = None
        self.status = "empty"

    def get_plan(self):
        return self.__plan

    def update_slot_mask(self, slot_mask):
        self.slot_mask = slot_mask
        self.init_plan()

    def __str__(self):
        return f"TablePlan: {self.name}"

    def __repr__(self):
        return self.__str__()
