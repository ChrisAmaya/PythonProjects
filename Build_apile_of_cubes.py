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