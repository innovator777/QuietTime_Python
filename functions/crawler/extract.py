import re
import word

def getMainTitle(soup):
    title = soup.find('div', style='display:inline; float:left; width:90%; padding-top:10px;')
    return title.text

def getAllVerse(soup):
    verse = soup.find('div', style='float:right; width:40%; display:inline;font-size:17px;text-align:right;letter-spacing:-1px;color:#868686;')
    return verse.text

def getPraise(soup):
    content_gray = soup.find_all('div', class_='content_gray')

    praise = ""
    for target in content_gray:
        if word.getPraiseWord() in target.text:
            praise = target.text

    return praise

def getHelper(soup):
    helper = ""
    content_gray = soup.find_all('div', class_='content_gray')

    for target in content_gray:
        if word.getHelperWord() in target.text:
            helper = target.text

    return helper

def getSummary(soup):
    summary = ""

    content_gray = soup.find_all('div', class_='content_gray')

    for target in content_gray:
        if word.getSummaryWord() in target.text:
            summary = target.text

    return summary

def getPrayer(soup):
    prayer = ""
    content_gray = soup.find_all('div', class_='content_gray')

    for target in content_gray:
        if word.getPrayerWord() in target.text:
            prayer = target.text

    return prayer

def getSubTitles(soup):
    result = list()
    bible_subtitle = soup.find_all('ul', class_='bible_subtitle')

    for target in bible_subtitle:
        if target.text not in subTitle:
            result.append(target.text)

    return result

def getScripture(soup):
    result = list()
    bible_con = soup.find_all('div', class_='bible_con')

    for target in bible_con:
        result.append(target.text.rstrip())

    return result


def getCommentary(soup):
    result = list()
    commentaryList = list()
    commentary = soup.find_all('div', style='padding:10px; letter-spacing:-0.5px;')
    for target in commentary:
        commentaryList.append(target.text)

    subTitleList = getSubTitles(soup)

    if len(commentaryList) == len(subTitleList):
        for i in range(0, len(commentaryList)):
            result.append(subTitleList[i])
            result.append(commentaryList[i])

    return result

def getMainText(soup):
    return arrangementMainText(getSubTitles(soup), getScripture(soup))


def arrangementMainText(subTitles, scriptures):
    result = list()
    for target in subTitleData:
        result.append(target)
        regex = re.compile(r'(\d+)~(\d+)')
        data = regex.search(target)
        if data :
            result.extend(extractVerses(data.group(1), data.group(2), scriptures))
        else :
            print("arrangementMainText Error")

    return result

def extractVerses(start, end, scriptures):
    resultList = list()
    regex = re.compile(r'(\d+)')
    for i in range(int(start), int(end) + 1):
        for target in scriptures:
            data = regex.search(target)
            if data :
                if int(data.group(1)) == i:
                    resultList.append(target)
            else :
                print("%d NONE Data" %(i))

    return resultList