from player import Player


class Frame:

    def __init__(self):
        self.p = []

    def is_strike(self,roll):
        return roll == 10

    def is_spare(self, rolls):
        return sum(rolls) == 10

    def getScoreFrame(self,players):
        for player in players:
            rollTry = 0
            rolls = []
            roll = 0
            while rollTry < 2:
                roll = player.roll(roll)
                rolls.append(roll)
                if self.is_strike(roll):
                    self.p.append({player.id:{'is_strike':rolls}})
                    break
                rollTry += 1
                
            if not self.is_strike(roll) and self.is_spare(rolls):
                self.p.append({player.id:{'is_spare':rolls}})
            
            if not self.is_strike(roll) and not self.is_spare(rolls):
                self.p.append({player.id:{'none':rolls}})
        return self.p



                
#players = [Player(),Player(),Player(),Player(),Player(),Player(),Player()]
#frame = Frame()
#result = frame.getScoreFrame(players)
#print(result)