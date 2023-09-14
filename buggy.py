import random

n1 = random.randint(1,10)
n2 = random.randint(1,10)

answer = input(f"What is {n1} + {n2}? : ")
if answer == n1 + n2:
    print("That's correct")
else:
    print(f"No. The answer is {n1 + n2}")
