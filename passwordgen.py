
import string

import secrets

length = input('How long do you need the password to be?\n')

alphabet = string.ascii_letters + string.digits 

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(int(length)))

    if (sum(c.islower() for c in password) >=4
            and sum(c.isupper() for c in password) >=4
            and sum(c.isdigit() for c in password) >=4):
            print (password)
            break 