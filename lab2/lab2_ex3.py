# Jose Antonio Santiago Cabrera - Exercise 3 — Formulas and operator precedence

n = int(input("n: "))

sum_n = n * (n + 1) // 2
sum_squares = n * (n + 1) * (2 * n + 1) // 6

print(f"Sum: {sum_n}")
print(f"Sum of squares: {sum_squares}")

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / height ** 2

print(f"Your Body Mass Index is {bmi:.2f}")