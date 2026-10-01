from typing import Sequence

from src.vector2 import Vector2
from src.shapes import PieceType, Shape, SHAPES


class Tetromino:
    def __init__(
            self,
            piece_type: PieceType,
            pos: Vector2 | Sequence[float] = (0, 0),
    ) -> None:
        self.type: PieceType = piece_type
        self.pos: Vector2 = Vector2(pos)
        self.shape: Shape = SHAPES[self.type]
        self.origin: Vector2 = Vector2(self.shape['origin'])
        self.blocks: list[Vector2] = []
        self.reset()

    def rotate(self) -> 'Tetromino':
        self.blocks = [
                ((block - self.origin).rotate_90() + self.origin)
                for block in self.blocks
        ]
        return self

    def move(self, dx: int, dy: int) -> 'Tetromino':
        self.pos += Vector2(dx, dy)
        return self

    def reset(self) -> 'Tetromino':
        self.blocks = [Vector2(block) for block in self.shape['blocks']]
        return self
