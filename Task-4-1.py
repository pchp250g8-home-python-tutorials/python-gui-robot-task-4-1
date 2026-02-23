from robot import *

while(is_free_right() or is_free_left() or is_free_down()):
    while(is_free_right()):
        paint()
        move_right()
    paint()
    move_down()
    while(is_free_left()):
        paint()
        move_left()
    paint()
    move_down()
paint()