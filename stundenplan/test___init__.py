from unittest import TestCase
import stundenplan


class Test(TestCase):
    def test_create_plans_slot_mask(self):
        # test slot_mask is applied to plan
        tag1 = "Tag 1 - Negativ"
        tag2 = "Tag 2 - Positiv"
        tag3 = "Tag 3 - Leer"
        tag4 = "Tag 4 - Lücke"
        plans = stundenplan.create_plans("test", slot_mask={tag1: list(range(-1, 6)), tag2: list(range(1, 4)), tag3: [],
                                                            tag4: [range(1, 3), range(4, 6)]})

        self.assertCountEqual([tag1, tag2, tag3, tag4], plans[0].get_plan().keys(), 'days are not correct')
        self.assertCountEqual(list(range(-1, 6)), plans[0].get_plan()[tag1].keys(), 'slots are not correct - Negativ')
        self.assertCountEqual(list(range(1, 4)), plans[0].get_plan()[tag2].keys(), 'slots are not correct - Positiv')
        self.assertCountEqual({}, plans[0].get_plan()[tag3].keys(), 'slots are not correct - Leer')
        self.assertCountEqual([range(1, 3), range(4, 6)], plans[0].get_plan()[tag4].keys(),
                              'slots are not correct - Lücke')

    def test_create_plans_config(self):
        # test config is default_config when not given
        plans = stundenplan.create_plans("test", slot_mask={})
        self.assertIsNotNone(plans[0].config, 'config is not created')
        self.assertDictEqual(stundenplan.get_default_config(), plans[0].config, 'config is not default_config')