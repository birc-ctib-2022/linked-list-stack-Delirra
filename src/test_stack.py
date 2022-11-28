"""Testing our stack implementation."""
from stack import(Link, Stack)


def test_stack_isEmpty() -> None:
    """I really hope you test your code."""
    stack = Stack()
    assert stack.is_empty() == True

    stack.push(1)
    assert stack.is_empty() == False

def test_stack_top() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 1
