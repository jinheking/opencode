#coding=utf-8 
'''
Created on 2012-8-20

@author: lenovo
'''
import sys
import MySQLdb
import MySQLdb.cursors
import ConfigParser
import time
class dbOperation(object):
    '''
    数据库操作类
    @author: eagle
    
    '''

    
    def __init__(self,filename):
        '''
        构造函数
        '''
        dict={}
        config = ConfigParser.ConfigParser()
        config.readfp(open(filename))
        dict['host'] = config.get("MySQL","host")
        dict['user'] = config.get("MySQL","user")
        dict[r'passwd'] = config.get("MySQL","passwd")
        dict['db'] = config.get("MySQL","db")
        dict['charset'] = config.get("MySQL","charset")
        self.conn= MySQLdb.connect(host=dict['host'],user=dict['user'],passwd=dict['passwd'],db=dict['db'],charset=dict['charset'],use_unicode=True,cursorclass = MySQLdb.cursors.DictCursor)
        
       
#        print self.cursor
    def getConn(self):
        '''
        取得Conn
        '''
        return self.conn
    
    def judgeExist(self,issue,type):
        '''
        判断开机号是否存在
        @param string issue:期号
        @param string type:类型
        @return: boolean  如果True就是要插入数据，如果False就不用继续操作了  
        '''
        cursor = self.conn.cursor()
        count = cursor.execute(r'select issue,type from cms_opencode where issue="'+issue+r'" AND type="'+type+r'"')
        cursor.close()
        if count==0:
            return True
        else:
            return False
#            records = self.cursor.fetchall()
#            for rs in records:
#                print rs['issue']

    def dbInsert(self,list,type):
        '''
        数据库插入操作
        '''
        cursor = self.conn.cursor()
        valdata=[]
        strsql = "insert into cms_opencode(`issue`,`number`,`type`,`characteristic`,`recommend`,`pubtime`) values (%s,%s,%s,%s,%s,%s)"
        valdata.append([
                       list['issue'],
                       list['number'],
                       type,
                       list['characteristic'],
                       list['strrecommend'],
                       time.strftime("%Y-%m-%d %X",time.localtime())
                       ])
        print valdata
        cursor.executemany(strsql, valdata)
        self.conn.commit()
        cursor.close()
#        self.conn.close()    
        