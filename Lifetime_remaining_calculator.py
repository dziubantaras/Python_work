# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = (90 - int(age))
month_left = years_left * 12
weeks_left = years_left * 52
days_left  = years_left * 365

message = (f"You have {days_left} days, {weeks_left} weeks, and {month_left} months left.")
print(message)