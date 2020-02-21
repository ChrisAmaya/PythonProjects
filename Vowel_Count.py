def getCount(str):
    """
    Purpose:
        Determines how many vowels are inside a string
    Pre-Condition:
        None
    Post-Condition:
        None
    :param str:
         any string
    :return:
         a integer (count) of vowels in the given string
    """
    num_vowels = 0
    for i in str:
        if i == "a":
            num_vowels += 1
        elif i == "e":
            num_vowels += 1
        elif i == "i":
            num_vowels += 1
        elif i == "o":
            num_vowels += 1
        else:
            num_vowels = num_vowels
    return num_vowels


