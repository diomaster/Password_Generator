import random
import string

print('Hello! Welcome to my Password Generator')

len = int(input('\n Enter the length of the password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbos = string.punctuation


setup = lower + upper + number + symbos

temp = random.sample(setup, len)
password = "". join(temp)

setup = string.ascii_letters + string.digits + string.punctuation
passes = "".join(random.sample(setup,len))

print(password)

