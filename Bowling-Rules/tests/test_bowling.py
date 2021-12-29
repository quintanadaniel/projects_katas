import unittest
from unittest import result
from frame import Frame
from player import Player
from game import Game
from decimos_frame import DecimoFrame

class TestFrame(unittest.TestCase):

    def setUp(self):
        self.frame = Frame()
        self.players = [Player(),Player()]
        #self.result_scoreGame = []
        self.decimo_frame = DecimoFrame()
    
    def testIsStrike(self):
        frame = [10]
        score_strike = self.frame.is_strike(frame)
        self.assertTrue(10,score_strike)

    def testIsSpare(self):
        frame = [4,6]
        score_spare = self.frame.is_strike(frame)
        self.assertTrue(10,score_spare)

    def testGetScoreFrame(self):
        result = self.frame.getScoreFrame(self.players)
        #print(result)


class TestGame(unittest.TestCase):

    def setUp(self):
        frames = [Frame(),Frame(),Frame(),Frame(),Frame(),Frame(),Frame(),Frame(),Frame(),DecimoFrame()]
        #players = [Player(),Player()]
        players = [Player()]
        self.game = Game(players,frames)

    def testLastFrame(self):
        result_game = self.game.score()
        

if __name__ == '__main__':
    unittest.main()