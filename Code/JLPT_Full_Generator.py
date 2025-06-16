#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Data preparation
import pandas as pd
import numpy as np

# Load data
JLPTN5 = pd.read_csv("JLPT/JLPT_Wordlist_N5.csv", encoding="shift_jis")
JLPTN4 = pd.read_csv("JLPT/JLPT_Wordlist_N4.csv", encoding="shift_jis")
JLPTN3 = pd.read_csv("JLPT/JLPT_Wordlist_N3.csv", encoding="shift_jis")
JLPTN2 = pd.read_csv("JLPT/JLPT_Wordlist_N2.csv", encoding="shift_jis")
JLPTN1 = pd.read_csv("JLPT/JLPT_Wordlist_N1.csv", encoding="shift_jis")
JLPTNG5 = pd.read_csv("JLPT/JLPT_Grammar_N5.csv", encoding="shift_jis")
JLPTNG4 = pd.read_csv("JLPT/JLPT_Grammar_N4.csv", encoding="shift_jis")
JLPTNG3 = pd.read_csv("JLPT/JLPT_Grammar_N3.csv", encoding="shift_jis")
JLPTNG2 = pd.read_csv("JLPT/JLPT_Grammar_N2.csv", encoding="shift_jis")

# Add a column indicating the JLPT level for each dataset
JLPTN5['JLPT_Level'] = 'N5'
JLPTN4['JLPT_Level'] = 'N4'
JLPTN3['JLPT_Level'] = 'N3'
JLPTN2['JLPT_Level'] = 'N2'
JLPTN1['JLPT_Level'] = 'N1'
JLPTNG5['JLPT_Level'] = 'N5'
JLPTNG4['JLPT_Level'] = 'N4'
JLPTNG3['JLPT_Level'] = 'N3'
JLPTNG2['JLPT_Level'] = 'N2'

# Merge JLPT lists
JLPTFull = pd.concat([JLPTN5, JLPTNG5, JLPTN4, JLPTNG4, JLPTN3, JLPTNG3, JLPTN2, JLPTNG2, JLPTN1], ignore_index=True)

# Print the merged data with the JLPT level column
print(JLPTFull)

# Save the aggregated data to a CSV
JLPTFull.to_csv("JLPTFull.csv", index=False, encoding="utf-8-sig")
print(f"Aggregated data saved to JLPTFull.csv")

