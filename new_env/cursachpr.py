import requests
from Wappalyzer import Wappalyzer, WebPage
import ssl, socket

# домен для поиска поддоменов
domain = "https://pgu.ru/"
# читать все поддомены
def get_cms(urls):
    result = {}
    cms_found = None
    wappalyzer = Wappalyzer.latest()
    try:
        webpage = WebPage.new_from_url(urls)
        result = wappalyzer.analyze_with_categories(webpage)
    except Exception as E:
        pass

    for key, key1 in result.items():
        for keys, values in key1.items():
            if values == ["cms"]:
                print("{0} : {1}".format(urls, key))
                cms_found = 1
                return urls + " : " + key
            else:
                cms_found = None
                continue
    if cms_found == None:
        return urls + " : No CMS"


print(get_cms(domain))

# список обнаруженных поддоменов

domain1 = "pgu.ru"


def get_certif(hostname):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.connect((hostname, 443))
        cert = s.getpeercert()

    subject = dict(x[0] for x in cert["subject"])
    issued_to = subject["commonName"]
    issuer = dict(x[0] for x in cert["issuer"])
    issued_by = issuer["commonName"]
    print(f"Сертификат SSL: {issued_by}")


get_certif(domain1)


def get_subdom(subdomain):
    discovered_subdomains = []
    file = open("subdomains-1000.txt")
    content = file.read()
    subdomains = content.splitlines()

    # создать URL
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain1}"
        try:
            # если возникает ОШИБКА, значит, субдомен не существует
            requests.head(url, timeout=5)
        except requests.ConnectionError:
            pass
            # если поддомена не существует, просто передать, ничего не выводить
        else:
            discovered_subdomains.append(url)
            print("[+] Обнаружен поддомен:", url)


print(get_subdom(domain))
