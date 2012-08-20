#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''

import opencode_lib.readJson
import opencode_lib 
def main():
    print opencode_lib.__abstract__ + opencode_lib.__version__
    readJson=opencode_lib.readJson(r'http://chart.chinacpw.com/index.php?s=/Opencode')
    dict=readJson.read()
    print dict
    
    readClosed=opencode_lib.readClosed();
    if readClosed.judgeSpring()==False:
        readOpencode=opencode_lib.readOpencode(dict,readClosed.getYear())
        #readOpencode.getIssue('3D')
        readOpencode.get3D()
        readOpencode.getP3()
        #print readOpencode.getRandom(0,9,3,True)
        
        if readClosed.judgeSsqOpen():#判断是不是双色球的开机日
            print readOpencode.getSSQ()
        if readClosed.judgeCjdltOpen():#判断是不是超级大乐透的开机日
            print readOpencode.getCJDLT()
    
if __name__ == '__main__':
     main()