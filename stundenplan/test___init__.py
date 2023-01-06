from unittest import TestCase
import stundenplan
import stundenplan.slot_methods as slot_methods


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
        # test if expected_slot_context is set correctly
        self.assertDictEqual(stundenplan.get_expected_slot_context(plans[0].config),
                             plans[0].expected_slot_context, 'expected_slot_context is not set correctly')
        # test if default_slot_options is set correctly
        self.assertDictEqual(stundenplan.get_default_slot_options(plans[0].config),
                                plans[0].slot_options, 'default_slot_options is not set correctly')

    def test_get_default_config(self):
        # setup slot_methods
        @slot_methods.slot_generator_method(expected_slot_context=None)
        @slot_methods.slot_rating_method(expected_slot_context=None)
        @slot_methods.slot_filter_method(expected_slot_context=None)
        def test_func():
            return []

        defaults = stundenplan.get_default_config()
        # slot_generator is equals to global_generator_methods
        self.assertCountEqual(defaults["slot_generator"], stundenplan.slot_methods.global_generator_methods,
                              'slot_generator is not equal to global_generator_methods')
        # slot_rating is equals to global_rating_methods
        self.assertCountEqual(defaults["slot_rating"], stundenplan.slot_methods.global_rating_methods,
                              'slot_rating is not equal to global_rating_methods')
        # slot_filter is equals to global_filter_methods
        self.assertCountEqual(defaults["slot_filter"], stundenplan.slot_methods.global_filter_methods,
                              'slot_filter is not equal to global_filter_methods')

    def test_get_expected_slot_context(self):
        def test_func(*args, **kwargs):
            return []

        # test with empty config
        empty_expected_context = stundenplan.get_default_config()
        empty_expected_context["slot_generator"] = [(test_func, None, None)]
        empty_expected_context["slot_rating"] = [(test_func, None, None)]
        empty_expected_context["slot_filter"] = [(test_func, None, None)]
        expected_slot_context = stundenplan.get_expected_slot_context(empty_expected_context)
        self.assertDictEqual(expected_slot_context, {}, 'expected_slot_context is not empty')
        # test with single expected_slot_context
        single_expected_context = stundenplan.get_default_config()
        single_expected_context["slot_generator"] = [(test_func, {"test": "test"}, None)]
        single_expected_context["slot_rating"] = [(test_func, {"test": "test"}, None)]
        single_expected_context["slot_filter"] = [(test_func, {"test": "test"}, None)]
        expected_slot_context = stundenplan.get_expected_slot_context(single_expected_context)
        self.assertDictEqual(expected_slot_context, {"test": "test"}, 'expected_slot_context is not single')
        # test with multiple expected_slot_context
        multiple_expected_context = stundenplan.get_default_config()
        multiple_expected_context["slot_generator"] = [(test_func, {"test": "test"}, None),
                                                       (test_func, {"test2": "test2"}, None)]
        multiple_expected_context["slot_rating"] = [(test_func, {"test": "test"}, None
                                                     ), (test_func, {"test2": "test2"}, None)]
        multiple_expected_context["slot_filter"] = [(test_func, {"test": "test"}, None
                                                     ), (test_func, {"test2": "test2"}, None)]
        expected_slot_context = stundenplan.get_expected_slot_context(multiple_expected_context)
        self.assertDictEqual(expected_slot_context, {"test": "test", "test2": "test2"},
                             'expected_slot_context is not multiple')

        # ToDo: test with sub dicts

    def test_get_default_slot_options(self):
        def test_func(*args, **kwargs):
            return []

        # test with empty config
        empty_options = stundenplan.get_default_config()
        empty_options["slot_generator"] = [(test_func, None, None)]
        empty_options["slot_rating"] = [(test_func, None, None)]
        empty_options["slot_filter"] = [(test_func, None, None)]
        slot_options = stundenplan.get_default_slot_options(empty_options)
        self.assertDictEqual(slot_options, {}, 'slot_options is not empty')

        # test with single slot_options
        single_options = stundenplan.get_default_config()
        single_options["slot_generator"] = [(test_func, None, {"test": "test"})]
        single_options["slot_rating"] = [(test_func, None, {"test": "test"})]
        single_options["slot_filter"] = [(test_func, None, {"test": "test"})]

        slot_options = stundenplan.get_default_slot_options(single_options)
        self.assertDictEqual(slot_options, {"test": "test"}, 'slot_options is not single')

        # test with multiple slot_options
        multiple_options = stundenplan.get_default_config()
        multiple_options["slot_generator"] = [(test_func, None, {"test": "test"}),
                                              (test_func, None, {"test2": "test2"})]
        multiple_options["slot_rating"] = [(test_func, None, {"test": "test"}),
                                           (test_func, None, {"test2": "test2"})]
        multiple_options["slot_filter"] = [(test_func, None, {"test": "test"}),
                                           (test_func, None, {"test2": "test2"})]
        slot_options = stundenplan.get_default_slot_options(multiple_options)
        self.assertDictEqual(slot_options, {"test": "test", "test2": "test2"},
                             'slot_options is not multiple')
        # ToDo: test with sub dicts
