#ignore this only to define the already defined functions so i dont get errors: 

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
def front_is_clear():
    print()
#ignore above



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()  
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        