# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remaining_year = 90 - int(age)

remaining_days = remaining_year * 365

remaining_weeks = remaining_year * 52

remaining_months = remaining_year * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")