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
fig, ax = plt.subplots(1, figsize=(5,3))

DataCleaning.findKeywords(DataCleaning._skill_prog_dict, df, "description")
skills_prog = pd.DataFrame(
    DataCleaning.findKeywords(
        DataCleaning._skill_prog_dict, df, "description")).mean()*100

skills_prog.sort_values(inplace=True, ascending=False)
skills_prog.plot(kind="bar", subplots=True, rot=-45,
                 label="Programming skills required for data science job (Berlin)")
ax.set_xticklabels(skills_prog.index, ha="left", size="small")
plt.ylabel("Percentage")
plt.gcf().subplots_adjust(bottom=0.25)

savefig("output/skills_prog.png")

# Data science skills
fig, ax = plt.subplots(1, figsize=(5,3))
skills_ds = pd.DataFrame(DataCleaning.findKeywords(DataCleaning._skill_ds_dict, df,
                                                    "description")).mean()*100
skills_ds.sort_values(inplace=True, ascending=False)
skills_ds.plot(kind="bar", subplots=True, rot=-45,
               label="Data science skills required")
ax.set_xticklabels(skills_ds.index, ha="left")
plt.ylabel("Percentage")
plt.gcf().subplots_adjust(bottom=0.4)
savefig("output/skills_ds.png")


#plt.show(block=False)
