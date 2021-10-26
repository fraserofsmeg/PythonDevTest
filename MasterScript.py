# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:37:39 2021

@author: Fraser
"""

from FasterGet import getdate

from decoder import processResponse

from WordSearch import runAllJobdescs


if __name__ == "__main__":
    getdate()
    processResponse()
    runAllJobdescs()
