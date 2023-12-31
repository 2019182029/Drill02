from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 0, 90

while (True) :
    if(x == 0 and y == 90) :
        while (x < 800) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x += 2
            delay(0.01)
    if(x == 800 and y == 90) :
        while (y < 600) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800, y)
            y += 2
            delay(0.01)
    if(x == 800 and y == 600) :
        while (x > 0) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 600)
            x -= 2
            delay(0.01)
    if(x == 0 and y == 600) :
        while (y > 90) :
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, y)
            y -= 2
            delay(0.01)
    
close_canvas()
