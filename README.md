# Effects

## Usage

```python
from io import StringIO
from typing import Callable
import effects

class Eff(effects.Effects):
    show: Callable

# Use global effects manager in a function.
def greet(username: str):
    Eff.show(f'Hello, {username}!')

# Provide actual side-effects handlers
# for the project prod entry point.
def main():
    with Eff(show=print):
        greet('World')

# Mock side-effects in tests.
def test_greet():
    stream = StringIO()
    with Eff(show=stream.write):
        greet('World')
    stream.seek(0)
    assert stream.read() == 'Hello, World!'

if __name__ == '__main__':
    main()
```
