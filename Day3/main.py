water_level = 50

if water_level > 80:
    print("drain water level")
else:
    print("Continue")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        print("Child tickets are $5.")
        ticket = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        ticket = 7
    elif age > 18:
        if age > 45 and age < 55:
            print("Everything is going to be ok. Have a free ride on us")
            ticket = 0
        else:
            print("Adult tickets are $12")
            ticket = 12
    
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        ticket += 3

    print(f"Your final ticket is ${ticket}")
else:
    print("Sorry, you have to grow taller before you can ride.")

