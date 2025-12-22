class Stack:
    def __init__(self):
        self._items = []

    def push(self, x: int) -> None:
        self._items.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
