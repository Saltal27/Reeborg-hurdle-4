def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while at_goal() is False:
    if wall_in_front():
        step()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
