# objwrap

*Easy object wrapping in Python.*

This package enables creation of transparent objects that wrap
others already in memory. Basically, it offers a more sophisticated
view over `getattr` that hand-rewires object methods, including
magic methods (`__add__`, `__len__` etc).

## :rocket: Quickstart
First install the latest version of the package 
with `pip install --upgrade objwrap`.


<details>
<summary>Custom classes to wrap
attribute getters and magic methods.</summary>
<br>

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
</details>


<details>
<summary>Wrappers to transform inputs to method calls.</summary>
<br>

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
z = x + y  # a Notify object
print(wrapped(z))

# Calling __add__ on 2 with args [2] and kwargs {}
# 3
```
</details>



<details>
<summary>Wrappers around dicts that call methods for their values.</summary>
<br>

```python
from objwrap import ClosedWrapper, wrapped
from objwrap.closure import Pending

class RunOnValues(ClosedWrapper):
    def __init__(self, obj):
        super().__init__(obj)
        self.symbols = obj.keys()
    
    def __unknown__(self, obj, name, args, kwargs):
        _, args, kwargs = super().__before__(None, args, kwargs)  # convert other instances of RunOnValues to dicts
        assert isinstance(obj, dict)  # enforce the type
        pending = dict()
        for symbol in self.symbols:
            pending[symbol] = Pending(method=getattr(obj[symbol], name),
                                      args=[arg[symbol] for arg in args],
                                      kwargs={k: arg[symbol] for k, arg in kwargs.items()})
        return pending

x = RunOnValues({"a": 1, "b": 2})
y = RunOnValues({"a": 10, "b": 20})
z = x + y
print(wrapped(z))

# {'a': 11, 'b': 22}
```
</details>

