#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''
import opencode_lib.readJson
import opencode_lib.readClosed
def main():
    readJson=opencode_lib.readJson()
    dict=readJson.read()
    print dict
    
    readClosed=opencode_lib.readClosed();
    print readClosed.readYear()
    print readClosed.dict['begin']
    
if __name__ == '__main__':
     main()