class Game:

    def __init__(self):
        pass

    def score(self,frame_scores):
        score = 0
        rolls = 0
        for index, frame_score in enumerate(frame_scores):
            if rolls >= 20:
                break
            if frame_score == '/':
                score += self.is_spare(frame_scores, index)
            elif frame_score == 'X':
                score += self.is_strike(frame_scores, index)
            elif frame_score != '-':
                score += int(frame_score)
            rolls += 1
        return score

    def is_spare(self,frame_scores,index):
        return 10 - self.frame_value(frame_scores[index-1]) + self.frame_value(frame_scores[index + 1])

    def is_strike(self,frame_scores,index):
        if frame_scores[index+2] == '/':
            return 20
        return 10 + self.frame_value(frame_scores[index + 1]) + self.frame_value(frame_scores[index + 2])

    def frame_value(self,frame):
        if frame == 'X':
            return 10
        if frame == '-':
            return 0
        return int(frame)

#game = Game()
#frames = 'XXXXXXXXXX9/'
#print(game.score(frames))