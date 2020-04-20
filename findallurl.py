import urllib.request
import re
from _ast import Try
# url = "http://nas.autoflight.com/deployment/product/v40-standard/beta/latest/latest/"
class FindAllUrl():
    

    def getCurrentUrlInPage(self,modulesUrl):
        try:
            moduleswebsite = urllib.request.urlopen(modulesUrl)
        except:
            print("url open error")
        #read html code
        html = moduleswebsite.read()
    #     print(html)
        #use re.findall to get all the links
        newlinks = []
        links = re.findall('<a href=\".*?/\"', html.decode('utf-8'))
        links.remove('<a href="../"')
        for link in links:
            link = re.findall('"([^"]+)"', link)
            newlinks.append(link[0])
        return newlinks
    
     
    def getAllUrlInPage(self,modulesUrl):
        links = self.getCurrentUrlInPage(modulesUrl)
        if len(links) == 0:
            return
        else:
            for link in links:
                newUrl = modulesUrl+link
                self.alllinks.append(newUrl)
                self.getAllUrlInPage(newUrl)
            
    def __init__(self,url):
        #connect to a URL
        self.url = url
        self.modulesUrl = url + "modules/"
        print(self.modulesUrl)
        self.alllinks = []
        try:
            website = urllib.request.urlopen(url)
        except:
            print("url open error")
        #read html code
        html = website.read()
        links = re.findall('<a href=\".*?.yml\"', html.decode('utf-8'))
        link = re.findall('"([^"]+)"', links[0])
        self.configure= link[0]
        
        self.projectName = self.configure[0:-4]
        
        self.getAllUrlInPage(self.modulesUrl)
        
        print(self.url)
        print(self.modulesUrl)
        print(self.alllinks)
        print(self.configure)
        print(self.projectName)
        
        
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