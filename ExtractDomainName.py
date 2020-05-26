# Extract the domain name from a URL


def domain_name(url):
    """
    Purpose: to get the domain name from a URLO
    Pre: URL - must be a proper formatted URL as a string
    :return: Domain name from the URL as a string
    """
    # gets rid of http://
    url = url[7:]

    # gets rid of www.
    if url.startswith('www.'):
        url = url[4:]

    # gets rid of any extensions
    ext_start = url.find("/")
    if ext_start == -1:
        pass
    else:
        url = url[:ext_start]

    # gets rid of .com
    if url.endswith('.com'):
        url = url[:-4]

    return url


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))