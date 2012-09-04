#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''
import urllib
import json
class readJson(object):
    '''
    classdocs
    '''

    urllink=''
    def __init__(self,url):
        '''
        Constructor
        '''
        self.urllink=url
    
    def read(self):
#        url='http://chart.chinacpw.com/index.php?s=/Opencode'
        url=self.urllink
        page=urllib.urlopen(url)
        json_data=page.read()
        dict=json.JSONDecoder().decode(json_data)['data']
        
        return dict;
    
    def readLottery(self,type,issue):
         params = urllib.urlencode({'type':type,'issue':issue})      #这里组织参数
         print params
         sock = urllib.urlopen("http://chart.lottery.com/index.php?s=/Opencode/readlottery/", params)  # 发送请求，并把参数传过去
         html = sock.read()
         sock.close()
         print html
        
        