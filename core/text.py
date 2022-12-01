from typing import Tuple
from pygame.font import Font
from pygame import Rect, Surface
from pygame import font

font.init()

class Text():
    def __init__(self, text:str, TopLeft_position:Tuple[int, int], color:Tuple[int, int, int], font=Font(None, 30)):
        self.text = text
        self.position = TopLeft_position
        self.color = color
        self.surface = Font.render(font, self.text, True, self.color)
        self.rect = self.surface.get_rect(topleft=self.position)
    
    def render(self, Surface:Surface) -> Rect:
        Surface.blit(self.surface, self.rect)
