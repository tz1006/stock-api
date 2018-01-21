#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: stock-api/sharelist.py

import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
import threading

#######-- list工具 --#######
def save_list(listname='share_list'):
    if os.path.exists('database') == False:
        os.makedirs('database')
    file = open('database/sharelist.txt','w')
    for i in globals()[listname]:
        file.write(i) 
        file.write("\n")
    file.close()
    print('写入sharelist.txt成功!')

def import_list():
    global share_list
    share_list = []
    file=open('database/sharelist.txt')
    a = file.readlines()
    for i in a:
        share_list.append(i.replace('\n',''))
    print('读取sharelist.txt成功!')


#################--load-pages--####################
