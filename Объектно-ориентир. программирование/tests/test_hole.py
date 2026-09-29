"""Тесты класса Hole."""

from src.hole import Hole


class TestHole:
    def test_initial_state(self):
        hole = Hole(10, 20)
        assert hole.position_x == 10
        assert hole.position_y == 20
        assert hole.is_occupied is False

    def test_spawn_rat(self):
        hole = Hole(0, 0)
        hole.spawn_rat()
        assert hole.is_occupied is True

    def test_free(self):
        hole = Hole(0, 0)
        hole.spawn_rat()
        hole.free()
        assert hole.is_occupied is False
