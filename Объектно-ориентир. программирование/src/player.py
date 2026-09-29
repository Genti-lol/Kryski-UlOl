"""Игрок — управляет молотком и жизнями."""

from .rat import Rat


class Player:
    """Игрок в Whack-a-Rat."""

    def __init__(self, lives: int = 3):
        self._lives = lives
        self._hammer_is_swinging = False
        self._score = 0

    @property
    def lives(self) -> int:
        return self._lives

    @property
    def hammer_is_swinging(self) -> bool:
        return self._hammer_is_swinging

    @property
    def score(self) -> int:
        return self._score

    def hit_rat(self, rat: Rat) -> bool:
        self._hammer_is_swinging = True
        points = rat.get_hit()
        if points > 0:
            self.add_score(points)
            self._hammer_is_swinging = False
            return True
        self._hammer_is_swinging = False
        return False

    def lose_life(self) -> None:
        self._lives = max(0, self._lives - 1)

    def add_score(self, points: int) -> None:
        self._score += points
