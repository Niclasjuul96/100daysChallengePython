#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_left():
    print()
def move():
    print()
def at_goal():
    print()
def wall_in_front():
    print()
def wall_on_right():
    print()
def right_is_clear():
    print()
def front_is_clear():
    print()
#ignore above


#standard but can happen to hit a specific starting point where, it ends up in a infinite loop. 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


#I have another solution where it getting rid of the infinite loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()  
while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()