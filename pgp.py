# PASSWORD GENERATOR PROJECT WITH PYTHON

import string
import random

Charac= string.ascii_letters + string.punctuation + string.hexdigits

Inp= int(input('Enter your Password Digit No. '))
Password=''

for i in range(Inp):
    s=random.choice(Charac)
    Password=Password+s

print(f'Your Password is :- {Password} ')
