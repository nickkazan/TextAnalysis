import urllib
import json

from selenium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup


def grabData(username):
    instagramUrl = "https://www.instagram.com"
    mainUrl = instagramUrl + "/" + username + "/"
    #We need selenium to run Google Chrome and find the proper link
    driver = webdriver.Chrome("/Users/nickkazan/Desktop/Python Practice/chromedriver")
    driver.get(mainUrl)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    links = []
    for tag in soup.find_all(class_="v1Nh3 kIKUG _bz0w"):
        linkedTag = tag.find("a", href=True)
        links.append(linkedTag["href"])
    
    #Now dealing with the photo webpage to grab the comments
    rawComments = []
    comments = []
    for link in links:
        photoUrl = instagramUrl + link
        driver.get(photoUrl)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for tag in soup.find_all(class_="KlCQn G14m- EtaWk"):
            for textTags in tag.find_all("span"):
                text = textTags.get_text()
                rawComments.append(text)
    
    for comment in rawComments:
        individualWords = comment.split(' ')
        for word in individualWords:
            if word.startswith("@"):
                individualWords.remove(word)
        result = " ".join(individualWords)
        comments.append(result)

    dictDocuments = {}
    documents = []
    for a in range(len(comments)):
        tempDict = {}
        index = str(a)
        tempDict['id'] = index
        tempDict['text'] = comments[a]
        documents.append(tempDict)
    dictDocuments['documents'] = documents
    #pprint(dictDocuments)

    return dictDocuments
