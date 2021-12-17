import requests

domain = "Введите название сайта:  "


def get_subdom(subdomain):
    discovered_subdomains = []
    file = open("subdomains-1000.txt")
    content = file.read()
    subdomains = content.splitlines()

    # создать URL
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            # если возникает ОШИБКА, значит, субдомен не существует
            requests.head(url, timeout=5)
        except requests.ConnectionError:
            pass
            # если поддомена не существует, просто передать, ничего не выводить
        else:
            discovered_subdomains.append(url)
            print("[+] Обнаружен поддомен:", url)


get_subdom(domain)
