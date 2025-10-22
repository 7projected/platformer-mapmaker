import pygame

class Panel(pygame.Rect):
    def __init__(self, position, size, color, color2, outline = False, inline = True, outline_width = 2):
        self.topleft = position
        self.size = size
        self.color = color
        self.color2 = color2
        self.current_color = 1

        self.outline = outline
        self.inline = inline
        self.outline_width = outline_width

    def draw_rect(self, surf, color, oppcolor):
        if self.inline:
            pygame.draw.rect(surf, color, self)
        if self.outline:
            pygame.draw.rect(surf, oppcolor, self, self.outline_width)

    def update(self, mouse_pos):
        pass

    def draw(self, surf):
        if self.current_color == 1:
            self.draw_rect(surf, self.color, self.color2)
        if self.current_color == 2:
            self.draw_rect(surf, self.color2, self.color)

class Button(Panel):
    def __init__(self, callback:callable, font:pygame.font.Font, text:str, position, size, text_color, color, color2, outline=False, inline=True, outline_width=2):
        super().__init__(position, size, color, color2, outline, inline, outline_width)
        self.callback = callback
        self.text = text
        self.text_color = text_color
        self.font = font
    
    def update(self, mouse_pos):
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        if (mouse_rect.colliderect(self)):
            self.callback()

    def draw(self, surf):
        super().draw(surf)
        txt = self.font.render(self.text, False, self.text_color)