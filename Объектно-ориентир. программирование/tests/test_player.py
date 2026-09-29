"""Тесты класса Player."""

from unittest.mock import Mock
from src.player import Player
from src.rat import Rat


class TestPlayer:
    def test_initial_state(self):
        player = Player()
        assert player.lives == 3
        assert player.score == 0
        assert player.hammer_is_swinging is False

    def test_lose_life(self):
        player = Player(lives=3)
        player.lose_life()
        assert player.lives == 2

    def test_lose_life_not_below_zero(self):
        player = Player(lives=1)
        player.lose_life()
        player.lose_life()
        assert player.lives == 0

    def test_add_score(self):
        player = Player()
        player.add_score(50)
        assert player.score == 50

    def test_hit_rat_success(self):
        player = Player()
        rat = Rat(points=20)
        rat.pop_up()
        assert player.hit_rat(rat) is True
        assert player.score == 20

    def test_hit_rat_miss(self):
        player = Player()
        rat = Rat()
        assert player.hit_rat(rat) is False
        assert player.score == 0
