from lxml import html
import requests


def getQueryString(personInfo, queryTemplate, attr, idx) :
    return personInfo.replace("<id>", str(idx + 1)) + queryTemplate.replace("<attr>", attr)

def doScrape() :
    page = requests.get("https://podio.com/site/creative-routines")
    tree = html.fromstring(page.text)

    personInfo = '//div[@class="name"][<id>]/preceding-sibling::ul[@class="person"]'
    queryTemplate = '//li[contains(@class,"<attr>")]/@style'

    names = tree.xpath('//div[@class="name"]/text()')
    namesLength = len(names)

    for idx in range(namesLength):
        sleep = tree.xpath(getQueryString(personInfo, queryTemplate, "sleep", idx))
        sleepStyles = (names[idx], sleep)
        work = tree.xpath(getQueryString(personInfo, queryTemplate, "creative", idx))
        workStyles = (names[idx], work)
        leasure = tree.xpath(getQueryString(personInfo, queryTemplate, "food", idx))
        leasureStyles = (names[idx], leasure)
        exercise = tree.xpath(getQueryString(personInfo, queryTemplate, "exercise", idx))
        exerciseStyles = (names[idx], exercise)
        
        print sleepStyles

doScrape()
