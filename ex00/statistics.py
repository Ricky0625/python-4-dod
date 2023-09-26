
"""
nums = [2, 5, 7, 1, 9]
print(nums) # [2, 5, 7, 1, 9]
print(*nums) # 2 5 7 1 9 (unpacking)

def order_pizza(size, *args):
    print(f"Ordered a {size} pizza.") # positional args
    print(args) # non keyword args (tuple)
    print(kwargs) # keyword args (dict)

order_pizza(5, "cheese", "bell pepper", tips="$4", delivery_time="30mins")

args and kwargs are special keyword which allows function to take variable
length argument. The name of the variable is not necessarily to be args or
kwargs, it can be whatever you like. but to use non keyword args, you need
to declare it as *name, and for keyword args, it should be **name.
"""


def is_num(arg):

    """
    check if an arg is either an int or float. bool is a subclass of int
    so technically it's an instance of int. so need to exclude it.
    """

    return isinstance(arg, (int, float)) and not isinstance(arg, bool)


def calculate_squared_diff_sum(data: tuple) -> float:

    """calculate the sum of squared difference"""

    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data)


def calculate_mean(data: tuple) -> float:

    """calculate mean"""

    return sum(data) / len(data)


def calculate_median(data: tuple) -> float:

    """calculate median"""

    n = len(data)

    # if number of data is odd, return the middle value
    if n % 2:
        return data[n // 2]

    # if number of data is even, return the average fo the middle two value
    mid_left = data[n // 2 - 1]
    mid_right = data[n // 2]
    return (mid_left + mid_right) / 2


def calculate_quartile(data: tuple) -> list[float]:

    """calculate quartile, 25% & 75% only"""

    q1 = float(data[len(data) // 4])
    q3 = float(data[len(data) // 4 * 3])
    return [q1, q3]


def calculate_std_deviation(data: tuple) -> float:

    """calculate standard deviation"""

    return calculate_variance(data) ** 0.5


def calculate_variance(data: tuple) -> float:

    """calculate variance"""

    return calculate_squared_diff_sum(data) / len(data)


def ft_statistics(*args: any, **kwargs: any) -> None:

    """
    takes in a variable length of args and calculate the Mean, Median,
    Quartile, Standard Deviation and Variance according to the **kwargs
    """

    try:
        if not all(is_num(arg) for arg in args):
            raise AssertionError("all non keyword args should be int or float")

        # operation dictionary
        OPERATION = {
            "mean": calculate_mean,
            "median": calculate_median,
            "quartile": calculate_quartile,
            "std": calculate_std_deviation,
            "var": calculate_variance
        }

        sorted_data = sorted(args)

        for opr in kwargs.values():
            operation_func = OPERATION.get(opr)
            if operation_func is None:
                continue
            if len(args):
                print(f"{opr} : {operation_func(sorted_data)}")
            else:
                print("ERROR")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
