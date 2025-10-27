import util, pygame, sys, texture

# first two bits (ff ff) are the size
# rest are pointers to indexs in a color palette  (one bit since 16 color pallete)

class App:
    def __init__(self):
        self.pal = util.Palette()
        self.pal.load_palette("purple")

        pygame.init() 

        self.sprite_size = [16, 16]
        self.pixel_size = 32
        self.sprite_position = [(1280 / 2) - ((self.sprite_size[0] * self.pixel_size) / 2),
                                (720 / 2) - ((self.sprite_size[1] * self.pixel_size) / 2)]
        self.sprite = texture.EditTx(self.sprite_position, self.sprite_size, self.pal, self.pixel_size)
        self.sprite.load_sprite_map("test", self.pal)

        self.clock = pygame.time.Clock()
        self.screen_size = [1, 1]

        self.screen = pygame.display.set_mode([1280, 720])
        self.size = 100
        self.selected_draw_color = self.pal.colors[0]
        self.selected_draw_color_index = 0

        self.lmb_pressed = False
        self.rmb_pressed = False

    def try_select_color(self):
        if pygame.mouse.get_pos()[1] <= self.size:
            num = pygame.mouse.get_pos()[0] / 100
            if num <= self.pal.color_count:
                self.selected_draw_color = self.pal.colors[int(num)]
                self.selected_draw_color_index = int(num)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.lmb_pressed = True
                    self.try_select_color()
                if event.button == 3:
                    self.rmb_pressed = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.lmb_pressed = False
                if event.button == 3:
                    self.rmb_pressed = False
        
        if self.lmb_pressed == True:
            self.sprite.draw_tile(self.selected_draw_color_index)
        
        if self.rmb_pressed == True:
            self.sprite.erase_tile()
                    

    def draw(self):
        self.screen.fill([0, 0, 0])

        for i, color in enumerate(self.pal.colors):
            pygame.draw.rect(self.screen, color, [i * self.size, 0, self.size, self.size])
            if i == self.selected_draw_color_index:
                pygame.draw.rect(self.screen, [0, 0, 0], [i * self.size, 0, self.size, self.size], 8)

        self.sprite.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60)


app = App()
while True:
    app.update()
    app.draw()