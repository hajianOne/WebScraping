#! /usr/bin/env python2.7

import matplotlib.pyplot as plt
from matplotlib.pylab import savefig
import pandas as pd

import json

from src import DataCleaning

reload(DataCleaning)

with open("data/data1.json","r") as Input:
    data = json.load(Input)

df = pd.DataFrame(data)

# Programming skills
fig = plt.figure(1)

skills_prog = pd.DataFrame(DataCleaning.findKeyword(DataCleaning._skill_prog, df,
                                                    "description")).mean()*100
skills_prog.sort_values(inplace=True, ascending=False)
skills_prog.plot(kind="bar", subplots=True, rot=-45, 
                      label="Programming skills required for data science job (Berlin)")
plt.ylabel("Percentage")
plt.gcf().subplots_adjust(bottom=0.15)

savefig("output/skills_prog.png")

# Data science skills
plt.figure(2)
skills_ds = pd.DataFrame(DataCleaning.findKeyword(DataCleaning._skill_ds, df,
                                                    "description")).mean()*100
skills_ds.sort_values(inplace=True, ascending=False)
skills_ds.plot(kind="bar", subplots=True, rot=0,
               label="Data science skills required")

plt.ylabel("Percentage")
savefig("output/skills_ds.png")


plt.show(block=False)
