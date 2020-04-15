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
#from six.moves import urllib
import os
import sys
#from email.policy import default

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
mkpaths=["Router_D321-drone\\",
        "FC\\",
        "AFPC\\",
        "TX2-yolov3_detector\\",
        "GMB\\",
        "TRA300-V40\\",
        "Cam-APP\\",
        "ESC-R7012\\",
        "TX2-Ros-xenial_aarch64\\",
        "ESC-R8016\\",
        "ESC-R7025\\",
        "AFPC\\",
        "GBOB_BOOTLOAD\\",
        "Gimbal-BL\\",
        "DroneHealth\\",
        "SERVO-BL\\",
        "TX2-Ros-xenial_x86_64_all\\",
        "TX2-videostreamer\\",
        "BEC-100V\\",
        "TX2-Ros-xenial_x86_64\\",
        "AFGC\\",
        "G50T\\",
        "TX2-pure_repeator\\",
        "ESC-BL\\",
        "ACRepeat\\",
        "TX2-kcf_tracker\\",
        "SERVO-KST\\",
        "TX2-perception_msgs\\",
        "TX2-Ros-win10_x86_64\\",
        "BEC-BL\\",
        "G51T\\",
        "Router_D321-tracker\\",
        "AIRDATA\\",
        "LinkHub\\"]
# 调用函数

for adir in mkpaths:
    adir = defaultRootPath+adir
    mkdir(adir)
    
    



def download_and_extract(filepath, save_dir):
    """
            根据给定的URL地址下载文件

    Parameter:
    filepath: list 文件的URL路径地址
    save_dir: str  保存路径
    Return:
None
""" 
"""   
    for url, index in zip(filepath, range(len(filepath))):
filename = url.split('/')[-1]
save_path = os.path.join(save_dir, filename)
urllib.request.urlretrieve(url, save_path)
sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
sys.stdout.flush()
    print('\nSuccessfully downloaded')


def _get_file_urls(file_url_txt):
    根据URL路径txt文件，获取URL地址列表

    Parameter:
file_url_txt: str  txt文件本地路径
    Return:
filepath: list  URL列表
    
    filepath = []
    file = open(file_url_txt, 'r')
    for line in file.readlines():
line = line.strip()
filepath.append(line)
    file.close()
    return filepath


if __name__ == '__main__':
    file_url_txt = 'file_url_txt.txt'
    save_dir = ''
    filepath = _get_file_urls(file_url_txt)
    download_and_extract(filepath, save_dir)
    
    """