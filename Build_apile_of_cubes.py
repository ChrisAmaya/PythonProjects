def find_nb(m):
    """
    purpose:
        Construct a building which will be a pile of cubes.
    pre-conditions:
        None
    post-conditions:
        None
    :param m:
        defines the total volume of the building
    :return:
        The integer n such as n^3 + (n-1)^3 + ... + 1^3 = m.
        Or -1 if there is no such n.
    """
    # m is something we refer to
    # find n in this function
    # example: if m is 8 then n is 2

    if 1 ** 3 == m:  # base case
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                return n
            else:
                n += 1
                continue
        return -1


