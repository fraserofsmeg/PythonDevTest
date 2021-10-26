# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:07:50 2021

@author: Fraser
"""

from urllib.request import Request, urlopen
import pickle

def getdate():
    targetURL = "http://ciivsoft.getsandbox.com/jobs"
    headers = {'Content-Type': 'application/json'}
    request = Request(targetURL, headers=headers)
    html = urlopen(request).read()
     
    filehandler = open("responseDump", 'wb') 
    pickle.dump(html, filehandler)
    
    
