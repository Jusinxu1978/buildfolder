#coding=utf-8
"""
目标：提供一个函数能够从网上下载资源
输入：
    url列表
    保存路径
输出：
    保存到指定路径中的文件
要求：
    能够实现下载过程，即从0%到100%可视化
"""
# =====================================================
import urllib
import os
import sys
#from email.policy import default
from findallurl import FindAllUrl
from ntpath import split

url = "http://nas.autoflight.com/deployment/product/v40-standard/beta/latest/latest/"

def mkdir(path):

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        
        print(path+' 创建成功\n')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在\n')
        return False     
# 定义要创建的目录

defaultRootPath = "D:\\AutoFlight\\智能开发部\\整机软件发布\\V40\\"


# 调用函数
def download_and_extract(url, save_dir):
    """
            根据给定的URL地址下载文件

    Parameter:
    filepath: list 文件的URL路径地址
    save_dir: str  保存路径
    Return:
None
""" 

    filename = url.split('/')[-1]
    print(filename)
    save_path = os.path.join(save_dir, filename)
    print(url)
    print(save_path)
    try:
        urllib.request.urlretrieve(url, save_path)
#         sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
#         sys.stdout.flush()
    except Exception as e:
        print("Error occurred when downloading file, error message:")
        print(e)
    else:
        print(url+' Successfully downloaded\n')
        
"""
Description:
    find objStr and locate the string need changed, then use newStr to replace
"""        
def replaceStrInFile(file,objStr,newStr):
    return 0

allUrl = FindAllUrl(url)
# allUrl.getAllUrlInPage(allUrl.url)
defaultProjectPath = defaultRootPath + allUrl.projectName + "\\"
releaseNotesName = defaultProjectPath+"RELEASENOTES.md"
releaseConfigFile = defaultProjectPath + allUrl.configure
modulePath = defaultProjectPath+"modules\\"

count = 1

for link in allUrl.alllinks:
    
    print("link:"+link,count)
    count+=1
    
print(len(allUrl.alllinks))

#打开releasenote文件
#创建项目路径
if not os.path.exists(defaultProjectPath):
    mkdir(defaultProjectPath)
    print("make a dir as defaultProjectPath")
else:
    print("defaultProjectPath has existed")
    
#下载配置文件
configureFileUrl = url + allUrl.configure
print(configureFileUrl)
download_and_extract(configureFileUrl,defaultProjectPath)
    
if os.path.exists(releaseNotesName):
  os.remove(releaseNotesName)
  print("remove old releaseNotes file")
  
with open(releaseNotesName,'w') as releaseNotes:
    #写入文件头信息
    releaseNotes.write("# ** ReleaseNote **" + "\n")
    version = allUrl.projectName
    releaseNotes.write("# ** Version:" + version + " **"+"\n")
    #从configure文件中读取release time
    
    print(releaseConfigFile)
    with open(releaseConfigFile,'r') as doc:
        docStr = doc.read()
    strList = docStr.split('release_date: "')
    try:
        releaseTime = strList[1].split('+0800')[0] 
        print(releaseTime)
        releaseNotes.write("# ** "+releaseTime+" **"+"\n")
    except:
        print("get time error")
#     releaseNotes.write("============================================================================================"+"\n")
    
# doc.close()
#打开releaseNotesFile
with open(releaseNotesName,'r') as releaseNotes:
    releaseNotesStr = releaseNotes.read()

for dirUrl in allUrl.alllinks:
    fileUrl = dirUrl + "RELEASENOTE.md"
    adirlist = dirUrl.split("/")
    adir = adirlist[-2]
    filePath = modulePath+adir+"\\"
    print(filePath)
    mkdir(filePath)
    download_and_extract(fileUrl,filePath)
    mdFile = filePath + "RELEASENOTE.md"
    #读出该文件
#     print("读取："+mdFile)
    with open(mdFile,'r',encoding='UTF-8') as doc:
        docStr = doc.read()
    strList = docStr.split('### Summary')
    tempListForInsert = list(strList[0])
    tempListForInsert.insert(2,adir+' ')
    strList[0] = "".join(tempListForInsert)
    strValidate = strList[0]+'### Summary'+strList[1][0:strList[1].find('#')].rstrip('\n')+'\n'
#     print(strValidate)
    #获取此releasenote的时间以便做比较，不让重复的releasenote加入进来
    keyStr = strList[0].split('\n')
    print(keyStr[1])
    index=releaseNotesStr.find(keyStr[1])
    print("index:{}".format(index))
    if index == -1:
        #没有找到这条releasenote则添加进去
        releaseNotesStr = releaseNotesStr+ '\n'+strValidate
    else:
        #找到这条releasenote则只增加模块名字
        
        insertPostion = releaseNotesStr[0:index].rindex("#")+2
        tempListForInsert = list(releaseNotesStr)
        tempListForInsert.insert(insertPostion,adir+'/')
        print(insertPostion)
        releaseNotesStr = "".join(tempListForInsert)

with open(releaseNotesName,'w') as releaseNotes:
    releaseNotes.write(releaseNotesStr)
#     releaseNotes.write("\n============================================================================================")
#     try:
#         releaseTime = strList[1].split('+0800')[0] 
#         print(releaseTime)
#         releaseNotes.write("# ** "+releaseTime+" **"+"\n")
#     except:
#         print("get time error")
    #写入到releasenote中
    #关闭该文件
    
    





    
