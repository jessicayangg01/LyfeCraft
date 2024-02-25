import pygame
import assets

class Text(pygame.sprite.Sprite):
    def __init__(self, text, *groups):        


        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
    
        self.font = pygame.font.SysFont("Arial", 12)
        # self.textSurf = self.font.render(text, 1, color)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        white = (255, 255, 255)

        self.image = pygame.Surface((200, 200))
        self.image.fill(white)

        # add text
        print(text)
        i = 50
        x = 0
        while i < len(text):
            currText = text[:i]
            self.textSurf = self.font.render(currText, True, green, blue)
            self.image.blit(self.textSurf, [0, x])
            print(currText)
            text = text[i:]
            x += 20
        self.textSurf = self.font.render(text, True, green, blue)
        self.image.blit(self.textSurf, [0, x])
            

        self.rect = self.image.get_rect(topleft =(50,50))
        super().__init__(*groups)


        # add yes and no
        self.image = assets.get_sprites("yes")
        self.rect = self.image.get_rect(topleft =(100,0))
        super().__init__(*groups)
        self.image = assets.get_sprites("no")
        self.rect = self.image.get_rect(topleft =(200,0))
        super().__init__(*groups)