"""Норка — место появления крысы."""


class Hole:
    """Норка на игровом поле."""

    def __init__(self, position_x: int, position_y: int):
        self._position_x = position_x
        self._position_y = position_y
        self._is_occupied = False

    @property
    def position_x(self) -> int:
        return self._position_x

    @property
    def position_y(self) -> int:
        return self._position_y

    @property
    def is_occupied(self) -> bool:
        return self._is_occupied

    def spawn_rat(self) -> None:
        self._is_occupied = True

    def free(self) -> None:
        self._is_occupied = False
