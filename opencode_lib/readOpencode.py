#coding=utf-8 
'''
Created on 2012-8-19

@author: lenovo
'''
import random
class readOpencode(object):
    '''
    读取开机号
    '''
    issues={}
    year=''

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
        y= str(int(self.issues[type]))[0:4]
        if self.year==y:
            return  int(self.issues[type])+1
        else:
            return int(self.year+'001') 
    def getRandom(self,begin,end,count,repeat=False,sort=False):
        '''
        @param int begin:随机数开始的数量
        @param int end: 随机数结束
        @param int count:得到几个随机数  
        @param boolean repeat:是否可以重复
        @param boolean sort:是否排序 
        '''
        list=[]
        if repeat:
            for i in range(0,count):
                list += range(begin,end+1)
        else:
            list = range(begin,end+1)
#        list.append(range(begin,end))
#        print list 
        #for i in range(0,100):
        slice = random.sample(list, count)
        if sort:
            slice=sorted(slice)
        
        return slice
#        list = ["01","02","03","04","05","06","07","08","09","10","11",
#        "11","12","13","14","15","16","17","18","19","20","21",
#        "21","22","23","24","25","26","27","28","29","30","31",
#        "32","33"]
#        get_array = random.sample(list,6)
#        
    def getJO(self,list):
        '''
        @param list list:传过来的数组
        返回是奇数还是偶数 
        '''
        result=''
        for  n in list:
            if n % 2 == 0:
                result+= '偶-'
            else:
                result+="奇-"
        return result[0:-1]
    
    
    def getDX(self,list,bigNumber):
        '''
        @param list list:传过来的数组
        @param int bigNumber
        返回是大数还是小数 
        '''
        result=''
        for  n in list:
            if n >=bigNumber:
                result+= '大-'
            else:
                result+="小-"
        return result[0:-1]
    
    
    def getSum(self,list):
        result=0
        for  n in list:
            result+=n
        return result
    
    def getRecomend(self,list,bit=1):
        '''
               取得推荐数组
        @param list list:和值数组
        @return: 返回字符串
        '''
        result=''
        for  n in list:
            result+=str(n).zfill(bit)
            result+="-"
           
        return result[0:-1]
    
    def getNumber(self,list,bit=1):
        '''
        取得开机数组
        @param list list:传过来的数组
        @param int bit:返回的数字是几位
        @return: 返回取得的数组  
        '''
        result=''
        for  n in list:
            result+=str(n).zfill(bit)
            result+=","
           
        return result[0:-1]
    
    def getDict(self,type):
        '''
       @param string type:类型
       返回所有需要的数组 
        '''
        dict={}
        dict['type']=type
        dict['issue']=self.getIssue(type)
        list=self.getRandom(0,9,3,True)
       # print list
        dict['list']=list
        dict['number']=self.getNumber(list)
        jo=self.getJO(list)
        dict['jo']=jo
        dx=self. getDX(list,5)
        dict['dx']=dx
        dict['sum']=self.getSum(list)
        dict['sums']=sorted(self.getRandom(1,26,4)) #和值推荐应该是0-27但是0、27出现的概率太低
        dict['recommend']=self.getRecomend(sorted(self.getRandom(0,9,6,False)))
        return dict
                         
    def get3D(self):
        '''
        计算3D
        '''
        dict=self.getDict("3D")
        dict['characteristic']=r'和值：'+str(dict['sum'])+r' 奇偶：'+dict['jo']+r' 大小：'+dict['dx']
        dict['strrecommend']=r'和值：'+self.getRecomend(dict['sums'])+r' 复试推荐：'+dict['recommend']
        return dict
        
    def getP3(self):
        '''
        计算3D
        '''
        dict=self.getDict("P3")
        dict['characteristic']=r'和值：'+str(dict['sum'])+r' 奇偶：'+dict['jo']+r' 大小：'+dict['dx']
        dict['strrecommend']=r'和值：'+self.getRecomend(dict['sums'])+r' 复试推荐：'+dict['recommend']
        return dict
    
    def getCJDLT(self):
        '''
        计算超级大乐透
        '''
        type="CJDLT"
        dict={}
        dict['type']=type
        dict['issue']=self.getIssue(type)
        list=self.getRandom(1,35,5,False,True)
#        print list
        dict['list']=list
        listBack=self.getRandom(1,12,2,False,True)
#        print listBack
        dict['listBack']=listBack
        dict['number']=self.getNumber(list,2)+"+"+self.getNumber(listBack,2)
        jo=self.getJO(list)
        dict['jo']=jo
        dict['sum']=self.getSum(list)
        dict['recommend']=self.getRecomend(sorted(self.getRandom(1,35,10)),2)
        dict['recommendBack']=self.getRecomend(sorted(self.getRandom(1,12,4)),2)
        dict['characteristic']=r'和值：'+str(dict['sum'])+r' 奇偶：'+dict['jo']
        dict['strrecommend']=r'前区：'+dict['recommend']+r'  后区：'+dict['recommendBack']
        return dict
    
    def getSSQ(self):
        '''
        计算超级大乐透
        '''
        type="SSQ"
        dict={}
        dict['type']=type
        dict['issue']=self.getIssue(type)
        list=self.getRandom(1,33,6,False,True)
#        print list
        dict['list']=list
        listBack=self.getRandom(1,16,1,False,True)
#        print listBack
        dict['listBack']=listBack
        dict['number']=self.getNumber(list,2)+"+"+self.getNumber(listBack,2)
        jo=self.getJO(list)
        dict['jo']=jo
        dict['sum']=self.getSum(list)
        dict['recommend']=self.getRecomend(sorted(self.getRandom(1,33,10)),2)
        dict['recommendBack']=self.getRecomend(sorted(self.getRandom(1,16,4)),2)
        dict['characteristic']=r'和值：'+str(dict['sum'])+r' 奇偶：'+dict['jo']
        dict['strrecommend']=r'红球：'+dict['recommend']+r'  蓝球：'+dict['recommendBack']
        return dict