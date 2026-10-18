# Jose Antonio Santiago Cabrera - Exercise 4 — Usernames (string methods)

full_name = input("Enter the full name: ")

letters = len(full_name.replace(" ", ""))
print(f"Full name: {full_name.upper()} has {letters} letters")

words = full_name.split()
username = (words[0][0] + words[1]).lower()
print(f"Username: {username}")