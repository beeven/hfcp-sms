# -*- coding: utf-8 -*-

import clr

clr.AddReference("ImApiDotNet.dll")

import ImApiDotNet


class SMSService(object):
    """description of class"""
    def send(self,mobiles,content):
        apiclient = ImApiDotNet.APIClient()
        ret = apiclient.init("183.63.251.76","hfcp","hfcp123456","hfcpapi","mas") #183.63.251.76,192.168.101.222
        if ret != 0:
            raise Exception(ret)
        apiclient.sendSM(mobiles,content,0)
        apiclient.release()
    def sendSurvay(self,mobile,name):
        template = '尊敬的{0}：您在广州海关的业务已办结。为推动机关作风建设，请回复数字对服务给予评价：1满意2基本满意3不满意。'
        apiclient = ImApiDotNet.APIClient()
        ret = apiclient.init("183.63.251.76","hfcp","hfcp123456","hfcpapi","mas")
        if ret!=0:
            raise IOError(ret,"")
        apiclient.sendSM((mobile,),template.format(name),0)
        apiclient.release()

    @staticmethod
    def translateAPIError(errno):
        if errno == 0: 
            return "操作成功"
        elif errno == -1:  
            return "连接数据库出错" 
        elif errno == -2:
            return "数据库关闭失败"
        elif errno == -3: 
            return "数据库插入错误"
        elif errno == -4:
            return "数据库删除错误"
        elif errno == -5:
            return "数据库查询错误" 
        elif errno == -6:
            return "参数错误"
        elif errno == -7: 
            return "API 编码非法"
        elif errno == -8: 
            return "参数超长"
        elif errno == -9: 
            return "没有初始化或初始化失败"
        elif errno == -10:
            return  "API 接口处于暂停（失效）状态"
        elif errno == -11:
            return "短信网关未连接"
        else:
            return "{0}: Unknown error".format(errno)


if __name__=="__main__":
    try:
        sms = SMSService()
        sms.sendSurvay("18665559889","Beeven")
    except IOError as e:
        print e.errno, SMSService.translateAPIError(e.errno)