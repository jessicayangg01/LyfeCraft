import pygame.sprite
import assets

class Game_Start(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("loading")
        self.rect = self.image.get_rect(topleft =(0,0))
        super().__init__(*groups)

    