from typing import Sequence

from src.vector2 import Vector2
from src.shapes import SHAPES, PieceType


class Tetromino:
    def __init__(
            self,
            piece_type: PieceType,
            pos: Vector2 | Sequence[float] = (0, 0),
    ) -> None:
        self.type: PieceType = piece_type
        self.pos: Vector2 = Vector2(pos)
        self.original: list[tuple[float, float]] = SHAPES[self.type]
        self.shape: list[Vector2] = []
        self.reset()

    def rotate(self) -> 'Tetromino':
        self.shape = [block.rotate_90() for block in self.shape]
        return self

    def move(self, dx: int, dy: int) -> 'Tetromino':
        self.pos += Vector2(dx, dy)
        return self

    def reset(self) -> 'Tetromino':
        self.shape = [Vector2(block) for block in self.original]
        return self
