from lxml import html
import requests


def getQueryString(personInfo, queryTemplate, attr, idx) :
    return personInfo.replace("<id>", str(idx)) + queryTemplate.replace("<attr>", attr)

def doScrape() :
    page = requests.get("https://podio.com/site/creative-routines")
    tree = html.fromstring(page.text)

    personInfo = '//div[@class="name"][<id>]/preceding-sibling::ul[@class="person"]'
    queryTemplate = '//li[contains(@class,"<attr>")]/@style'

    names = tree.xpath('//div[@class="name"]/text()')
    namesLength = len(names)

    for idx in range(namesLength):
        sleepStyles = tree.xpath(getQueryString(personInfo, queryTemplate, "sleep", idx))
        workStyles = tree.xpath(getQueryString(personInfo, queryTemplate, "creative", idx))
        leasureStyles = tree.xpath(getQueryString(personInfo, queryTemplate, "food", idx))
        exerciseStyles = tree.xpath(getQueryString(personInfo, queryTemplate, "exercise", idx))

        print names[idx]
        print sleepStyles

doScrape()
