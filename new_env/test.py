from Wappalyzer import Wappalyzer, WebPage

wappalyzer = Wappalyzer.latest()


def getCms():
    webpage = WebPage.new_from_url("https://pgu.ru/")
    return "&".join(wappalyzer.analyze(webpage))


getCms()

