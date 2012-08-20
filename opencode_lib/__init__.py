#coding=utf-8 
'''
Created on 2012-8-17

@author: Eagle
'''
from opencode_lib.readJson import readJson
from opencode_lib.readClosed import readClosed
from opencode_lib.readOpencode import readOpencode
from opencode_lib.dbOperation import dbOperation
__abstract__ = '计算开机号程序。开发者：Eagle  版本：'
__version__ = '0.0.2'
__info__ = '0.0.2增加数据库读写'
"""The version of opencode"""
__all__ = ["readJson","readClosed","readOpencode","dbOperation"]