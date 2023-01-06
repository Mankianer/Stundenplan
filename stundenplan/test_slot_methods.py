from unittest import TestCase

import slot_methods


class Test(TestCase):

    def test_slot_generator_method(self):
        @slot_methods.slot_generator_method(expected_slot_context=None)
        def test_func():
            return []

        self.assertIn(test_func.__name__, [method.__name__ for method, c, o in slot_methods.global_generator_methods])

    def test_slot_rating_method(self):
        @slot_methods.slot_rating_method(expected_slot_context=None)
        def test_func():
            return []

        self.assertIn(test_func.__name__, [method.__name__ for method, c, o in slot_methods.global_rating_methods])

    def test_slot_filter_method(self):
        @slot_methods.slot_filter_method(expected_slot_context=None)
        def test_func():
            return []

        self.assertIn(test_func.__name__, [method.__name__ for method, c, o in slot_methods.global_filter_methods])