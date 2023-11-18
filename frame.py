from typing import Any


class Frame:

    @classmethod
    def get_frame(cls: Any, width, height):
        return cls.angle + cls.horizontal*width + cls.angle + '\n'\
                + (cls.side + ' '*width + cls.side + '\n')*height +\
                cls.angle + cls.horizontal*width + cls.angle



class DefaultFrame(Frame):
    side = '|'
    horizontal = '-'
    angle = '+'

class Frame1(Frame):
    side = '^'
    horizontal = '='
    angle = '#'

class Frame2(Frame):
    side = '#'
    horizontal = ':'
    angle = 'X'
