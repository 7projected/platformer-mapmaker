import util, pygame, sys

# first two bits (ff ff) are the size
# rest are pointers to indexs in a color palette  (one bit since 16 color pallete)

class App:
    def __init__(self):
        self.pal = util.Palette()
        self.pal.load_palette()

        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen_size = [1, 1]

        self.screen = pygame.display.set_mode([1280, 720])
        self.size = 100
        self.selected_draw_color = self.pal.color_list[0]
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
                        try:
                            self.selected_draw_color = self.pal.color_list[int(num)]
                            self.selected_draw_color_index = int(num)
                        except:
                            pass

    def draw(self):
        self.screen.fill([0, 0, 0])

        for i, color in enumerate(self.pal.color_list):
            pygame.draw.rect(self.screen, color, [i * self.size, 0, self.size, self.size])
            if i == self.selected_draw_color_index:
                pygame.draw.rect(self.screen, [0, 0, 0], [i * self.size, 0, self.size, self.size], 8)

        
        pygame.display.update()
        self.clock.tick(60)


app = App()
while True:
    app.update()
    app.draw()