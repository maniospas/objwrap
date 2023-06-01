from objwrap.wrapper import Wrapper


class ClosedWrapper(Wrapper):
    def __before__(self, method, args, kwargs):
        args = [arg.__value__() if arg.__class__ == self.__class__ else arg for arg in args]
        kwargs = {k: arg.__value__() if arg.__class__ == self.__class__ else arg for k, arg in kwargs.items()}
        return method, args, kwargs

    def __after__(self, obj):
        return self.__class__(obj)

    def __wrapattr__(self, obj, name):
        ret = super().__wrapattr__(obj, name)
        if not callable(ret):
            return ret

        def method(*args, **kwargs):
            called_method, args, kwargs = self.__before__(ret, args, kwargs)
            return self.__after__(called_method(*args, **kwargs))
        return method
