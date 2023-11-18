import os

from frame import DefaultFrame
from obj import BaseObj, Obj


class Window(BaseObj):
    def __init__(self, title: str, frame = DefaultFrame, width: int = 150, height: int = 40) -> None:
        self.width = width
        self.height = height
        super().__init__(frame=frame)
        self.frame = self.Frame.get_frame(width, height)
        self.__buffer = self.frame
        self.title = title

    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = f'[ {title} ]'
        self._insert_title_into_frame()

    def _insert_title_into_frame(self):
        title_len = len(self.title)
        gap = (self.width - title_len) // 2
        self.frame = self.insert(self.frame, self.title, gap, 0)
        self.__buffer = self.insert(self.__buffer, self.title, gap, 0)

    @staticmethod
    def clear():
        os.system('clear')

    def clear_buffer(self):
        self.__buffer = self.frame

    def flush(self):
        self.clear()
        print(self.__buffer, flush=True)

    def draw_obj(self, obj: Obj, x, y):
                self.__buffer = self.insert(
                self.__buffer,
                obj.text,
                x,
                y
                )

    def clear_draw_obj(self, obj: Obj, x, y):
        self.__buffer = self.insert(
                self.frame,
                obj.text,
                x,
                y
                )

