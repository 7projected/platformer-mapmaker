import scenes, pygame, panel, random

class MainMenu:
    def __init__(self, scene_manager:scenes.SceneManager, base_mult, ratio):
        scene_manager.setup_scene(scenes.MAIN_MENU, self.update, self.draw)
        self.i = 0
        self.base_mult = base_mult
        self.base_screen_size = [ratio[0] * base_mult, ratio[1] * base_mult]
        self.ratio = ratio
        self.requested_mult = base_mult

        self.bg_color = [100.0, 100.0, 100.0]
        self.bg_color_default_item = 100
        self.bg_anim_index = 1
        self.bg_anim_add = True

        self.panels = [
            panel.Panel([0, 0], [self.base_screen_size[0] / 5, self.base_screen_size[1]], [255, 255, 255], 0, True, True, 2)
            
        ]

    def update(self, mult):
        self.requested_mult = mult
        self.screen_size = [self.ratio[0] * mult, self.ratio[1] * mult]

        self.bg_color[self.bg_anim_index] += 5

        
        if self.bg_color[self.bg_anim_index] == 255:
            default = self.bg_anim_index
            rng = self.bg_anim_index

            while rng == default:
                rng = random.randint(0, 2)
                self.bg_color[self.bg_anim_index] = self.bg_color_default_item
                self.bg_anim_index = rng
        

    def draw(self, surf:pygame.Surface):
        surf.fill(self.bg_color)

        for p in self.panels:
            p.draw(surf)