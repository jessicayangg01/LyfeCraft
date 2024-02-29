import pygame
import assets
import configs
from objects.background import Background
from objects.game_start import Game_Start
from objects.character import Character
from characterStats import characterStats

# buttons
from objects.yesButton import Yes_Button
from objects.noButton import No_Button
from objects.okButton import Ok_Button

# import stats bar
from objects.statBars import StatsBar

from objects.text import Text
from objects.actionEvent import getEvent
from objects.characterDisplay import CharacterText
from objects.characterAge import CharacterAge

from playsound import playsound


# audio
assets.load_audio()
playsound(assets.get_audio("backgroundMusic"), False)


# from objects.background import Background
pygame.init()
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()


# import sprites
assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()


# Background(sprites)
gameStart = Game_Start(sprites)
unclicked = True

# add AGE event every few seconds
AGEEVENT = pygame.USEREVENT+1
t1 = 10000
# pygame.time.set_timer(AGEEVENT, t1)

# add event every few seconds
OPPORTUNITYEVENT = pygame.USEREVENT+1
t2 = 15000
# pygame.time.set_timer(OPPORTUNITYEVENT, t2)

# create Character
character = characterStats()

# keeps track of events
currEvent = None
currEventYes = None
currEventNo = None
currEventBackground = None
aftermath = None
aftermathOk = None


# stats bars
# drawing bar
statsBars = {}
x = 300
for i in range(7):
    statsBars[i] = StatsBar(80, x, 200, 20, 100)
    x += 30
drawNow = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("CLICKED")
            
            if unclicked:
                unclicked = False
                Background(sprites)
                Character(character, sprites)
                CharacterText(0, "Jessica", sprites)
                CharacterAge(character, sprites)
                gameStart.die()
                drawNow = True
                pygame.time.set_timer(OPPORTUNITYEVENT, t2) 
                pygame.time.set_timer(AGEEVENT, t1)               

                            
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # print(clicked_sprites)
            # do something with the clicked sprites..

            # all the buttons clicked
            if currEventNo in clicked_sprites or currEventYes in clicked_sprites:
                if currEventNo in clicked_sprites:
                    playsound(assets.get_audio("badSound"), False)
                    # resume timer
                    pygame.time.set_timer(OPPORTUNITYEVENT, t2) 
                    pygame.time.set_timer(AGEEVENT, t1)   
                elif currEventYes in clicked_sprites:
                    playsound(assets.get_audio("goodSound"), False)
                    character.updateStat(currEvent, statsBars)
                    aftermath = Text(currEvent["Follow-up Event"], "UPDATE", sprites)
                    aftermathOk = Ok_Button(sprites)
                currEventNo.die()
                currEventYes.die()
                currEventBackground.die()
            
            if aftermathOk in clicked_sprites:
                playsound(assets.get_audio("goodSound"), False)
                aftermath.die()
                aftermathOk.die()

                # resume timer
                pygame.time.set_timer(OPPORTUNITYEVENT, t2) 
                pygame.time.set_timer(AGEEVENT, t1)   


                
            # maybe have another class for the events
        
        if event.type == AGEEVENT:
            character.ageUp(sprites)
        
        if event.type == OPPORTUNITYEVENT:
            # pause time
            pygame.time.set_timer(OPPORTUNITYEVENT, 0) 
            pygame.time.set_timer(AGEEVENT, 0)     



            # EventBox(sprites)
            playsound(assets.get_audio("eventSound"), False)
            currEvent = getEvent()
            currEventBackground = Text(currEvent["Event"], "OPPORTUNITY", sprites)
            currEventYes = Yes_Button(sprites)
            currEventNo = No_Button(sprites)


             
    screen.fill("pink")
    sprites.draw(screen)
    
    if drawNow:
        for i in statsBars:
            statsBars[i].draw(screen)
    
    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()