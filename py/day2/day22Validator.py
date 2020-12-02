def is_valid(password):
    first = password.password[password.min-1] == password.char
    second = password.password[password.max-1] == password.char

    return xor(first, second)


def xor(lhs, rhs):
    return lhs != rhs
