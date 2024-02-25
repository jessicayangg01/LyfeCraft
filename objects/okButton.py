import pygame.sprite
import assets

class Ok_Button(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("ok")
        self.rect = self.image.get_rect(topleft =(85,200))
        super().__init__(*groups)

    def die(self):
        self.kill()