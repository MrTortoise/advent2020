import unittest

from day2.passwordsparser import PasswordsParser
from day2.password import Password
from day2.day21Validator import is_valid as is_valid1
from day2.day22Validator import is_valid as is_valid2


class PasswordWill(unittest.TestCase):

    def test_pass21(self):
        data = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
        parser = PasswordsParser(data)
        total_valid = Password.get_total_valid(parser.passwords, is_valid1)

        self.assertEqual(2, total_valid)

    def test_pass22(self):
        data = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
        parser = PasswordsParser(data)
        total_valid = Password.get_total_valid(parser.passwords, is_valid2)

        self.assertEqual(1, total_valid)
