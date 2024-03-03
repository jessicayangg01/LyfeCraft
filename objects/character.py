import pygame.sprite
import assets

class Character(pygame.sprite.Sprite):

    # what do i need in character
    # .. etc

    def __init__(self, character, *groups):
        self.image = assets.get_sprites("infant")
        self.rect = self.image.get_rect(topleft =(20,70))

        # added
        # self.font = pygame.font.SysFont("Arial", 30)
        # self.blue = (0, 0, 128)
        # self.textSurf = self.font.render("Age: " + str(character.age), True, self.blue)
        # self.image.blit(self.textSurf, [20, 200])

        super().__init__(*groups)

        # which image
        self.switch = 0
        self.allAges = []
        for i in range(6):
            self.allAges.append("characterImage" + str(i))

    

    def update(self, character, *groups):
        # age += 1
        # if self.age == 2:
        if (character.age+1)%7 == 0:
            if self.switch < len(self.allAges):
                self.image = assets.get_sprites(self.allAges[self.switch])
                self.rect = self.image.get_rect(topleft =(20,70))
                self.switch += 1
        
        
        
        # self.textSurf = self.font.render("Age: " + str(character.age), True, self.blue)
        # self.image = assets.get_sprites(self.allAges[self.switch])
        # self.image.blit(self.textSurf, [20, 200])
        
    
# class CharacterStats(object):
#     def __init__(self):
#         self.age = 0
#         self.health = 0


    