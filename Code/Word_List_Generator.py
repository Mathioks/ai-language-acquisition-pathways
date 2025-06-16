#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data preparation
import pandas as pd
import numpy as np

# Load data
JLPT = pd.read_csv("JLPTFull.csv", encoding = "utf-8")
Top10K_Kagome = pd.read_csv("SRC/2021_Top10K_JP_Frequency_Kagome.csv", encoding = "shift_jis", delimiter = ";")
Top10K_Kagome.drop(columns=Top10K_Kagome.columns[0], axis=1, inplace=True)
Duolingo = pd.read_csv("Duolingo_unique_words.csv", encoding = "utf-8")

print(Top10K_Kagome)


# In[2]:


print(JLPT)


# In[3]:


# Load the provided files
import pandas as pd

# Load the files as DataFrames
duolingo_words = pd.read_csv('Duolingo_unique_words.csv', encoding="utf-8", header=None, names=["Word"])
jlpt_full = pd.read_csv('JLPTFull.csv', encoding="utf-8")
top10k = pd.read_csv('SRC/2021_Top10K_JP_Frequency_Kagome.csv', encoding="shift_jis", delimiter = ";")

# Display the first few rows of each DataFrame to understand their structures
duolingo_words.head(), jlpt_full.head(), top10k.head()

# Rename columns for consistency
jlpt_full.rename(columns={"Column1": "Word"}, inplace=True)
top10k.rename(columns={"Rank": "Rank", "Lemma": "Word", "Occurrences": "Occurrences"}, inplace=True)

# Display the first few rows of each DataFrame to understand their structures
duolingo_words.head(), jlpt_full.head(), top10k.head()


# In[4]:


# Add columns for Duolingo and JLPT presence to the Top10K dataframe
top10k["Duolingo_Words"] = top10k["Word"].isin(duolingo_words["Word"]).astype(int)  # 1 if present in Duolingo
top10k["JLPT_Words"] = top10k["Word"].isin(jlpt_full["Word"]).astype(int)          # 1 if present in JLPT

# Identify words in Duolingo but not in Top10K
duolingo_extra = duolingo_words[~duolingo_words["Word"].isin(top10k["Word"])].copy()
duolingo_extra["Rank"] = None
duolingo_extra["Occurrences"] = None
duolingo_extra["Duolingo_Words"] = 1
duolingo_extra["JLPT_Words"] = 0

# Identify words in JLPT but not in Top10K or Duolingo
jlpt_extra = jlpt_full[~jlpt_full["Word"].isin(top10k["Word"]) & ~jlpt_full["Word"].isin(duolingo_words["Word"])].copy()
jlpt_extra["Rank"] = None
jlpt_extra["Occurrences"] = None
jlpt_extra["Duolingo_Words"] = 0
jlpt_extra["JLPT_Words"] = 1

# Combine the Top10K, Duolingo extra, and JLPT extra into a single dataframe
combined = pd.concat([top10k, duolingo_extra, jlpt_extra], ignore_index=True)

# Save the combined dataframe to a CSV
combined.to_csv("Output/Combined_Wordlist.csv", index=False, encoding="utf-8-sig")

# Display the first few rows of the combined dataframe
combined.head(50)


# In[5]:


# NEW
# Add columns for Duolingo and JLPT presence to the Top10K dataframe
top10k["Duolingo_Words"] = top10k["Word"].isin(duolingo_words["Word"]).astype(int)  # 1 if present in Duolingo
top10k["JLPT_Words"] = top10k["Word"].isin(jlpt_full["Word"]).astype(int)          # 1 if present in JLPT

# Remove duplicates in jlpt_full and map JLPT_Level based on Word
jlpt_level_map = jlpt_full.drop_duplicates(subset="Word").set_index("Word")["JLPT_Level"]
top10k["JLPT_Level"] = top10k["Word"].map(jlpt_level_map)

# Identify words in Duolingo but not in Top10K
duolingo_extra = duolingo_words[~duolingo_words["Word"].isin(top10k["Word"])].copy()
duolingo_extra["Rank"] = None
duolingo_extra["Occurrences"] = None
duolingo_extra["Duolingo_Words"] = 1
duolingo_extra["JLPT_Words"] = 0
duolingo_extra["JLPT_Level"] = None  # No JLPT level for Duolingo extra words

# Identify words in JLPT but not in Top10K or Duolingo
jlpt_extra = jlpt_full[~jlpt_full["Word"].isin(top10k["Word"]) & ~jlpt_full["Word"].isin(duolingo_words["Word"])].copy()
jlpt_extra["Rank"] = None
jlpt_extra["Occurrences"] = None
jlpt_extra["Duolingo_Words"] = 0
jlpt_extra["JLPT_Words"] = 1
# JLPT_Level already exists in jlpt_extra, no need to modify it

# Combine the Top10K, Duolingo extra, and JLPT extra into a single dataframe
combined = pd.concat([top10k, duolingo_extra, jlpt_extra], ignore_index=True)

# Save the combined dataframe to a CSV
combined.to_csv("Output/Combined_Wordlist.csv", index=False, encoding="utf-8-sig")

# Display the first few rows of the combined dataframe
combined.head(50)


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns

# Words in and not in the Top 10K for Duolingo
duolingo_in_top10k = combined["Duolingo_Words"] == 1
duolingo_not_in_top10k = combined["Duolingo_Words"] == 0

# Counts
duolingo_in_count = duolingo_in_top10k.sum()
duolingo_not_in_count = duolingo_not_in_top10k.sum()

# Pie chart
plt.figure(figsize=(6, 6))
labels = ["In Top 10K", "Not in Top 10K"]
sizes = [duolingo_in_count, duolingo_not_in_count]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["blue", "lightblue"])
plt.title("Duolingo Words in Top 10K")
plt.show()


# In[7]:


# Words in and not in the Top 10K for JLPT
jlpt_in_top10k = combined["JLPT_Words"] == 1
jlpt_not_in_top10k = combined["JLPT_Words"] == 0

# Counts
jlpt_in_count = jlpt_in_top10k.sum()
jlpt_not_in_count = jlpt_not_in_top10k.sum()

# Pie chart
plt.figure(figsize=(6, 6))
sizes = [jlpt_in_count, jlpt_not_in_count]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["green", "lightgreen"])
plt.title("JLPT Words in Top 10K")
plt.show()


# In[8]:


plt.figure(figsize=(10, 6))

# Histogram for Duolingo words
sns.histplot(
    data=combined[duolingo_in_top10k],
    x="Rank",
    bins=50,
    color="blue",
    label="Duolingo Words",
    kde=True
)

# Histogram for JLPT words
sns.histplot(
    data=combined[jlpt_in_top10k],
    x="Rank",
    bins=50,
    color="green",
    label="JLPT Words",
    kde=True
)

plt.xlabel("Frequency Rank (Top 10K)")
plt.ylabel("Word Count")
plt.title("Rank Distribution of Duolingo and JLPT Words in Top 10K")
plt.legend()
plt.show()


# In[9]:


print(f"Duolingo Words in Top 10K: {duolingo_in_count}")
print(f"Duolingo Words not in Top 10K: {duolingo_not_in_count}")
print(f"JLPT Words in Top 10K: {jlpt_in_count}")
print(f"JLPT Words not in Top 10K: {jlpt_not_in_count}")


# In[10]:


plt.figure(figsize=(10, 6))

# Calculate cumulative frequency for all words
combined["Cumulative_Occurrences"] = combined["Occurrences"].cumsum()

# Plot cumulative occurrence for Duolingo and JLPT
sns.lineplot(
    data=combined[combined["Duolingo_Words"] == 1],
    x="Rank",
    y="Cumulative_Occurrences",
    label="Duolingo Words",
    color="blue"
)

sns.lineplot(
    data=combined[combined["JLPT_Words"] == 1],
    x="Rank",
    y="Cumulative_Occurrences",
    label="JLPT Words",
    color="green"
)

# Add overall cumulative line for reference
sns.lineplot(
    data=combined,
    x="Rank",
    y="Cumulative_Occurrences",
    label="All Words",
    color="black",
    linestyle="--"
)

plt.xlabel("Frequency Rank (Top 10K)")
plt.ylabel("Cumulative Occurrences")
plt.title("Cumulative Coverage of Top 10K Words")
plt.legend()
plt.show()


# In[11]:


from matplotlib_venn import venn2

# Calculate overlap
duolingo_words = set(combined[combined["Duolingo_Words"] == 1]["Word"])
jlpt_words = set(combined[combined["JLPT_Words"] == 1]["Word"])

venn = venn2([duolingo_words, jlpt_words], ("Duolingo", "JLPT"))
plt.title("Overlap Between Duolingo and JLPT Word Lists")
plt.show()


# In[13]:


print(duolingo_words)


# In[14]:


print(jlpt_full)


# In[15]:


print(Top10K_Kagome)


# In[16]:


print(combined)


# In[18]:


Scraped = pd.read_csv("Output/Scraped_Wordlist.csv", encoding = "utf-8")
print(Scraped)

