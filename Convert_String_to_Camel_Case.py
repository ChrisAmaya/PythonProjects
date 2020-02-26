def to_camel_case(text):
    """
    Purpose:
        Converts a string to a Camel Case version of itself
    Pre-Conditions:
        instead of spaces, if "Text" Param has dash/underscore
    Post-Conditions:
        String
    :return:
        String with Camel Case
    """

    Camel_version = ""

    for i in range(1, len(text)): # First letter case
        Camel_version += text[0]
        if str(i) == "-" or "_": # dash/Underscore case
            Camel_version += str(i+1).upper()
        else:  # regular letter case
            Camel_version += str(i).lower()
    return Camel_version




