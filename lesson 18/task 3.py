class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                return result

        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                return result

        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, bool):
                return result
            if result.lower() == "true":
                return True
            if result.lower() == "false":
                return False
            return result

        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper



ty = TypeDecorators
print(ty.to_str("hello"))