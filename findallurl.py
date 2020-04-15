import urllib.request
import re
#connect to a URL
url = "http://nas.autoflight.com/deployment/product/v40-standard/beta/latest/latest/"
alllinks = []
def getCurrentUrlInPage(url):
    website = urllib.request.urlopen(url)
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
#     print(newlinks)
    return newlinks
# getCurrentUrlInPage(url)
def getAllUrlInPage(url):
 
    links = getCurrentUrlInPage(url)
    if len(links) == 0:
#         print("find leaf")
        return
    else:
        for link in links:
            newUrl = url+link
            alllinks.append(newUrl)
            getAllUrlInPage(newUrl)
            
getAllUrlInPage(url)

count = 1

for link in alllinks:
    
    print("link:"+link,count)
    count+=1
    
print(len(alllinks))