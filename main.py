import curses
from src.tetrominal import Game


def main(stdscr: curses.window) -> None:
    game: Game = Game(
            grid_size=(10, 20),
            key_bindings={
                    curses.KEY_LEFT : 'left',
                    curses.KEY_RIGHT: 'right',
                    curses.KEY_UP   : 'rotate',
                    curses.KEY_DOWN : 'soft_drop',
            },
    )
    game.main(stdscr)


if __name__ == '__main__':
    curses.wrapper(main)
