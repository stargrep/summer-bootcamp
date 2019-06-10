def fibonacci(index):
    """
    fibonacci implementation in python, use recursion.
    (0), 1, 1, 2, 3, 5, 8, 13, 21, 34
    index 0 -> 0
    index 1 -> 1
    index 2 -> 1
    ...
    index 7 -> 13
    ...
    :param index: the i-th fibonacci number
    :return:
    """
    # when index < or == 0, value is 0
    if index < 1:
        return 0
    # when index == 1 or == 2, value is 1
    if index < 3:
        return 1
    # fibonacci function is current index = previous + the one before previous
    return fibonacci(index - 1) + fibonacci(index - 2)


print(fibonacci(9))  # should be 34
