def is_valid(password):
    total = sum(1 for c in password.password if c == password.char)
    return password.min <= total <= password.max
