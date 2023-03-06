# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2

lowercase_string = combined_string.lower()

love = 0

love += lowercase_string.count('t')
love += lowercase_string.count('r')
love += lowercase_string.count('u')
love += lowercase_string.count('e')

first_digit = love
love = 0

love += lowercase_string.count('l')
love += lowercase_string.count('o')
love += lowercase_string.count('v')
love += lowercase_string.count('e')

second_digit = love

def concat(a, b):
    return int(f"{a}{b}")

num = int(concat(first_digit,second_digit))


if num < 10 or num > 90:
    print(f"Your score is {num}, you go together like coke and mentos.")
elif num > 40 and num < 50:
    print(f"Your score is {num}, you are alright together.")
else:
    print(f"Your score is {num}.")