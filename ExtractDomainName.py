# Extract the domain name from a URL


def domain_name(url):
    """
    Purpose: to get the domain name from a URLO
    Pre: URL - must be a proper formatted URL as a string
    :return: Domain name from the URL as a string
    """
    domain = url.split("://"[1].split("/")[0])
    return domain


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))