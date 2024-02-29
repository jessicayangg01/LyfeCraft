
class characterStats(object):
    def __init__(self):
        self.age = 0
        self.happiness = 20
        self.wealth = 20
        self.health = 20
        self.relationship = 20
        self.education = 20
        self.career = 20
        self.adventure = 20
   
    
    def ageUp(self, sprites):
        self.age+=1
        sprites.update(self)
    
    def updateStat(self, stats, statsBars):
        for i in stats:
            if i == "Wealth" and stats[i]+self.wealth >= 0 and stats[i]+self.wealth <= 100:
                self.wealth += stats[i]
                statsBars[1].hp = self.wealth
            elif i == "Health" and stats[i]+self.health >= 0  and stats[i]+self.wealth <= 100:
                self.health += stats[i]
                statsBars[2].hp = self.health
            elif i == "Relationship" and stats[i]+self.relationship >= 0  and stats[i]+self.health <= 100:
                self.relationship += stats[i]
                statsBars[3].hp = self.relationship
            elif i == "Education" and stats[i]+self.education >= 0  and stats[i]+self.education <= 100:
                self.education += stats[i]
                statsBars[4].hp = self.education
            elif i == "Career" and stats[i]+self.career >= 0 and stats[i]+self.career <= 100:
                self.career += stats[i]
                statsBars[5].hp = self.career
            elif i == "Adventure" and stats[i]+self.adventure >= 0 and stats[i]+self.adventure <= 100:
                self.adventure += stats[i]
                statsBars[6].hp = self.adventure
        self.happiness = sum([self.wealth, self.health, self.relationship, self.education, self.career, self.adventure])/6
        statsBars[0].hp = self.happiness


    