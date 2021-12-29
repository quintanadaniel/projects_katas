from bowling_kata import Game
import pytest


@pytest.fixture()
def game():
    game = Game()
    return game


def test_all_zero(game):
    frames = '--------------------'
    score = game.score(frames)
    assert 0 == score


def test_all_ones(game):
    frames = '11111111111111111111'
    score = game.score(frames)
    assert 20 == score


def test_a_spare(game):
    frames = '1/111111111111111111'
    score = game.score(frames)
    assert 29 == score


def test_a_strike(game): # revisar este caso
    frames = 'X1111111111111111111'
    score = game.score(frames)
    assert 31 == score


def test_a_spare_then_strike(game):
    frames = '1/X11111111111111111'
    score = game.score(frames)
    assert 49 == score


def test_three_strikes(game):
    frames = 'XXX11111111111111111'
    score = game.score(frames)
    assert 80 == score


def test_a_spare_with_zero(game):
    frames = '1/-11111111111111111'
    score = game.score(frames)
    assert 27 == score


def test_perfect_game(game):
    frames = 'XXXXXXXXXXXX'
    score = game.score(frames)
    assert 300 == score

def test_spare_at_end(game):
    frames = '-------------------/5'
    score = game.score(frames)
    assert 15 == score

def test_spare_perfect_game(game):
    frames = 'XXXXXXXXXX9/'
    score = game.score(frames)
    assert 290 == score