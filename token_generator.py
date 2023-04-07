import string
import secrets

def token_generator():
    token_length = int(input("Enter the length of token"))
    alphenumeric = string.ascii_letters + string.digits
    while True:
        token = ''.join(secrets.choice(alphenumeric) for i in range(token_length))
        if (any(c.islower() for c in token)
                and any(c.isupper() for c in token)
                and sum(c.isdigit() for c in token) >= 3):
            break
