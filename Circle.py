from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 600

while(True) :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y))

close_canvas()
    
