#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2012-4-11

@author: Eagle
'''

import sys,re,urllib2,cookielib
import urllib,httplib,re

class weiboOperation(object):

	def get_code(self,strmsg):
		app_key = '1968125717'
		#url='https://api.t.sina.com.cn/oauth2/authorize?client_id=123050457758183&redirect_uri=http://www.example.com/response&response_type=code'
		url=r"https://api.weibo.com/oauth2/authorize?client_id=1968125717&redirect_uri=http%3A%2F%2Fweb.xxx.com%2Fweibo%2Fcallback.php&response_type=code"
		callback_url = 'http://web.xxx.com/weibo/callback.php'
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
		opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322)')]
		
		conn = httplib.HTTPSConnection('api.weibo.com')
		username=r"xxx@sina.com"
		passwd=r"xxxx"
		postdata = urllib.urlencode({'client_id':app_key,'response_type':'code','redirect_uri':callback_url,'action':'submit','userId':username,'passwd':passwd,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
		#conn.request('POST','/oauth2/authorize',postdata,{'Referer':url})
		conn.request('POST','/oauth2/authorize',postdata,{'Referer':url, 'Content-Type': 'application/x-www-form-urlencoded'})
		res = conn.getresponse()
		page = res.read 
		
		#print 'msg===========',res.msg
		content=re.sub('\r\n', '', str(res.msg))
		m= re.findall(r'.*?Location:(.*?)X-Varnish.*?',content, re.S | re.I)
		print '######',m[0].strip()
		#print 'status===========',res.status
		#print 'reason===========',res.reason
		#print 'version===========',res.version
		
		f = opener.open(m[0].strip())
		s = f.read()
	   # print s
		
		f=opener.open(r'http://web.xxx.com/weibo/weibolist.php?text='+strmsg)
		s = f.read()
		f.close()
		#print page
		conn.close()
'''

if __name__ == '__main__':
    strmsg= sys.argv[1]
    string = unicode(strmsg,r"utf-8")
    strmsg=urllib.quote(string.encode("utf-8"))
    #strmsg=urllib.quote(strmsg)
	
    get_code(strmsg)
    #s=download()
    #print s
    print r'‘À––ÕÍ±œ'
    pass
'''