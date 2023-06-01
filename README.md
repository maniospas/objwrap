# objwrap

*Easy object wrapping for Python.*

## :rocket: Quickstart
Define custom classes that wrap object
attribute getters (including built-in getters
like `__add__`).

```python
from objwrap import Wrapper

class Notify(Wrapper):
    def __wrapattr__(self, obj, name):
        print(f"Accessing {name}")
        return super().__wrapattr__(obj, name)

x = Notify(1)
print(x+1)
# Accessing __add__
# 2
```

Define wrappers that also transform inputs and outputs of 
method calls.


```python
from objwrap import ClosedWrapper, wrapped


class Notify(ClosedWrapper):
    def __after__(self, obj):
        return Notify(obj)  # this is the default behavior
    
    def __before__(self, method, args, kwargs):
        method, args, kwargs = super().__before__(method, args, kwargs)
        print(f"Calling {method.__name__} on {wrapped(self)} with args {args} and kwargs {kwargs}")
        return method, args, kwargs


x = Notify(1)
y = Notify(2)
z = x + y
print(wrapped(z))

# Calling __add__ on 2 with args [2] and kwargs {}
# 3
```
