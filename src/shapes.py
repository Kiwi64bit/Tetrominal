from enum import IntEnum, auto
from typing import TypedDict


class PieceType(IntEnum):
    EMPTY = 0
    I = auto()
    J = auto()
    L = auto()
    O = auto()
    S = auto()
    T = auto()
    Z = auto()


class Shape(TypedDict):
    blocks: list[tuple[float, float]]
    origin: tuple[float, float]


SHAPES: dict[PieceType, Shape] = {
        PieceType.I: Shape(
                blocks=[(-1, 0), (0, 0), (1, 0), (2, 0)],
                origin=(0.5, 0.5),
        ),
        PieceType.J: Shape(
                blocks=[(-1, -1), (-1, 0), (0, 0), (1, 0)],
                origin=(0, 0),
        ),
        PieceType.L: Shape(
                blocks=[(-1, 0), (0, 0), (1, 0), (1, -1)],
                origin=(0, 0),
        ),
        PieceType.O: Shape(
                blocks=[(0, 0), (1, 0), (1, 1), (0, 1)],
                origin=(0.5, 0.5),
        ),
        PieceType.S: Shape(
                blocks=[(-1, 0), (0, 0), (0, -1), (1, -1)],
                origin=(0, 0),
        ),
        PieceType.T: Shape(
                blocks=[(-1, 0), (0, 0), (0, -1), (1, 0)],
                origin=(0, 0),
        ),
        PieceType.Z: Shape(
                blocks=[(-1, -1), (0, -1), (0, 0), (1, 0)],
                origin=(0, 0),
        ),
}
