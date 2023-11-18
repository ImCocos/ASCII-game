from typing import Any
from frame import DefaultFrame


class BaseObj:
    def __init__(self, frame = DefaultFrame) -> None:
        self.Frame = frame

    def insert(self, window: Any, obj: Any, obj_x, obj_y) -> str:
        try:
            window = window.arrayed_text
        except:
            window = self.arraify_text(window)

        try:
            obj = obj.arrayed_text
        except:
            obj = self.arraify_text(obj)        
       
        obj_x -= (obj_x + obj.width+1)*int(obj_x+obj.width > window.width)
        obj_y -= (obj_y + obj.height+1)*int(obj_y+obj.height > window.height)

        
        for y, string in enumerate(obj):
            for x, let in enumerate(string):
                window[obj_y+y][obj_x+x] = let
                
        return self.dearraify_text(window)

    @staticmethod
    def arraify_text(s: str, gap: int = 0) -> list:
        class MyList(list):
            @property
            def width(self):
                return self._width
            @width.setter
            def width(self, n):
                self._width = n

            @property
            def height(self):
                return self._height
            @height.setter
            def height(self, n):
                self._height = n


        a = MyList()

        strings = s.strip().split('\n')
        max_string_len = max([len(string) for string in strings])
        for string in strings:
            a.append(list(' '*gap + string + ' '*(max_string_len-len(string)) + ' '*gap))

        a.width = len(a[0])
        a.height = len(a)


        return a

    @staticmethod
    def dearraify_text(text):
        return '\n'.join([''.join(string) for string in text])


class Obj(BaseObj):
    def __init__(self, text, frame = DefaultFrame):
        self.arrayed_text = self.arraify_text(text.strip('\n'), gap=1)

        self.width = len(self.arrayed_text[0])
        self.height = len(self.arrayed_text)
        
        super().__init__(frame)
        self.frame = self.Frame.get_frame(self.width, self.height)

        self.text = self.insert(self.frame, self, 1, 1)

