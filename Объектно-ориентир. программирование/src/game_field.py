"""Игровое поле — набор норок и управление крысами."""

import random
from .hole import Hole
from .rat import Rat


class GameField:
    """Игровое поле с норками и крысами."""

    def __init__(self, holes_count: int = 9):
        self._holes_count = holes_count
        self._active_rats = []
        self._holes = []
        self.generate_holes(holes_count)

    @property
    def holes_count(self) -> int:
        return self._holes_count

    @property
    def active_rats(self) -> list:
        return self._active_rats.copy()

    def generate_holes(self, count: int) -> None:
        self._holes_count = count
        self._holes = []
        for i in range(count):
            x = (i % 3) * 100
            y = (i // 3) * 100
            self._holes.append(Hole(x, y))

    def spawn_rat(self, difficulty_level: int = 1) -> Rat | None:
        free_holes = [h for h in self._holes if not h.is_occupied]
        if not free_holes:
            return None
        hole = random.choice(free_holes)
        speed = 1.0 + difficulty_level * 0.2
        points = 10 * difficulty_level
        rat = Rat(speed=speed, points=points)
        rat.pop_up()
        hole.spawn_rat()
        self._active_rats.append({'rat': rat, 'hole': hole})
        return rat

    def update_field(self) -> None:
        to_remove = []
        for entry in self._active_rats:
            if not entry['rat'].is_visible:
                entry['hole'].free()
                to_remove.append(entry)
        for entry in to_remove:
            self._active_rats.remove(entry)

    def remove_rat(self, rat: Rat) -> None:
        for entry in self._active_rats:
            if entry['rat'] is rat:
                entry['hole'].free()
                self._active_rats.remove(entry)
                return
