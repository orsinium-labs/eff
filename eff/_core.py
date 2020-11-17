from contextlib import ContextDecorator
from typing import Callable, Dict, List, Type


class StackError(ValueError):
    pass


class Stack:
    items: List['Effects']

    def __init__(self) -> None:
        self._items = []

    def _push(self, instance: 'Effects'):
        self._items.append(instance)

    def _drop(self) -> None:
        if not self._items:
            raise StackError('the stack is empty')
        del self._items[-1]

    def _head(self) -> 'Effects':
        if not self._items:
            raise StackError('the stack is empty')
        return self._items[-1]


class Meta(type):
    _stack: Stack

    def __new__(*args) -> Type['Effects']:
        effects = type.__new__(*args)
        effects._stack = Stack()
        return effects

    def __getattr__(cls: Type['Effects'], name: str) -> Callable:
        instance = cls._stack._head()
        return getattr(instance, name)


class Effects(ContextDecorator, metaclass=Meta):
    _stack: Stack

    def __init__(self, **kwargs: Dict[str, Callable]) -> None:
        self.__dict__.update(kwargs)

    def __enter__(self) -> 'Effects':
        self._stack._push(self)
        return self

    def __exit__(self, *exc) -> bool:
        self._stack._drop()
        return False
