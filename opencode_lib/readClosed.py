#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''
import os
import json
import time
import datetime
class readClosed(object):
    '''
    classdocs
    '''
    dict={}
    todayWeek=0
    def __init__(self):
        '''
        Constructor
        '''
        file=open("./closed.json","r")
        strfile=file.readline()
        #print strfile
        self.dict=json.JSONDecoder().decode(strfile)['closed']
        file.close()
        today=self.readToday()
        self.todayWeek=today.weekday()+1
        #print self.dict
    def readYear(self):
        '''
        返回今天是那年
        '''
        today=datetime.date.today()
        return str(today)[0:4]
    
    def readToday(self):
        '''
        读取今天的日期
        '''
        today=datetime.date.today()
        return today
    
        
    def judgeSpring(self):
        '''
        判断是不是春节
        '''
       # print self.dict
        t=time.strptime(self.dict['begin'], "%Y-%m-%d")
        tBegin= datetime.date(t.tm_year,t.tm_mon,t.tm_mday)
        t1= self.readToday()-tBegin
        t=time.strptime(self.dict['end'], "%Y-%m-%d")
        tEnd= datetime.date(t.tm_year,t.tm_mon,t.tm_mday)
        t2=tEnd-self.readToday()
        if int(str(t1.days))>-1 and int(str(t2.days))>0:
            return True
        else:
            return False
    
    def judgeSsqOpen(self):
        '''
        一、三、五是双色球开机号创建日期
        '''
        list=[1,3,5] #等价于range(1,6,2)
        if self.todayWeek in list:
            return True
        else:
            return False
        
    def judgeCjdltOpen(self):
        '''
        二、四、日是超级大乐透开机号创建日期
        '''
        list=[2,4,7]
        if self.todayWeek in list:
            return True
        else:
            return False