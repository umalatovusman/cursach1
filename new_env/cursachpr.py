import requests
from Wappalyzer import Wappalyzer, WebPage
# домен для поиска поддоменов
domain = "pgu.ru"
# читать все поддомены
file = open("subdomains-1000.txt")
# прочитать весь контент
content = file.read()
# разделить на новые строки
subdomains = content.splitlines()
# список обнаруженных поддоменов
discovered_subdomains = []

for subdomain in subdomains:
    # создать URL

    url = f"http://{subdomain}.{domain}"
    try:
        # если возникает ОШИБКА, значит, субдомен не существует
        requests.head(url, timeout=5)
    except requests.ConnectionError:
        # если поддомена не существует, просто передать, ничего не выводить
        pass
    else:
        print("[+] Обнаружен поддомен:", url)
        discovered_subdomains.append(url)


wappalyzer = Wappalyzer.latest()
webpage = WebPage.new_from_url(domain)
print(wappalyzer.analyze_with_categories(webpage)