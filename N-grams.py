# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:39:33 2021

@author: Fraser
"""

from os import listdir
from os.path import isfile, join
import re
from multiprocessing import Pool

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

import string

from parseLines import getSkills

allSkillsWPunc = getSkills()
allSkills = [x.translate(str.maketrans('', '', string.punctuation)) for x in allSkillsWPunc]
numskills = len(allSkills)

def process1Job(loc):
    with open(loc, 'r') as file:
        jobDesc = file.read().lower().translate(str.maketrans('', '', string.punctuation))
    return jobDesc
        
if __name__ == '__main__':
    pool = Pool()

    jobDescPath = "Job descriptions/"
    onlyfiles = [jobDescPath + f for f in listdir(jobDescPath) if isfile(join(jobDescPath, f))]
    
    alltext = pool.map(process1Job, onlyfiles)
    
    tfidf_vectorizer=TfidfVectorizer(use_idf=True)
    tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(alltext)
    featureDict = tfidf_vectorizer.get_feature_names()
    
    skillsIndex = [featureDict.index(x) if x in featureDict else -1 for x in allSkills]
    
    for cntr1, x in enumerate(tfidf_vectorizer_vectors):
        print("File " + str(cntr1) + "...")
        for cntr2, z in enumerate(skillsIndex):
            if z == -1:
                print(allSkills[cntr2] + " [[0.0]]" )
                #this quick pass only takes  into account single word n-grams
                #so anything not in featureDict (eg. multiword skills) requires special handling
            else:
                print(allSkills[cntr2] + " " + str(x.T.todense()[z]))
        print("\n")

    