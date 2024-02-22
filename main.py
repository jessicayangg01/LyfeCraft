import pygame
import assets
import configs
from objects.background import Background
from objects.game_start import Game_Start
from objects.character import Character
from characterStats import characterStats


# from objects.background import Background

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()

# Background(sprites)
Game_Start(sprites)
unclicked = True

# add AGE event every few seconds
AGEEVENT = pygame.USEREVENT+1
t1 = 10000
pygame.time.set_timer(AGEEVENT, t1)

# add event every few seconds
OPPORTUNITYEVENT = pygame.USEREVENT+1
t2 = 5000
pygame.time.set_timer(OPPORTUNITYEVENT, t2)

# create Character
character = characterStats()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("CLICKED")
            if unclicked:
                unclicked = False
                Background(sprites)
                Character(sprites)
                            
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # do something with the clicked sprites..

            # maybe have another class for the events
        
        if event.type == AGEEVENT:
            print("AGED")
            character.ageUp(sprites)
        
        if event.type == OPPORTUNITYEVENT:
            print("NEW EVENT")
             
    screen.fill("pink")
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()