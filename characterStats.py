
class characterStats(object):
    def __init__(self):
        self.age = 0
        self.happiness = 0
        self.wealth = 0
        self.health = 0
        self.relationship = 0
        self.education = 0
        self.career = 0
        self.adventure = 0
    
    def ageUp(self, sprites):
        self.age+=1
        if 3%self.age == 0:
            sprites.update()
    
    def updateStat(self, stats):
        for i in stats:
            if i == "wealth" and stats[i]+self.wealth >= 0:
                self.wealth += stats[i]
            elif i == "health" and stats[i]+self.health >= 0:
                self.health += stats[i]
            elif i == "relationship" and stats[i]+self.relationship >= 0:
                self.relationship += stats[i]
            elif i == "education" and stats[i]+self.education >= 0:
                self.education += stats[i]
            elif i == "career" and stats[i]+self.career >= 0:
                self.career += stats[i]
            elif i == "adventure" and stats[i]+self.adventure >= 0:
                self.adventure += stats[i]
        self.happiness = sum(self.wealth, self.health, self.relationship, self.education, self.career, self.adventure)/6


    