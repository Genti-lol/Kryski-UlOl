"""Тесты класса Game."""

from unittest.mock import Mock
from src.game import Game


class TestGame:
    def test_initial_state(self):
        game = Game()
        assert game.game_state == "menu"
        assert game.current_score == 0
        assert game.high_score == 0
        assert game.difficulty_level == 1
        assert game.is_sound_on is True

    def test_start_game(self):
        game = Game()
        game.start_game()
        assert game.game_state == "playing"

    def test_pause_game(self):
        game = Game()
        game.start_game()
        game.pause_game()
        assert game.game_state == "paused"

    def test_toggle_sound(self):
        game = Game()
        game.toggle_sound()
        assert game.is_sound_on is False
        game.toggle_sound()
        assert game.is_sound_on is True

    def test_update_difficulty(self):
        game = Game()
        game.update_difficulty()
        assert game.difficulty_level == 2

    def test_save_high_score(self):
        game = Game()
        game._current_score = 100
        game.save_high_score()
        assert game.high_score == 100

    def test_save_high_score_not_lower(self):
        game = Game()
        game._high_score = 200
        game._current_score = 100
        game.save_high_score()
        assert game.high_score == 200

    def test_run_with_mock_ui(self):
        ui = Mock()
        game = Game(ui=ui)
        game.run()
        assert game.game_state == "game_over"
        assert ui.show_message.called
