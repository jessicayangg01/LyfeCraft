import pygame.sprite
import assets

class No_Button(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("no")
        self.rect = self.image.get_rect(topleft =(60,200))
        super().__init__(*groups)

    def die(self):
        self.kill()