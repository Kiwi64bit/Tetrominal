import curses
import time
from typing import Sequence

from src.vector2 import Vector2
from src.grid import Grid
from src.randomizers.shuffle_bag import ShuffleBag
from src.tetromino import Tetromino
from src.shapes import PieceType


class Game:
    def __init__(self, grid_size: Sequence[int], key_bindings: dict) -> None:
        self.board: Grid = Grid(
                grid_size[0],
                grid_size[1],
                default=PieceType.EMPTY.value,
        )
        self.tetrominoes: list[Tetromino] = self._create_tetrominoes()
        self.bag: ShuffleBag = ShuffleBag(self.tetrominoes)
        self.active: Tetromino = self.spawn_piece()
        self.key_bindings: dict = key_bindings
        self.actions: dict = {
                'left'     : self.move_left,
                'right'    : self.move_right,
                'rotate'   : self.rotate,
                'soft_drop': self.soft_drop,
        }

        self.fall_time: float = 0.5
        self.last_fall: float = time.monotonic()
        self.score: int = 0
        self.game_over: bool = False
        self.paused: bool = False

    @staticmethod
    def _create_tetrominoes() -> list[Tetromino]:
        return [Tetromino(piece_type) for piece_type in PieceType if
                piece_type != PieceType.EMPTY]

    def tick(self) -> None:
        now: float = time.monotonic()
        if now - self.last_fall < self.fall_time:
            return
        self.last_fall = now
        if not self.move_down():
            self.handle_lock()

    def handle_lock(self) -> None:
        self.lock()
        cleared_lines: int = self.clear_lines()
        self.score += self.calculate_score(cleared_lines)
        self.active = self.spawn_piece()
        if not self.is_valid_state():
            self.handle_game_over()

    def handle_game_over(self) -> None:
        self.game_over = True

    def move(self, dx: int, dy: int) -> bool:
        self.active.move(dx, dy)
        if self.is_valid_state():
            return True
        self.active.move(-dx, -dy)
        return False

    def move_down(self) -> bool:
        return self.move(0, 1)

    def move_up(self) -> bool:
        return self.move(0, -1)

    def move_left(self) -> bool:
        return self.move(-1, 0)

    def move_right(self) -> bool:
        return self.move(1, 0)

    def rotate(self) -> bool:
        self.active.rotate()
        if self.is_valid_state():
            return True
        self.active.rotate()
        self.active.rotate()
        self.active.rotate()
        return False

    def soft_drop(self) -> bool:
        has_moved: bool = self.move_down()
        if has_moved:
            self.score += 1
        return has_moved

    def spawn_piece(self) -> Tetromino:
        piece: Tetromino = self.bag.next()
        piece.reset()
        piece.pos = Vector2(self.board.width // 2 - 1, 1)
        return piece

    def lock(self) -> None:
        for block in self.active.blocks:
            x, y = block + self.active.pos
            x, y = int(x), int(y)
            self.board[x, y] = self.active.type.value

    def clear_lines(self) -> int:
        new_data: list[list[int]] = [row for row in self.board.data if
                                     any(cell == 0 for cell in row)]
        cleared_lines: int = self.board.height - len(new_data)

        for _ in range(cleared_lines):
            new_data.insert(0, [0] * self.board.width)

        self.board.data = new_data
        return cleared_lines

    @staticmethod
    def calculate_score(cleared_lines: int) -> int:
        return {1: 40, 2: 100, 3: 300, 4: 1200}.get(cleared_lines, 0)

    def is_valid_state(self) -> bool:
        for block in self.active.blocks:
            x, y = block + self.active.pos
            x, y = int(x), int(y)
            if not self.board.is_inside(x, y) or self.board[x, y] != 0:
                return False
        return True

    def handle_input(self, key: int, can_move=True) -> None:
        if key == -1:
            return

        if key in (ord('p'), ord('P')):
            self.paused = not self.paused
            return

        if key in (ord('q'), ord('Q')):
            self.game_over = True
            return

        if not can_move:
            return

        action_name: str = self.key_bindings.get(key)
        action = self.actions.get(action_name)
        if action is not None:
            action()

    def render(self, stdscr: curses.window) -> None:
        buffer: Grid = Grid(self.board.width, self.board.height, ' ')

        # locked cells
        for y in range(self.board.height):
            for x in range(self.board.width):
                buffer[x, y] = '[]' if self.board[x, y] != 0 else '  '

        # active piece
        for block in self.active.blocks:
            x, y = block + self.active.pos
            x, y = int(x), int(y)
            if self.board.is_inside(x, y):
                buffer[x, y] = '[]'

        stdscr.erase()

        stdscr.addstr(0, 0, '┌' + '──' * buffer.width + '┐')
        for i, row in enumerate(buffer.data):
            stdscr.addstr(i + 1, 0, '│' + ''.join(row) + '│')
        stdscr.addstr(buffer.height + 1, 0, '└' + '──' * buffer.width + '┘')

        stdscr.addstr(buffer.height + 2, 1, f'Score: {self.score}\n')

        if self.game_over:
            stdscr.addstr(
                    buffer.height + 4,
                    1,
                    'GAME OVER! Press Space to exit.',
            )
        elif self.paused:
            stdscr.addstr(
                    buffer.height + 4,
                    1,
                    'Press Q to exit, or P to unpause.',
            )
        else:
            stdscr.addstr(
                    buffer.height + 4,
                    1,
                    'Press Q to exit, or P to pause.',
            )

        stdscr.refresh()

    def main(self, stdscr: curses.window):
        stdscr.nodelay(True)
        stdscr.keypad(True)
        curses.curs_set(0)
        while not self.game_over:
            key = stdscr.getch()
            self.handle_input(key, can_move=not self.paused)
            if not self.paused:
                self.tick()
            self.render(stdscr)
            time.sleep(0.016)  # ~60 FPS

        # last render
        self.render(stdscr)
        key = stdscr.getch()
        while key != ord(' '):
            key = stdscr.getch()
