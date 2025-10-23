import util, pygame, sys, texture

# first two bits (ff ff) are the size
# rest are pointers to indexs in a color palette  (one bit since 16 color pallete)

class App:
    def __init__(self):
        self.pal = util.Palette()
        self.pal.load_palette("purple")

        pygame.init() 

        self.sprite = texture.Texture([16, 16], self.pal)
        self.sprite.load_sprite_map("test", self.pal)

        self.clock = pygame.time.Clock()
        self.screen_size = [1, 1]

        self.screen = pygame.display.set_mode([1280, 720])
        self.size = 100
        self.selected_draw_color = self.pal.colors[0]
        self.selected_draw_color_index = 0
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.mouse.get_pos()[1] <= self.size:
                        num = pygame.mouse.get_pos()[0] / 100
                        if num <= self.pal.color_count:
                            self.selected_draw_color = self.pal.colors[int(num)]
                            self.selected_draw_color_index = int(num)

    def draw(self):
        self.screen.fill([0, 0, 0])

        for i, color in enumerate(self.pal.colors):
            pygame.draw.rect(self.screen, color, [i * self.size, 0, self.size, self.size])
            if i == self.selected_draw_color_index:
                pygame.draw.rect(self.screen, [0, 0, 0], [i * self.size, 0, self.size, self.size], 8)

        self.sprite.draw(self.screen, [400, 400])

        pygame.display.update()
        self.clock.tick(60)


app = App()
while True:
    app.update()
    app.draw()