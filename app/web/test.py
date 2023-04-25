
import string
import random

length_of_string = 8
a = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

print(a)