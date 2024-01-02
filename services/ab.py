from bs4 import BeautifulSoup
import requests



r = requests.get("https://www.perekrestok.ru/sitemap.xml")
xml = r.text

soup = BeautifulSoup(xml, 'xml')
sitemapTags = soup.find_all("sitemap")
res = []
for sitemap in sitemapTags:
    res.append((sitemap.findNext("loc").text, sitemap.findNext("lastmod", sitemap.findNext("priority")).text))

print(res)
