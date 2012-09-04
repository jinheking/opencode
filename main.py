#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''

import opencode_lib.readJson
import opencode_lib 
def main():
    msg=opencode_lib.__abstract__ + opencode_lib.__version__
#    print unicode(msg,"utf-8").encode('gb18030')
    print msg
    
    readJson=opencode_lib.readJson(r'http://chart.chinacpw.com/index.php?s=/Opencode')
    dict=readJson.read()
#    print dict
    
    readClosed=opencode_lib.readClosed();
    if readClosed.judgeSpring()==False:
        readOpencode=opencode_lib.readOpencode(dict,readClosed.getYear())
        #readOpencode.getIssue('3D')
        db=opencode_lib.dbOperation(r'./config.ini')
        if db.judgeExist(str(readOpencode.getIssue('3D')), "3D"):
            db.dbInsert(readOpencode.get3D(),'3D')
        else:
            readJson.readLottery(r"3D",dict['3D'])
        if db.judgeExist(str(readOpencode.getIssue('P3')), "P3"):
            db.dbInsert(readOpencode.getP3(),'P3')
        #print readOpencode.getRandom(0,9,3,True)
        
        if readClosed.judgeSsqOpen():#判断是不是双色球的开机日
            if db.judgeExist(str(readOpencode.getIssue('SSQ')), "SSQ"):
                db.dbInsert(readOpencode.getSSQ(), "SSQ")
        if readClosed.judgeCjdltOpen():#判断是不是超级大乐透的开机日
            if db.judgeExist(str(readOpencode.getIssue('CJDLT')), "CJDLT"):
                db.dbInsert(readOpencode.getCJDLT(), "CJDLT")
    
if __name__ == '__main__':
     main()
     print "Over"