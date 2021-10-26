# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:58:41 2021

@author: Fraser
"""

import requests

headers = {'Content-Type': 'application/json'}

response = requests.get("http://ciivsoft.getsandbox.com/jobs",headers=headers)

print(response.content)