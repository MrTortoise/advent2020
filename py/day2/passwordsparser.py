from day2.password import Password


class PasswordsParser:

    def __init__(self, text):
        lines = text.split('\n')
        self.passwords = [Password(i) for i in lines]
