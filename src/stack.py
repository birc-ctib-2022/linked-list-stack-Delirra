"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.stack = None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        self.stack = Link(x, self.stack)

    def top(self) -> T:
        """Return the top of the stack."""
        return self.stack.head

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        res = self.stack.head
        self.stack = self.stack.tail
        return res

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        return self.stack is None

stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack)


