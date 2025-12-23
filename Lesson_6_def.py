def is_very_long(password):
    password_length = len(password)
    if password_length > 12:
        return True
    else:
        return False

def has_digits(password):
    return any(c.isdigit() for c in password)

def has_letter(password):
    return any(p.isalpha() for p in password)

def has_upper_letters(password):
    return any(p.isupper() for p in password)

def has_lower_letters(password):
    return any(p.islower() for p in password)

def has_symbols(password):
    return any(p.isalnum() for p in password)

def rating_password(password):
    check = [has_digits, has_letter, has_upper_letters, has_lower_letters, has_symbols]
    score = 0
    for c in check:
        if c(password):
            score += 2
    rating = f'Рейтинг пароля {score}'
    return rating
