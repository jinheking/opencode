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


    def __init__(self):
        '''
        Constructor
        '''
    
    def read(self):
        url='http://chart.chinacpw.com/index.php?s=/Opencode'
        page=urllib.urlopen(url)
        json_data=page.read()
        dict=json.JSONDecoder().decode(json_data)['data']
        
        return dict;
        
        