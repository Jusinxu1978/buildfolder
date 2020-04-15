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

url = "http://nas.autoflight.com/deployment/product/v40-standard/beta/latest/latest/modules/"

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
defaultRootPath = "D:\\AutoFlight\\智能开发部\\整机软件发布\\V40\\V40-standard-v0.0.7-beta\\modules\\"

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

allUrl = FindAllUrl(url)
allUrl.getAllUrlInPage(allUrl.url)

count = 1

for link in allUrl.alllinks:
    
    print("link:"+link,count)
    count+=1
    
print(len(allUrl.alllinks))

for adir in allUrl.alllinks:
    filepath = adir + "RELEASENOTE.md"
    adirlist = adir.split("/")
    adir = adirlist[-2]
    adir = defaultRootPath+adir+"\\"
    print(adir)
    mkdir(adir)
    download_and_extract(filepath,adir)
    
    






    
