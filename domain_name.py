from urllib.parse import urlparse

def domain_name(str):

    domain = urlparse(str).hostname
    print(domain)
    

domain_name('https://www.google.com')