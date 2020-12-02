from day2.passwordsparser import PasswordsParser
from day2.validator import Validator


def day21():
    data = open("data.txt").read()
    parser = PasswordsParser(data)
    total_valid = Validator.get_total_valid(parser.passwords)
    print(total_valid)


if __name__ == '__main__':
    day21()
