# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:03:37 2021

@author: Fraser
"""


def getSkills():
    with open('skills.txt') as f:
        lines = f.readlines()
    cleanLines = [x.replace("\n","").lower() for x in lines]
    return cleanLines