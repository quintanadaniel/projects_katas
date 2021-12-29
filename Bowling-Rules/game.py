from frame import Frame
from player import Player


class Game:

    def __init__(self,players,frames):
        self.players = players
        self.frames_game = frames
        self.score_by_player = {}


    def roll(self,pins:int):
        pass

    def score(self):
        score_game_frames = []
        scores = 0
        id=0
        for frame in self.frames_game:
            score_game_frames.append(frame.getScoreFrame(self.players))

        long_lista = len(score_game_frames)
        for i in range(long_lista):
            score=0
            for j in score_game_frames[i]:
                
                for k,v in j.items():
                    scoref=0
                    id=k
                    print(k, v)
                    if j[k].get('is_strike') and (i+1)<long_lista:
                        scoref=j[k].get('is_strike')[0]
                        next_frame=score_game_frames[i+1]
                        score_next_frame = 0
                        for n in next_frame:
                            _player =n[k]
                            if _player:
                                for v in _player.values():
                                    score_next_frame=sum(v)
                        scoref += score_next_frame
                        

                    if j[k].get('is_spare') and (i+1)<long_lista:
                        score=sum(j[k].get('is_spare'))
                        next_frame=score_game_frames[i+1]
                        score_next_frame = 0
                        for n in next_frame:
                            _player =n[k]
                            if _player:
                                for v in _player.values():
                                    score_next_frame=v[0]
                        scoref += score_next_frame
                        

                    if j[k].get('none'):
                        scoref=sum(j[k].get('none'))

                    score+=scoref
                    
            if id in self.score_by_player:
                self.score_by_player[id]+=score
            else:
                self.score_by_player[id]=score
                    
                #if 
        #for player in score_game_frames:
        #    for k,v in player.items():
        #        if player[k].get('is_strike'):
        #            next_strike = player[k].get('is_strike')[0]
        #            scores += 10 + player[k].get('is_strike')[0] + next_strike
        #        if player[k].get('is_spare'):
        #            next_spare = player[k].get('is_spare')[1]
        #            scores += 10 - sum(player[k].get('is_spare')) + next_spare
        #        if player[k].get('none'):
        #            scores += sum(player[k].get('none'))
        #        self.score_by_player[k] = scores
        print('------',self.score_by_player)
        return self.score_by_player