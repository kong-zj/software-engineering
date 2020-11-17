import configparser # 配置文件模块 读写配置文件
from aip import AipBodyAnalysis
import joint
#import base64 #转码



""" 你的 APPID AK SK """
APP_ID = '22984220'
API_KEY = 'QfowbVxCoywxnpHVdVeouc56'
SECRET_KEY = 'rmuG3DAIdFk3f1fSMb3Y3vzLQo8CA8m0'

#client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)



class BaiDuAPI(object):
    #特殊 构造函数 初始化函数
    def __init__(self,filePath):
        target = configparser.ConfigParser()
        target.read(filePath,encoding='utf-8-sig')

        self.client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
     
    """ 读取图片 """
    def get_file_content(self,photoPath):
        with open(photoPath, 'rb') as fp:
            return fp.read()

    """ 主函数 """    
    def file_main(self,photoPath):   

        #转码
        #base64_data = base64.b64encode(photoPath)

        #img = self.get_file_content('{}'.format(photoPath))
        img = self.get_file_content('{}'.format(photoPath))
        """ 调用人体关键点识别 """
        #此处只能对一个人进行关键点识别
        #也就是说一个图片如果有好多人的话,只能标出一个人的关节特征
        #此处可以做修改,即进行把一张图所有人的关节特征都表达出来
        #------
        #print(self.client.bodyAnalysis(img))
        result = self.client.bodyAnalysis(img)['person_info'][0]['body_parts']
        jo = joint.Joint(result)
        jo.xunhun(photoPath)
        #print(result) 