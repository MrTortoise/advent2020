from day2.passwordsparser import PasswordsParser
from day2.password import Password
from day2.day21Validator import is_valid as is_valid1


def day21():
    data = open("data.txt").read()
    parser = PasswordsParser(data)
    total_valid = Password.get_total_valid(parser.passwords, is_valid1)
    print(total_valid)


if __name__ == '__main__':
    day21()
