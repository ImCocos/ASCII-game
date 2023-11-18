from window import Window

from obj import Obj

from frame import Frame1, Frame2

import time
from time import monotonic

from random import shuffle


window = Window('Game')

text = '''
This is long text
i think(and really hope) it will
draw perfect
'''
title = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz_-+=~`!@#$%^&*()1234567890'
title = list(title)

square = Obj('''
@@@@@@
@@@@@@
@@@@@@
''', frame = Frame2)

x = 37
y = 18

speed_x = 1
speed_y = 1

while 1:
    window.flush()

    st = monotonic()

    shuffle(title)
    window.title = ''.join(title)
    window.draw_obj(square, x, y)
    
    if x + speed_x + square.width >= window.width:
        speed_x *= -1
    elif x + speed_x <= 0:
        speed_x *= -1
    x += speed_x

    if y + speed_y + square.height >= window.height:
        speed_y *= -1
    elif y + speed_y <= 0:
        speed_y *= -1
    y += speed_y
    
    window.draw_obj(Obj(f'X: {x}; Y: {y}\nSX: {speed_x}; SY: {speed_y}'), 150, 1)

    t = monotonic() - st
    time.sleep(0.08-t)

