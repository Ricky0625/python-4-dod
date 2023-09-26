def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:

    """
    to demonstrate closure. a closure is a function that remember the
    environment in which it was created, including the variables and 
    values available at that time. it can be access and use these
    variables even after the outer function that created it has
    finished executing.
    """

    # local of outer, this will always be 0 when outer() is called
    count = 0

    def inner() -> float:

        """
        when this function returns from outer, it remembers the value of
        x & count
        """

        # make the count variable we use here not local in inner() only
        nonlocal count
        count += 1
        res = x
        for _ in range(count):
            res = function(res)
        return res
    return inner
