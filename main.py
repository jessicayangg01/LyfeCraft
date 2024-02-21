import pygame
import assets
import configs
from objects.background import Background
from objects.game_start import Game_Start
# from objects.background import Background

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()
# Background(sprites)
Game_Start(sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # added
        if event.type == pygame.MOUSEBUTTONUP:
            print("CLICKED")
            Background(sprites)
            
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # do something with the clicked sprites..
            # maybe have another class for the events
    
    screen.fill("pink")

    sprites.draw(screen)
    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()