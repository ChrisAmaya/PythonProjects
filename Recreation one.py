def list_squared(m, n):
    """
    Purpose:
        Find all integers between m and n whose sum of squared divisors is itself a square
    Pre:
        :param m: Positive integer equal to or larger then 1
        :param n: Positive integer larger then m
    :return:
        Array of lists where each list is the divisor with its corresponding squared divisors
        first is the number whose squared divisors is a square and then the sum of the squared divisors.
    """
    assert m <= n, 'Invalid Input'
    if m == 1 and n == 1:
        return [[1, 1]]
    else:

