"""Тесты класса Rat."""

from src.rat import Rat


class TestRat:
    def test_initial_state(self):
        rat = Rat()
        assert rat.is_visible is False
        assert rat.speed == 1.0
        assert rat.points == 10

    def test_pop_up(self):
        rat = Rat()
        rat.pop_up()
        assert rat.is_visible is True

    def test_hide(self):
        rat = Rat()
        rat.pop_up()
        rat.hide()
        assert rat.is_visible is False

    def test_get_hit_visible(self):
        rat = Rat(points=20)
        rat.pop_up()
        assert rat.get_hit() == 20
        assert rat.is_visible is False

    def test_get_hit_invisible(self):
        rat = Rat()
        assert rat.get_hit() == 0
