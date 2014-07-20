from lxml import html
import requests

page = requests.get("https://podio.com/site/creative-routines")
tree = html.fromstring(page.text)

personInfo = '//div[@class="name"]/preceding-sibling::ul[@class="person"]'
queryTemplate = '//li[contains(@class,"<attr>")]/@style'

sleepStyles = tree.xpath(personInfo + queryTemplate.replace("<attr>","sleep"))
workStyles = tree.xpath(personInfo + queryTemplate.replace("<attr>","creative"))
leasureStyles = tree.xpath(personInfo + queryTemplate.replace("<attr>","food"))
exerciseStyles = tree.xpath(personInfo + queryTemplate.replace("<attr>","exercise"))

print leasureStyles
