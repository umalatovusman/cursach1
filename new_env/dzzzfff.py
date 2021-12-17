import ssl, socket
from Wappalyzer import Wappalyzer, WebPage
import requests

domain = input("Введите название сайта:  ")


def get_certif(hostname):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            cert = s.getpeercert()
    except Exception as E:
        pass
        # print(cert)
    subject = dict(x[0] for x in cert["subject"])
    issued_to = subject["commonName"]
    issuer = dict(x[0] for x in cert["issuer"])
    issued_by = issuer["commonName"]
    orgname = issuer["organizationName"]
    dateof_iss = cert["notBefore"]
    dateof_end = cert["notAfter"]

    print(
        f"\nСертификат SSL {issued_to}: {issued_by} \nВыдан организацией: {orgname}\nДата выдачи:{dateof_iss}\nДействителен до {dateof_end} "
    )


get_certif(domain)

# from Wappalyzer import Wappalyzer, WebPage

# domain = input("Введите название сайта:  ")
