# compound interest

P = 10000
n = 12
r = 0.08

t = int(input("Enter years : "))

A = P * (1 + r/n) ** (n*t)

print("Amount =", A)
