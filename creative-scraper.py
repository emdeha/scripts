from lxml import html
import requests
import re


def getQueryString(personInfo, queryTemplate, attr, idx):
    return personInfo.replace("<id>", str(idx + 1)) + queryTemplate.replace("<attr>", attr)

def getHoursForActivity(activities):
    hours = 0.0
    for activity in activities :
        percentage = re.search('(?<=width: )\d*\.?\d*', activity).group(0)
        hours += (float(percentage) / 100.0) * 24.0
    return hours

def doScrape():
    page = requests.get("https://podio.com/site/creative-routines")
    tree = html.fromstring(page.text)

    personInfo = '//div[@class="name"][<id>]/preceding-sibling::ul[@class="person"]'
    queryTemplate = '//li[contains(@class,"<attr>")]/@style'

    names = tree.xpath('//div[@class="name"]/text()')
    namesLength = len(names)

    sleepStyles = []
    workStyles = []
    leasureStyles = []
    exerciseStyles = []

    for idx in range(namesLength):
        sleep = tree.xpath(getQueryString(personInfo, queryTemplate, "sleep", idx))
        sleepStyles.append((names[idx], getHoursForActivity(sleep)))

        work = tree.xpath(getQueryString(personInfo, queryTemplate, "creative", idx))
        workStyles.append((names[idx], getHoursForActivity(work)))

        leasure = tree.xpath(getQueryString(personInfo, queryTemplate, "food", idx))
        leasureStyles.append((names[idx], getHoursForActivity(leasure)))

        exercise = tree.xpath(getQueryString(personInfo, queryTemplate, "exercise", idx))
        exerciseStyles.append((names[idx], getHoursForActivity(exercise)))
        
    print "Sleep:"
    print '\n'.join(map(str, sleepStyles))
    print "Work:"
    print '\n'.join(map(str, workStyles))
    print "Leasure:"
    print '\n'.join(map(str, leasureStyles))
    print "Exercise:"
    print '\n'.join(map(str, exerciseStyles))

doScrape()
