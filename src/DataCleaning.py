#! /usr/bin/env python2.7

'''
DataCleaning.py contains subroutines to clean and parse information gathered on 
jobs from internet.
'''

# programming skills
_skill_prog = ["R,", "ruby", "python", "java", "c\+\+", "mysql",
               "mapreduce", "hadoop", "nosql", "matlab", "scala",
               "excel", "mongodb", "spark", "tableau", "sql",
               "php", "azure", "postgresql"]

# educational background
_skill_edu = ["mathematics", "statistics", "computer science"]

# data science skills
_skill_ds = ["machine learning", "deep learning", "neural network"]


def findKeyword(keys, df, col):
    '''
    findKeyword finds keys in the given column of 
    the data frame and construct a new column with the those found keys.
    '''

    data = df[col]
    
    out = {}
    for key in keys:
        locBool = data.str.contains(key, case=False).fillna(False)
        out[key] = locBool
        
    return out
