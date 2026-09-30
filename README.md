# Tetrominal

A phenomenal terminal game, inspired by the popular game "Tetris", built using
`Python` and `curses` module.

## How to run the game?

This is A terminal game, so we'll be using the terminal.

### on Unix (Linux/macOS)

The curses module already comes with python on Unix-like systems.
All you need to do is to open the game directory in the terminal and run the
following command.

```bash
python3 main.py
```

### on windows

There is another version of the `curses` module called `windows-curses`, which
does not come with python, so we have to install it.
You can install it using python package
manager [pip](https://pip.pypa.io/en/stable/) using the following command.

```bash
pip install windows-curses
```

or

```bash
python3 -m pip install windows-curses
```

You can now open the game directory in the terminal and run the next command.

```bash
python main.py
```

## Gameplay

1. Control the pieces using arrow keys (Up to rotate, Left/Right to move, Down
   to soft drop).
2. The objective is to clear rows and get the highest score.
3. If there is no place for a new piece to spawn, you lose.

> Note: If the game crashes when starting it, make sure the terminal is big
> enough (25 rows, 12 columns).

## Features

* It's a fun game. what else do you want?
* Be careful, it's addictive.
* Irritating controls (that's a feature not a bug)

## What's next?

* A starting menu.
* Hold, hard drop, and next piece
* Difficulty progression.
* Better user interface
* High score tracker

If you have suggestions or modifications, I am more than happy to see them. you
can open an issue or a pull request.

Have fun!

Please TTC don't sue me :D

## License

[MIT](https://choosealicense.com/licenses/mit/)
