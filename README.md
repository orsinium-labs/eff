# Eff

Eff is a Python library to work with algebraic effects.

Algbraic effects are all side-effects of a piece of code, like reading a user input, writing a text on the screen, doing network requests, reading a file etc. Eff allows to easily handle such effects making the code cleaner and testing easier.

Features:

+ **Easy to understand**. You don't need to read long scientific papers to understand how to use the library and what it does.
+ **Easy to integrate**. If you decided to add a logger into a function, changes will be minimal, no need to pass the logger down through the whole call stack.
+ **Fast**. The classic approach for handling algebraic effects is using coroutines or exceptions. This library uses global shared state instead which doesn't require to unwrap the whole call stack at runtime.
+ **Type-safe**. Effect handlers container is just a class. Annotate effect handlers type to make their usage type-safe.

## Installation

```bash
python3 -m pip install --user eff
```

## Usage

```python
from io import StringIO
from typing import Callable

import eff

class Eff(eff.ects):
    show: Callable

# Use global effects manager in a function.
def greet(username: str) -> None:
    Eff.show(f'Hello, {username}!')

# Provide actual side-effects handlers
# for the project prod entry point.
def main() -> None:
    with Eff(show=print):
        greet('World')

# Mock side-effects in tests.
def test_greet() -> None:
    stream = StringIO()
    with Eff(show=stream.write):
        greet('World')
    stream.seek(0)
    assert stream.read() == 'Hello, World!'

if __name__ == '__main__':
    main()
```

## Further reading

You don't have to read it but it's a good reading for better understanding of the motivation behind the library.

+ [Why PLs Should Have Effect Handlers](https://robotlolita.me/diary/2018/10/why-pls-need-effects/)
+ [Algebraic Effects for the Rest of Us](https://overreacted.io/algebraic-effects-for-the-rest-of-us/)
+ [What does algebraic effects mean in FP?](https://stackoverflow.com/a/57280373)
+ [Eff programming language](https://www.eff-lang.org/)
