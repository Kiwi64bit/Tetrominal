from random import sample
from typing import Any, Optional


class ShuffleBag:
    def __init__(self, items: Optional[list[Any]] = None) -> None:
        if items is None:
            items = []
        self._items: list[Any] = items
        self._bag: list[Any] = []

    def reset(self) -> None:
        self._bag = sample(self._items, len(self._items))

    def next(self, index: int = 0) -> Any:
        if self.is_empty():
            self.reset()
        return self._bag.pop(index)

    def peek(self, index: int = 0) -> Any:
        if self.is_empty():
            self.reset()
        return self._bag[index]

    def is_empty(self) -> bool:
        return len(self._bag) == 0


if __name__ == '__main__':
    bag: ShuffleBag = ShuffleBag([1, 2, 3, 4, 5, 6, 7])
    for i in range(100):
        print(bag.next())
