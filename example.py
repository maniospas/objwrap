from objwrap import ClosedWrapper, wrapped
from objwrap.closure import Pending


class RunOnValues(ClosedWrapper):
    def __init__(self, obj):
        super().__init__(obj)
        self.symbols = obj.keys()

    def __unknown__(self, obj, name, args, kwargs):
        _, args, kwargs = super().__before__(None, args, kwargs)
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
