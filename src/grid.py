from typing import Any


class Grid:
    def __init__(self, width: int, height: int, default: Any = None) -> None:
        self.width: int = width
        self.height: int = height
        self.data: list[list[Any]] = [[default] * width
                                      for _ in range(self.height)]

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def fill(self, value: Any) -> None:
        for y in range(self.height):
            self.data[y] = [value] * self.width

    def __getitem__(self, key: tuple[int, int]) -> Any:
        x, y = key
        x, y = int(x), int(y)
        return self.data[y][x]

    def __setitem__(self, key: tuple[int, int], value: Any) -> None:
        x, y = key
        x, y = int(x), int(y)
        self.data[y][x] = value

    def __str__(self) -> str:
        rows: list[str] = [' '.join(str(cell) for cell in row)
                           for row in self.data]
        grid_str: str = '\n'.join(rows)
        return grid_str


if __name__ == '__main__':
    grid: Grid = Grid(10, 20, '.')
    grid[5, 5] = '#'
    grid[5, 3] = '#'
    grid[5, 2] = '#'
    print(grid)
