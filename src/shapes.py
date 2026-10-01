from enum import IntEnum, auto


class PieceType(IntEnum):
    EMPTY = 0
    I = auto()
    J = auto()
    L = auto()
    O = auto()
    S = auto()
    T = auto()
    Z = auto()


SHAPES: dict[PieceType, list[tuple[float, float]]] = {
        PieceType.I: [(-1.5, -0.5), (-0.5, -0.5), (0.5, -0.5), (1.5, -0.5)],
        PieceType.J: [(-1, -1), (-1, 0), (0, 0), (1, 0)],
        PieceType.L: [(-1, 0), (0, 0), (1, 0), (1, 1)],
        PieceType.O: [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)],
        PieceType.S: [(-1, 0), (0, 0), (0, -1), (1, -1)],
        PieceType.T: [(-1, 0), (0, 0), (0, -1), (1, 0)],
        PieceType.Z: [(-1, -1), (0, -1), (0, 0), (1, 0)],
}
