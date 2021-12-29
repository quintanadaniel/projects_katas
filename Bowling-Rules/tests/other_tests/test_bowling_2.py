import unittest
from bowling_kata import Game


class TestBowlingKata(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    
    def testRollGame(self):
        self.roll_many(0,20)
        assert self.game.score() == 0


    def testAllOnes(self):
        self.roll_many(1,20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0,17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0,16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.roll_many(10,12)
        assert self.game.score() == 300

    def testAllSpare(self):
        self.roll_many(5,21)
        assert self.game.score() == 150
    
    def roll_many(self,rolls,pins):
        for i in range(rolls):
            self.game.roll(pins)