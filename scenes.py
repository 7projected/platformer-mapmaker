import pygame

MAIN_MENU = 0
SPRITE_SELECT = 1
SPRITE_EDITOR = 2



class SceneManager:
    def __init__(self, base_mult, ratio):
        self.scene = 0
        self.display_mult = base_mult
        self.ratio = ratio
        self.surface = pygame.Surface([base_mult * ratio[0], base_mult * ratio[1]])
        self.update_callables :dict[callable]= {}
        self.draw_callables :dict[callable]= {}

    def setup_scene(self, scene:int, update:callable, draw:callable):
        self.update_callables[self.scene] = update
        self.draw_callables[self.scene] = draw

    def switch_to(self, scene:int):
        self.scene = scene
    
    def update(self):
        self.update_callables[self.scene](self.display_mult)

    def draw(self, surf:pygame.Surface):
        self.surface.fill([0, 0, 0])
        surf_size = surf.get_size()
        
        self.draw_callables[self.scene](self.surface)

        self.display_mult = surf_size[0] / self.ratio[0]
        draw_surf = pygame.transform.scale(self.surface, surf_size)
        surf.blit(draw_surf, [0, 0])

class Scene:
    def __init__(self, scene_manager:SceneManager, scene_num, base_mult, ratio, update, draw):
        scene_manager.setup_scene(scene_num, update, draw)
        self.base_mult = base_mult
        self.base_screen_size = [ratio[0] * base_mult, ratio[1] * base_mult]
        self.ratio = ratio
        self.requested_mult = base_mult