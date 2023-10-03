def callLimit(limit: int):

    """
    this function returns a decorator function.
    """

    count = 0
    def callLimiter(function):
        """decorator function, use function closures"""
        def limit_function(*args: any, **kwds: any):
            """a wrapper. by accepting args and kwargs, the
            decorator can work with functions that have diff
            numbers and types of arguments"""
            nonlocal count
            if count < limit:
                # make sure that the func receives the same arguments
                # it was originally called with
                res = function(*args, **kwds)  # unpack args and kwargs
                count += 1
                return res
            else:
                print(f"Error: {function} call too many times")
        return limit_function  # return the decorated function
    return callLimiter  # return the decorator itself
