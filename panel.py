import pygame

class Panel(pygame.Rect):
    def __init__(self, position, size, color, color2 = 0, outline = False, inline = True, outline_width = 8):
        self.topleft = position
        self.size = size
        self.color = color
        self.color2 = color
        if color2 != 0: self.color2 = color2
        self.current_color = 1

        self.outline = outline
        self.inline = inline
        self.outline_width = outline_width

    def draw_rect(self, surf, color, oppcolor):
        if self.inline:
            pygame.draw.rect(surf, color, self)
        if self.outline:
            pygame.draw.rect(surf, oppcolor, self, self.outline_width)

    def draw(self, surf):
        if self.current_color == 1:
            self.draw_rect(surf, self.color, self.color2)
        if self.current_color == 2:
            self.draw_rect(surf, self.color2, self.color)