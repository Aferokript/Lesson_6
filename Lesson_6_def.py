def is_very_long(password):
    return len(password) >= 12


def has_digits(password):
    return any(c.isdigit() for c in password)


def has_letter(password):
    return any(p.isalpha() for p in password)


def has_upper_letters(password):
    return any(p.isupper() for p in password)


def has_lower_letters(password):
    return any(p.islower() for p in password)


def has_symbols(password):
    return any(not p.isalnum() for p in password)


def rating_password(password):
    check = [
       is_very_long,
       has_digits,
       has_letter,
       has_upper_letters,
       has_lower_letters,
       has_symbols
    ]
    score = 0
    for c in check:
        if c(password):
            score += 2
    return f'Рейтинг пароля {score}'


def main():
    password = input('Введите пароль ')
    print(rating_password(password))

if __name__ == '__main__':
    main()

