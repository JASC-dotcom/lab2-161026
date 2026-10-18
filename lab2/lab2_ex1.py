# Jose Antonio Santiago Cabrera - Exercise 1 — Server uptime (integer division and remainder)

seconds = int(input("Seconds: "))

days = seconds // 86400      # 86400 s = 1 day
rest = seconds % 86400
hours = rest // 3600
rest = rest % 3600
minutes = rest // 60
secs = rest % 60

print(f"{seconds} seconds are {days} days, {hours} hours, {minutes} minutes and {secs} seconds")