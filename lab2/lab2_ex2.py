# Jose Antonio Santiago Cabrera - Exercise 2 — Storage growth (compound percentage)

GROWTH = 0.06

usage = float(input("Current usage (GB): "))

usage = usage * (1 + GROWTH)
print(f"Month 1: {usage:.2f} GB")

usage = usage * (1 + GROWTH)
print(f"Month 2: {usage:.2f} GB")

usage = usage * (1 + GROWTH)
print(f"Month 3: {usage:.2f} GB")