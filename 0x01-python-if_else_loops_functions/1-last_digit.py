#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
print(f"Last digit of {number} is", end=" ")
if int(number) >= 0:
    last_digit = int(number[-1])
else:
    last_digit = int(number[-1])*-1

if last_digit > 5:
    print(f"{last_digit} and is greater than 5")
elif int(number[-1]) == 0:
    print(f"{last_digit} and is 0")
else:
    print(f"{last_digit} and is less than 6 and not 0")
