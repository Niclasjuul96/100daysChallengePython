import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)

print(my_module.pi)

#random Random returns random numbers between 0 and 1, for increasing or decreasing the number then times the number
random_float = random.random()*100
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

states_of_america = ["Delaware", "Pennsylvania"]

num_of_states = len(states_of_america)

print(states_of_america[num_of_states-1])

fruits = ["Strawberry", "Nectarines", "Apple", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)