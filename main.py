import pygame, scenes
import main_menu

pygame.init()

def get_requested_screen_size():
    return [int(requested_ratio[0] * requested_mult),
             int(requested_ratio[1] * requested_mult)]

def setup_scenes(scene_manager, scene_dict):
    scene_dict[scenes.MAIN_MENU] = main_menu.MainMenu(scene_manager, requested_mult, requested_ratio)

requested_mult = 80.0
requested_ratio = [16, 9]
current_size = [1, 1]
scene_dict = {}

screen = pygame.display.set_mode([1, 1])
clock = pygame.time.Clock()
scene_manager = scenes.SceneManager(requested_mult, requested_ratio)

setup_scenes(scene_manager, scene_dict) 

scene_manager.switch_to(scenes.MAIN_MENU)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            if event.size[0] != current_size[0]:
                requested_mult = event.size[0] / requested_ratio[0]
            if event.size[1] != current_size[1]:
                requested_mult = event.size[1] / requested_ratio[1]

    if current_size != get_requested_screen_size():
            screen = pygame.display.set_mode(get_requested_screen_size(), pygame.RESIZABLE)
            current_size = get_requested_screen_size()

    scene_manager.update()    

    screen.fill((255, 255, 255)) # Fill with white
    scene_manager.draw(screen)

    clock.tick(60)
    pygame.display.update()
pygame.quit()
