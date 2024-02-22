
class characterStats(object):
    def __init__(self):
        self.age = 0
        self.happiness = 0
    
    def ageUp(self, sprites):
        self.age+=1
        sprites.update()
        # if 3%self.age == 0:
        #     sprites.update()