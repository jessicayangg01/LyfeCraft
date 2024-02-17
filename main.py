import pygame
import assets
import configs
from objects.background import Background
# from objects.background import Background

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()
Background(sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("pink")
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()