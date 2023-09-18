from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

degree = 1

while (True) :
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + cos(degree * pi / 180) * 250, 340 + sin(degree * pi / 180) * 250)
    degree += 1
    delay(0.01)
    
close_canvas()
