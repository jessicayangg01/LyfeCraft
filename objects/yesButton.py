import pygame.sprite
import assets

class Yes_Button(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("yes")
        self.rect = self.image.get_rect(topleft =(150,200))
        super().__init__(*groups)

    def die(self):
        self.kill()