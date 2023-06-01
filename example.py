from objwrap import ClosedWrapper, wrapped


class Notify(ClosedWrapper):
    def __before__(self, method, args, kwargs):
        method, args, kwargs = super().__before__(method, args, kwargs)
        print(f"Calling {method.__name__} on {wrapped(self)} with args {args} and kwargs {kwargs}")
        return method, args, kwargs


x = Notify(1)
y = Notify(2)
z = x + y
print(wrapped(z))
