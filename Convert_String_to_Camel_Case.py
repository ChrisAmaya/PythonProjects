def to_camel_case(text):
    """
    Purpose:
        Converts a string to a Camel Case version of itself
    Pre-Conditions:
        instead of spaces, if "Text" Param has more then one word, use dash/underscore
    Post-Conditions:
        String
    :return:
        String with Camel Case
    """

    Camel_version = ""
    Camel_version += text[0]
    i = 1
    while i < (len(text)):
        if text[i] == "_":
            Camel_version = Camel_version + str(text[i+1]).upper()
            i += 2
        else:
            Camel_version = Camel_version + str(text[i]).lower()
            i += 1
    return Camel_version

print(to_camel_case("please_work"))


