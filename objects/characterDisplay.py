import pygame

class CharacterText(pygame.sprite.Sprite):
    def __init__(self, age, name, *groups):        


        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
        blue = (0, 0, 128)

        self.age = age
        self.name = name


        
        self.image = pygame.Surface([640,640], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        self.font = pygame.font.SysFont("Arial", 30)
        self.textSurf = self.font.render(self.name, True, blue)
        self.image.blit(self.textSurf, [150, 90])

        self.font = pygame.font.SysFont("Arial", 15)

        statsList = ["Happiness", "Wealth", "Health", "Relationship","Education","Career","Adventure"]
        index = 300
        for i in statsList:
            self.textSurf = self.font.render(i, True, blue)
            self.image.blit(self.textSurf, [5, index])
            index += 30
            

        self.rect = self.image.get_rect(topleft =(0, 0))
        super().__init__(*groups)
    