class Game:

    def __init__(self):
        self.rolls = []


    def roll(self, pins):
        self.rolls.append(pins)

    
    def score(self):
        score = 0
        rollIndex = 0
        for frameIndex in range(20):
            if self.is_strike(rollIndex):
                score += self.strike_score(rollIndex)
                rollIndex += 1
            elif (self.is_spare(rollIndex)):
                score += self.spare_score(rollIndex)
                rollIndex += 2
            else:
                score += self.frame_score(rollIndex)
            rollIndex += 2
        return score

    def is_spare(self,rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def is_strike(self,rollIndex):
        return self.rolls[rollIndex] == 10

    def spare_score(self,rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def strike_score(self,rollIndex):
        return 10 + self.rolls[rollIndex + 2] + self.rolls[rollIndex + 2]

    def frame_score(self,rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]