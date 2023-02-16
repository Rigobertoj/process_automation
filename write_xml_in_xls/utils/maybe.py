class Maybe():
    def __init__(self, value) -> None:
        self.value = value

    
    def bind(self, func):
        if self.value is not None :
            return Maybe(func(self.value ))
        else: 
            return Maybe(None)


def unit_maybe(value):
    return Maybe(value)


class  Result :
    def __init__(self, value, error) -> None:
        self.value = value
        self.error = error
    
    
    def __str__(self) -> str:
        return f"""
        value : {self.value} error : {self.error}"""


    def bind(self, func : callable):
        try:
            return func(self.value)
        except self.error:
            Result(None, self.error)


def unit_result(value, error):
    return Result(value, error)


