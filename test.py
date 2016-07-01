import unittest

from example import hello_world, split_dollar_bills, dont_pass_42, SomeException


class TestExample(unittest.TestCase):
    def test_hello_world(self):
        assert hello_world() == "hello world!"

    def test_split_dollar_bills(self):
        self._split_dollar_bill_helper(n_persons=10, n_bills=19, expected=1)
        self._split_dollar_bill_helper(n_persons=20, n_bills=41, expected=2)

    def _split_dollar_bill_helper(self, n_persons, n_bills, expected):
        result = split_dollar_bills(n_persons, n_bills)
        self.assertTrue(result == expected,
                        "Expected {exp} but got {result}".
                        format(exp=expected, result=result))

    def test_dont_pass_42(self):
        with self.assertRaises(SomeException):
            dont_pass_42(42)
