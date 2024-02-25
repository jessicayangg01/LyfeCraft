import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, text, type, *groups):        


        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
        blue = (0, 0, 128)
        white = (255, 255, 255)


        
        self.image = pygame.Surface((200, 200))
        self.image.fill(white)

        self.font = pygame.font.SysFont("Arial", 30)
        self.textSurf = self.font.render(type, True, blue, white)
        self.image.blit(self.textSurf, [0, 2])

        self.font = pygame.font.SysFont("Arial", 12)

        # add text
        i = 48
        x = 40
        while i < len(text):
            currText = text[:i]
            self.textSurf = self.font.render(currText, True, blue, white)
            self.image.blit(self.textSurf, [0, x])
            text = text[i:]
            x += 20
        self.textSurf = self.font.render(text, True, blue, white)
        self.image.blit(self.textSurf, [0, x])
            

        self.rect = self.image.get_rect(topleft =(50,50))
        super().__init__(*groups)

    def die(self):
        if self.rect.x < 100:
            self.kill()