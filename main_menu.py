import scenes, pygame, panel, random

class MainMenu(scenes.Scene):
    def __init__(self, scene_manager:scenes.SceneManager, base_mult, ratio):
        super().__init__(scene_manager, scenes.MAIN_MENU, base_mult , ratio, self.update, self.draw)
        
        self.scene_manager = scene_manager
        self.bg_color = [0, 0, 0]
        self.bg_color_default_item = 0
        self.bg_anim_index = 1
        self.anim_speed = 0.5

        main_panel_size = 256
        button_height = 32

        self.panels = [
            panel.Panel([0, 0], [main_panel_size, self.base_screen_size[1]], [255, 255, 255], [0, 0, 0], True, True, 2),
            panel.Button(self.switch_to_sprite_scene, self.scene_manager.font, "Sprite Select", [16, 16], [main_panel_size - 32, button_height], [0, 0, 0], [255, 255, 255], [0, 0, 0], True, True, 2)
        ]

    def update(self, mult):
        self.requested_mult = mult
        self.screen_size = [self.ratio[0] * mult, self.ratio[1] * mult]

        self.bg_color[self.bg_anim_index] += self.anim_speed

        for panel in self.panels:
            panel.update(self.scene_manager.mouse_pos)

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

    def switch_to_sprite_scene(self):
        print("CALLLL")
        self.scene_manager.switch_to(scenes.SPRITE_SELECT)