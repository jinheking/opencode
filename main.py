#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''

import opencode_lib.readJson
import opencode_lib 
def main():
    print opencode_lib.__abstract__ + opencode_lib.__version__
    readJson=opencode_lib.readJson()
    dict=readJson.read()
    print dict
    
    readClosed=opencode_lib.readClosed();
    if readClosed.judgeSpring()==False:
        #readOpencode=opencode_lib.readOpencode()
        print readClosed.judgeSsqOpen();#判断是不是双色球的开机日
        print readClosed.judgeCjdltOpen();#判断是不是超级大乐透的开机日
    
if __name__ == '__main__':
     main()