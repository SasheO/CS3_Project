import string
import secrets
alphenumeric = string.ascii_letters + string.digits
while True:
    token = ''.join(secrets.choice(alphenumeric) for i in range(10))
    if (any(c.islower() for c in token)
            and any(c.isupper() for c in token)
            and sum(c.isdigit() for c in token) >= 3):
        break