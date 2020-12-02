import unittest
from day2.validator import Validator
from day2.passwordsparser import PasswordsParser


class PasswordWill(unittest.TestCase):

    def test_pass(self):
        data = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
        parser = PasswordsParser(data)
        total_valid = Validator.get_total_valid(parser.passwords)

        self.assertEqual(2, total_valid)
