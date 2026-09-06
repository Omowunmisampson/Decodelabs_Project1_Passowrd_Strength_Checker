import string


def check_password(password):
    has_uppercase = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    if len(password) >= 8:
        score += 1

    if has_uppercase:
        score += 1

    if has_number:
        score += 1

    if has_symbol:
        score += 1

    if score <= 1:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength


# Test the password
password = "CyberTest123@"

print("Password:", password)
print("Password strength:", check_password(password))
