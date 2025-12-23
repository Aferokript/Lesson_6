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
    if '@' or '$' or '#' or '%' or '^' or '&' or '*' or '!' or '(' or ')' in password:
        return True

def rating_password(password):
    check = [has_digits, has_letter, has_upper_letters, has_lower_letters, has_symbols]
    score = 0
    for c in check:
        if c(password):
            score += 2
    rating = f'Рейтинг пароля {score}'
    return rating

print(is_very_long('Password234324'))
print(has_digits('Password234324'))
print(has_letter('Password234324'))
print(has_upper_letters('Password234324'))
print(has_lower_letters('Password234324'))
print(has_symbols('Password234324!'))
print(rating_password('Password234324'))
