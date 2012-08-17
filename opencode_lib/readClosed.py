#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''
import os
import json
import datetime
class readClosed(object):
    '''
    classdocs
    '''
    dict={}
    
    def __init__(self):
        '''
        Constructor
        '''
        file=open("./closed.json","r")
        strfile=file.readline()
        #print strfile
        self.dict=json.JSONDecoder().decode(strfile)['closed']
        file.close()
        #print self.dict
    def readYear(self):
        '''
        返回今天是那年
        '''
        today=datetime.date.today()
        return str(today)[0:4]
    
    def read(self):
        print dict
        today=datetime.date.today()
        print today