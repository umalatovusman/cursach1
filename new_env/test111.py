from Wappalyzer import Wappalyzer, WebPage

domain = "https://pgu.ru/"


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
