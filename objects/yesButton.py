import pygame.sprite
import assets

class Yes_Button(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("yes")
        self.rect = self.image.get_rect(topleft =(200,0))
        super().__init__(*groups)

    def die(self):
        if self.rect.x < 100:
            self.kill()