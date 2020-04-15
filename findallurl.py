import urllib.request
import re
from _ast import Try
# url = "http://nas.autoflight.com/deployment/product/v40-standard/beta/latest/latest/"
class FindAllUrl():
    def __init__(self,url):
        #connect to a URL
        self.url = url
        self.alllinks = []
    def getCurrentUrlInPage(self,url):
        try:
            website = urllib.request.urlopen(url)
        except:
            print("url open error")
        #read html code
        html = website.read()
    #     print(html)
        #use re.findall to get all the links
        newlinks = []
        links = re.findall('<a href=\".*?/\"', html.decode('utf-8'))
        links.remove('<a href="../"')
        for link in links:
            link = re.findall('"([^"]+)"', link)
            newlinks.append(link[0])
        return newlinks

    def getAllUrlInPage(self,url):
        links = self.getCurrentUrlInPage(url)
        if len(links) == 0:
            return
        else:
            for link in links:
                newUrl = url+link
                self.alllinks.append(newUrl)
                self.getAllUrlInPage(newUrl)
            
# allurl = FindAllUrl(url)
# allurl.getAllUrlInPage(allurl.url)
# 
# count = 1
# 
# for link in allurl.alllinks:
#     
#     print("link:"+link,count)
#     count+=1
#     
# print(len(allurl.alllinks))