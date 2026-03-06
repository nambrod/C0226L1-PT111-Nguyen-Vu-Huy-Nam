def is_long_enough(password):
    if len(password) >= 8:
        return True
    else:
        return False
def has_uppercase(password):
    count = 0
    for letter in password:
        if letter.isupper() == True:
            count += 1
    if count > 0:
        return True
    else:
        return False
def has_number(password):
    count = 0
    for letter in password:
        if letter.isdigit() == True:
            count += 1
    if count > 0:
        return True
    else:
        return False
def is_strong_password(password):
    if is_long_enough(password) and has_uppercase(password) and has_number(password) == True:
        return True
    else:
        return False