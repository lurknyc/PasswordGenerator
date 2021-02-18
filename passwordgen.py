

import string

import secrets

alphabet = string.ascii_letters + string.digits 

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(15))

    if (sum(c.islower() for c in password) >=4
            and sum(c.isupper() for c in password) >=4
            and sum(c.isdigit() for c in password) >=4):
            print (password)
            break