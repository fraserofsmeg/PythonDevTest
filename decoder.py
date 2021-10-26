# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:14:44 2021

@author: Fraser
"""
import json
import pickle
import base64
def processResponse():
    filehandler = open("responseDump", 'rb') 
    html = pickle.load(filehandler)
    
    #print(html)
    my_json = html.decode('utf8')
    data = json.loads(my_json)
    for cntr, x in enumerate(data['result']):
        with open('Job descriptions/' + str(cntr) + '.txt', 'w') as f:
            f.write(base64.b64decode(x).decode('utf-8'))