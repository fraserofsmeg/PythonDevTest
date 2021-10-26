# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:23:29 2021

@author: Fraser
"""

from os import listdir
from os.path import isfile, join
import re
from multiprocessing import Pool

from parseLines import getSkills
import numpy as np
import pandas as pd 

allSkills = getSkills()
numskills = len(allSkills)

#function for processing an individual job
#Inputs: file  location of job description
#Outputs: list of lists containing character number of each search term
#        (outer list is per search term, inner list if different occourances)
def process1Job(loc):
    with open(loc, 'r') as file:
        jobDesc = file.read().lower()
        results = [0]*numskills
        for cntr, y in enumerate(allSkills):
            results[cntr] =[m.start() for m in re.finditer(y, jobDesc)]
    return results

#Main function to loop through all jobs in specified folder (Job descriptions/)
#Inputs: None
#Outputs: CSV file for each job descript, table of each skill word occurances in file
def runAllJobdescs():
    pool = Pool()
    jobDescPath = "Job descriptions/"
    fileOutputPath = "WordLocs/"
    onlyfiles = [jobDescPath + f for f in listdir(jobDescPath) if isfile(join(jobDescPath, f))]
    
    finalResults = pool.map(process1Job, onlyfiles)
    for cntr,z in enumerate(finalResults):
        length = max(map(len, finalResults[0]))
        y=np.array([xi+[None]*(length-len(xi)) for xi in z]).T  
        df = pd.DataFrame(y)
        df.columns = [allSkills]
        df.to_csv(fileOutputPath + str(cntr) + ".csv")
