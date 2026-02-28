from robot import *

while(is_free_right() or is_free_left() or is_free_down()):
    while(is_free_right() and is_wall_down()):
        paint()
        move_right()
    while(is_free_left() and is_wall_down()):
        paint()
        move_left()
    while is_free_down():
        paint()
        move_down()
paint()