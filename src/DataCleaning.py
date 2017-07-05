#! /usr/bin/env python2.7

import pandas as pd

from bs4 import BeautifulSoup

'''
DataCleaning.py contains subroutines to clean and parse information gathered on 
jobs from internet.
'''

# programming skills

_skill_prog_dict = {"R-software": ["R,", " R "],
                    "Ruby": ["ruby"],
                    "Python": ["python"],
                    "Java": ["java"],
                    "C++": ["c\+\+"],
                    "MySql": ["mysql"],
                    "MapReduce": ["mapreduce"],
                    "Hadoop": ["hadoop"],
                    "NoSql": ["nosql"],
                    "MatLab": ["matlab"],
                    "Scala": ["scala"],
                    "Excel": ["excel"],
                    "MongoDB": ["mongodb"],
                    "Spark": ["spark"],
                    "Tableau": ["tableau"],
                    "Sql": ["sql"],
                    "PHP": ["php"],
                    "Azure": ["azure"],
                    "PostgreSql": ["postgresql"],
                    "JSON": ["json"]
}

# educational background
_skill_edu_dict = {"mathematics": ["mathematics"],
                   "statistics": ["statistics"],
                   "computer science": ["computer science"]
}

# data science skills

_skill_ds_dict = { "machine learning": ["ml", "machine learning"],
                   "deep learning": ["dp", "deep learning"],
                   "NLP": ["nlp", "natural language processing"],
                   "neural network": ["neural network"],
                   "data modeling": ["data modeling", "data modelling"],
                   "microservices": ["microservices"]
}


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

def findKeywords(Dict, df, col):
    '''
    findKeyword finds keys in the given column of 
    the data frame and construct a new column with the those found keys.
    '''

    out = {}
    
    for key in Dict.keys():
        locBool = pd.Series(False, index=df.index)
        #
        for keyword in Dict[key]:
            locBool = locBool | df[col].str.contains(keyword, case=False).fillna(False)
        out[key] = locBool
        
    return out

def Html2Text(df, col):
    '''
    converts html code presented in a col into plain text.
    '''

    get_text = lambda x : BeautifulSoup(x, "lxml").get_text()

    return df[col].apply(get_text)
