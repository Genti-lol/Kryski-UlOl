"""Тесты класса GameField."""

from src.game_field import GameField


class TestGameField:
    def test_generate_holes(self):
        field = GameField(holes_count=5)
        assert field.holes_count == 5

    def test_spawn_rat(self):
        field = GameField(holes_count=9)
        rat = field.spawn_rat(difficulty_level=1)
        assert rat is not None
        assert rat.is_visible is True
        assert len(field.active_rats) == 1

    def test_spawn_rat_when_full(self):
        field = GameField(holes_count=1)
        field.spawn_rat()
        assert field.spawn_rat() is None

    def test_update_field(self):
        field = GameField(holes_count=9)
        rat = field.spawn_rat()
        rat.hide()
        field.update_field()
        assert len(field.active_rats) == 0
