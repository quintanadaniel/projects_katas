import unittest
from bowling_kata import Game


class BowlingTest(unittest.TestCase):

    def test_all_zero(self):
        game = Game()
        frames = '--------------------'
        score = game.score(frames)
        self.assertEqual(0, score)
    
    def test_all_ones(self):
        game = Game()
        frames = '11111111111111111111'
        score = game.score(frames)
        self.assertEqual(20,score)

    def test_a_spare(self):
        game = Game()
        frames = '1/111111111111111111'
        score = game.score(frames)
        self.assertEqual(29,score)

    def test_a_strike(self):
        game = Game()
        frames = 'X1111111111111111111'
        score = game.score(frames)
        self.assertEqual(30,score)