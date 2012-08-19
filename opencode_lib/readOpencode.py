#coding=utf-8 
'''
Created on 2012-8-19

@author: lenovo
'''

class readOpencode(object):
    '''
    读取开机号
    '''
    issues={}
    year=0

    def __init__(self,issues,year):
        '''
        Constructor
        @param dict issues:从json读取的上期个彩种的期号 
        @param integer year:今天是哪年  
        '''
        self.issues=issues
        self.year=year
        
    def getIssue(self,type):
        '''
        读取开机号
        @param string type:彩种 
        '''
            