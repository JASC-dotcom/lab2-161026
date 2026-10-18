# Jose Antonio Santiago Cabrera - Exercise 5 — Dates and prices (split, slicing and format)

# --- Date ---
date = input("Date: ")

day, month, year = date.split("/")
print(f"Date: {day.zfill(2)}/{month.zfill(2)}/{year}")

# --- Product ---
product = input("Product: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

euros = int(unit_price)
cents = round((unit_price - euros) * 100)
print(f"Euros: {euros} · Cents: {cents}")

total = unit_price * quantity
print(f"{product} {unit_price:09.2f} {quantity:03d} {total:011.2f}")