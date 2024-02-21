import pygame.sprite
import assets

class Character(pygame.sprite.Sprite):

    # what do i need in character
    # .. etc

    def __init__(self, *groups):
        self.image = assets.get_sprites("tempCHARACTER")
        self.rect = self.image.get_rect(topleft =(0,0))
        super().__init__(*groups)
    

    def state(self, *groups):
        # age += 1
        # if self.age == 2:
        self.image = assets.get_sprites("tempCHARACTER2")
        self.rect = self.image.get_rect(topleft =(0,0))

# class CharacterStats(object):
#     def __init__(self):
#         self.age = 0
#         self.health = 0


    