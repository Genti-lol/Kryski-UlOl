"""Крыса — цель игрока."""


class Rat:
    """Крыса, которая появляется из лунки."""

    def __init__(self, speed: float = 1.0, points: int = 10):
        self._is_visible = False
        self._speed = speed
        self._points = points

    @property
    def is_visible(self) -> bool:
        return self._is_visible

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def points(self) -> int:
        return self._points

    def pop_up(self) -> None:
        self._is_visible = True

    def hide(self) -> None:
        self._is_visible = False

    def get_hit(self) -> int:
        if not self._is_visible:
            return 0
        self._is_visible = False
        return self._points
