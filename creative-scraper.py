from lxml import html
import requests

page = requests.get("https://podio.com/site/creative-routines")
tree = html.fromstring(page.text)

personInfo = '//div[@class="name"][<id>]/preceding-sibling::ul[@class="person"]'
queryTemplate = '//li[contains(@class,"<attr>")]/@style'

names = tree.xpath('//div[@class="name"]/text()')
namesLength = len(names)

for idx in range(namesLength):
    sleepStyles = tree.xpath(personInfo.replace("<id>",str(idx)) +
                             queryTemplate.replace("<attr>","sleep"))
    workStyles = tree.xpath(personInfo.replace("<id>",str(idx)) +
                            queryTemplate.replace("<attr>","creative"))
    leasureStyles = tree.xpath(personInfo.replace("<id>",str(idx)) +
                               queryTemplate.replace("<attr>","food"))
    exerciseStyles = tree.xpath(personInfo.replace("<id>",str(idx)) +
                                queryTemplate.replace("<attr>","exercise"))

    print names[idx]
    print sleepStyles
