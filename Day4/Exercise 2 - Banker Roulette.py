# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lenght = len(names)
name_picked = names[random.randint(0, lenght-1)]

print(f"{name_picked} is going to buy the meal today!")