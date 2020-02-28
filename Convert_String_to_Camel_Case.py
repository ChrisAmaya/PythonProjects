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
    Camel_version = Camel_version + text[0]
    for i in range(len(text)-1):  # First letter case
        if str(i) == "-" or "_":  # dash/Underscore case
            Camel_version = Camel_version + str(text[i+1]).upper()
        else:  # regular letter case
            Camel_version = Camel_version + str(text[i]).lower()
    return Camel_version

print(to_camel_case("please_work"))


