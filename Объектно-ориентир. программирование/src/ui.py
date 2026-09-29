"""Интерфейс пользователя."""


class UI:
    """Абстракция над вводом/выводом."""

    def __init__(self):
        self._machine_3d_model = None

    def show_menu(self) -> None:
        print("=== WHACK-A-RAT ===")
        print("1. Начать игру")
        print("2. Настройки")
        print("3. Выход")

    def show_scoreboard(self, score: int, high_score: int) -> None:
        print(f"Счёт: {score} | Рекорд: {high_score}")

    def draw_hammer_animation(self) -> None:
        print("Удар!")

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def show_message(self, message: str) -> None:
        print(message)
