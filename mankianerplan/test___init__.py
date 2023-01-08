from unittest import TestCase
import mankianerplan
import mankianerplan.slot_methods as slot_methods


class Test(TestCase):
    def test_create_plans_slot_mask(self):
        # test slot_mask is applied to plan
        tag1 = "Tag 1 - Negativ"
        tag2 = "Tag 2 - Positiv"
        tag3 = "Tag 3 - Leer"
        tag4 = "Tag 4 - Lücke"
        plans = mankianerplan.create_plans("test", slot_mask={tag1: list(range(-1, 6)), tag2: list(range(1, 4)), tag3: [],
                                                              tag4: [range(1, 3), range(4, 6)]})

        self.assertCountEqual([tag1, tag2, tag3, tag4], plans[0].get_plan().keys(), 'days are not correct')
        self.assertCountEqual(list(range(-1, 6)), plans[0].get_plan()[tag1].keys(), 'slots are not correct - Negativ')
        self.assertCountEqual(list(range(1, 4)), plans[0].get_plan()[tag2].keys(), 'slots are not correct - Positiv')
        self.assertCountEqual({}, plans[0].get_plan()[tag3].keys(), 'slots are not correct - Leer')
        self.assertCountEqual([range(1, 3), range(4, 6)], plans[0].get_plan()[tag4].keys(),
                              'slots are not correct - Lücke')

    def test_create_plans_config(self):
        # test config is default_config when not given
        plans = mankianerplan.create_plans("test", slot_mask={})
        self.assertIsNotNone(plans[0].config, 'config is not created')
        self.assertDictEqual(mankianerplan.get_default_config(), plans[0].config, 'config is not default_config')
        # test if default_slot_options is set correctly
        self.assertDictEqual(mankianerplan.get_default_slot_options(plans[0].config),
                             plans[0].slot_options, 'default_slot_options is not set correctly')

    def test_get_default_config(self):
        # setup slot_methods
        @slot_methods.slot_generator_method()
        @slot_methods.slot_rating_method()
        @slot_methods.slot_filter_method()
        def test_func():
            return []

        defaults = mankianerplan.get_default_config()
        # slot_generator is equals to global_generator_methods
        self.assertCountEqual(defaults["slot_generator"], mankianerplan.slot_methods.global_generator_methods,
                              'slot_generator is not equal to global_generator_methods')
        # slot_rating is equals to global_rating_methods
        self.assertCountEqual(defaults["slot_rating"], mankianerplan.slot_methods.global_rating_methods,
                              'slot_rating is not equal to global_rating_methods')
        # slot_filter is equals to global_filter_methods
        self.assertCountEqual(defaults["slot_filter"], mankianerplan.slot_methods.global_filter_methods,
                              'slot_filter is not equal to global_filter_methods')

    def test_get_default_slot_options(self):
        def test_func(*args, **kwargs):
            return []

        # test with empty config
        empty_options = mankianerplan.get_default_config()
        empty_options["slot_generator"] = [(test_func, None)]
        empty_options["slot_rating"] = [(test_func, None)]
        empty_options["slot_filter"] = [(test_func, None)]
        slot_options = mankianerplan.get_default_slot_options(empty_options)
        self.assertDictEqual(slot_options, {}, 'slot_options is not empty')

        # test with single slot_options
        single_options = mankianerplan.get_default_config()
        single_options["slot_generator"] = [(test_func, {"test": "test1"})]
        single_options["slot_rating"] = [(test_func, {"test": "test2"})]
        single_options["slot_filter"] = [(test_func, {"test": "test3"})]

        slot_options = mankianerplan.get_default_slot_options(single_options)
        self.assertDictEqual(slot_options, {"test": "test2"}, 'slot_options is not single')

        # test with multiple slot_options
        multiple_options = mankianerplan.get_default_config()
        multiple_options["slot_generator"] = [(test_func, {"test": "test"}),
                                              (test_func, {"test2": "test2"})]
        multiple_options["slot_rating"] = [(test_func, {"test": "test"}),
                                           (test_func, {"test2": "test2"})]
        multiple_options["slot_filter"] = [(test_func, {"test": "test"}),
                                           (test_func, {"test2": "test2"})]
        slot_options = mankianerplan.get_default_slot_options(multiple_options)
        self.assertDictEqual(slot_options, {"test": "test", "test2": "test2"},
                             'slot_options is not multiple')
        # test with multiple expected_slot_context and None
        multiple_options = mankianerplan.get_default_config()
        multiple_options["slot_generator"] = [(test_func, {"test": "test1"}),
                                              (test_func, None)]
        multiple_options["slot_rating"] = [(test_func, {"test": "test2"}),
                                           (test_func, None)]
        multiple_options["slot_filter"] = [(test_func, {"test": "test3"}),
                                           (test_func, None)]
        slot_options = mankianerplan.get_default_slot_options(multiple_options)
        self.assertDictEqual(slot_options, {"test": "test2"}, 'slot_options is not multiple with None')

        # test with lists
        list_options = mankianerplan.get_default_config()
        list_options["slot_generator"] = [(test_func, {"test": [7, 8, 9]})]
        list_options["slot_rating"] = [(test_func, {"test": [1, 2, 3]})]
        list_options["slot_filter"] = [(test_func, {"test": [4, 5, 6]})]
        slot_options = mankianerplan.get_default_slot_options(list_options)
        self.assertDictEqual(slot_options, {"test": [1, 2, 3]}, 'slot_options is not list')

        # test with sub dicts
        multiple_options = mankianerplan.get_default_config()
        multiple_options["slot_generator"] = [(test_func, {"test": {"test": "test1"}})]
        multiple_options["slot_rating"] = [(test_func, {"test": {"test": "test2"}})]
        multiple_options["slot_filter"] = [(test_func, {"test": {"test3": "test3"}})]
        slot_options = mankianerplan.get_default_slot_options(multiple_options)
        self.assertDictEqual(slot_options, {"test": {"test": "test2", "test3": "test3"}},
                             'slot_options can not handle sub dicts')

        # test with collision with same type
        collition_options = mankianerplan.get_default_config()
        collition_options["slot_generator"] = [(test_func, {"test": "test"}),
                                               (test_func, {"test": "test2b"})]
        collition_options["slot_rating"] = [(test_func, {"test": "test2"})]
        collition_options["slot_filter"] = []
        slot_options = mankianerplan.get_default_slot_options(collition_options)
        self.assertDictEqual(slot_options, {"test": "test2"}, 'slot_options has wrong collision')

        # test with collision with different type
        collition_options = mankianerplan.get_default_config()
        collition_options["slot_generator"] = [(test_func, {"test": {"test": "test"}}),
                                               (test_func, {"test": 2})]
        collition_options["slot_rating"] = [(test_func, {"test": {"test1": "test2"}})]
        collition_options["slot_filter"] = []
        slot_options = mankianerplan.get_default_slot_options(collition_options)
        self.assertDictEqual(slot_options, {"test": {"test1": "test2"}},
                             'slot_options has wrong collision')
