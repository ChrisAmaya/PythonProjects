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
    n = 1
    if n ^ 3 == m: # base case
        return n
    else:
        # TODO: figure out a way to add 1 to n each time (making it global maybe 
        n += 1
        find_nb(m)

