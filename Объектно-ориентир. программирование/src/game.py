"""Игра Whack-a-Rat — управление игровым циклом."""

from .ui import UI
from .player import Player
from .game_field import GameField


class Game:
    """Управляет игровым процессом Whack-a-Rat."""

    def __init__(self, ui: UI | None = None):
        self._high_score = 0
        self._current_score = 0
        self._game_state = "menu"
        self._difficulty_level = 1
        self._is_sound_on = True
        self._ui = ui if ui is not None else UI()
        self._field = GameField(holes_count=9)
        self._player = Player(lives=3)

    @property
    def high_score(self) -> int:
        return self._high_score

    @property
    def current_score(self) -> int:
        return self._current_score

    @property
    def game_state(self) -> str:
        return self._game_state

    @property
    def difficulty_level(self) -> int:
        return self._difficulty_level

    @property
    def is_sound_on(self) -> bool:
        return self._is_sound_on

    def start_game(self) -> None:
        self._game_state = "playing"
        self._current_score = 0
        self._player = Player(lives=3)
        self._field = GameField(holes_count=9)
        self._ui.show_message("Игра началась! Ударьте крысу!")

    def pause_game(self) -> None:
        if self._game_state == "playing":
            self._game_state = "paused"
            self._ui.show_message("Пауза")

    def restart_game(self) -> None:
        self.start_game()

    def toggle_sound(self) -> None:
        self._is_sound_on = not self._is_sound_on
        status = "включён" if self._is_sound_on else "выключен"
        self._ui.show_message(f"Звук {status}")

    def update_difficulty(self) -> None:
        self._difficulty_level += 1
        self._ui.show_message(f"Уровень сложности: {self._difficulty_level}")

    def save_high_score(self) -> None:
        if self._current_score > self._high_score:
            self._high_score = self._current_score

    def run(self) -> None:
        self.start_game()
        for _ in range(3):
            rat = self._field.spawn_rat(self._difficulty_level)
            if rat:
                hit = self._player.hit_rat(rat)
                if hit:
                    self._ui.draw_hammer_animation()
                    self._current_score = self._player.score
                    self._ui.show_scoreboard(
                        self._current_score, self._high_score
                    )
                else:
                    self._player.lose_life()
                    self._ui.show_message("Промах! Потеряна жизнь.")
            self._field.update_field()
        self._game_state = "game_over"
        self.save_high_score()
        self._ui.show_message(
            f"Игра окончена! Счёт: {self._current_score}, "
            f"Рекорд: {self._high_score}"
        )
