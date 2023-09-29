def callLimit(limit: int):

    """
    this function returns a decorator function.
    """

    count = 0
    def callLimiter(function):
        """decorator function"""
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                res = function(*args, **kwds)
                count += 1
                return res
            else:
                print(f"Error: {function} call too many times")
        return limit_function  # return the decorated function
    return callLimiter  # return the decorator itself
