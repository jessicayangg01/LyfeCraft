import pygame.sprite
import assets

class Character(pygame.sprite.Sprite):

    # what do i need in character
    # .. etc

    def __init__(self, *groups):
        self.image = assets.get_sprites("tempCHARACTER")
        self.rect = self.image.get_rect(topleft =(0,0))
        super().__init__(*groups)

        # which image
        self.switch = 0
        self.allAges = []
        for i in range(6):
            self.allAges.append("characterImage" + str(i))

    

    def update(self, *groups):
        # age += 1
        # if self.age == 2:
        if self.switch < len(self.allAges):
            self.image = assets.get_sprites(self.allAges[self.switch])
            self.rect = self.image.get_rect(topleft =(0,0))
            self.switch += 1
        
    
# class CharacterStats(object):
#     def __init__(self):
#         self.age = 0
#         self.health = 0


    