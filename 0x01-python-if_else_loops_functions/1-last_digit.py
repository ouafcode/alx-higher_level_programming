#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dt = (((-1 * number) % 10) * -1)
else:
    last_dt = number % 10
if last_dt > 5:
    print("Last digit of {} is {} and is greater\
 than 5".format(number, last_dt))
elif last_dt == 0:
    print("Last digit of {} is {} and is\
 0".format(number, last_dt))
elif last_dt < 6 and not 0:
    print("Last digit of {} is {} and is less than 6\
 and not 0".format(number, last_dt))
