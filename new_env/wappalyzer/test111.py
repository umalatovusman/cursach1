from Wappalyzer import Wappalyzer, WebPage

wappalyzer = Wappalyzer.latest()
webpage = WebPage.new_from_url("https://pgu.ru/")
print(wappalyzer.analyze_with_categories(webpage)
