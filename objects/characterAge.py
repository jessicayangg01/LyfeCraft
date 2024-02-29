import pygame.sprite
import assets

class CharacterAge(pygame.sprite.Sprite):

    # what do i need in character
    # .. etc

    def __init__(self, character, *groups):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([640,640], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        # added
        self.font = pygame.font.SysFont("Arial", 30)
        self.blue = (0, 0, 128)
        self.textSurf = self.font.render("Age: " + str(character.age), True, self.blue)
        self.image.blit(self.textSurf, [150, 150])

        self.rect = self.image.get_rect(topleft =(0, 0))

        super().__init__(*groups)


    

    def update(self, character, *groups):
        # age += 1
        # if self.age == 2:
        self.image = pygame.Surface([640,640], pygame.SRCALPHA, 32)
        self.textSurf = self.font.render("Age: " + str(character.age), True, self.blue)
        self.image.blit(self.textSurf, [150, 150])
        
    
# class CharacterStats(object):
#     def __init__(self):
#         self.age = 0
#         self.health = 0

