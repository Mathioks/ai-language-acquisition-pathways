#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd
import MeCab

# Load the list of words
duo = np.loadtxt("SRC/Duolingo_JP_Wordlist_2024-12-09.txt", encoding="utf-8", dtype="str")
print(duo)

# Initialize MeCab Tagger for word segmentation
wakati = MeCab.Tagger("-Owakati")

# Parse each word individually and collect the results
parsed_words = []
for word in duo:
    # Parse the word and split it into tokens
    parsed = wakati.parse(word).split()
    parsed_words.extend(parsed)

# Convert the list of parsed words to a Pandas DataFrame
df = pd.DataFrame(parsed_words, columns=["Word"])

# Remove duplicates, keeping only the first occurrence
df_unique = df.drop_duplicates(subset=["Word"], keep='first').reset_index(drop=True)

# Define the output file name
output_file = "Duolingo_unique_words.csv"

# Save the unique words to CSV
df_unique.to_csv(output_file, index=False, encoding="utf-8-sig")

# Print the results
print(f"Duolingo_Unique words saved to {output_file}")


# In[69]:


pfreq = pd.read_csv('Personalized_Frequency_List.csv', encoding="utf-8-sig")
duolist = pd.read_csv('Duolingo_unique_words.csv', encoding="utf-8", header=None, names=["Word"])

# Create an empty list to hold the result (word and line number)
duolingo_frequency = []

# Compare each word in the Duolingo list with the Personalized list
for duolingo_word in duolist["Word"]:
    # Try to find the word in the personalized list
    match = pfreq[pfreq["Word"] == duolingo_word]
    if not match.empty:
        # Get the line number (index + 1 for human-readable index)
        line_number = match.index[0] + 1  # Adding 1 to make the line number 1-based
        count = match["Total Count"].values[0]  # Get the count of the word from the Personalized list (not 'Total Count')
        duolingo_frequency.append([duolingo_word, line_number, count])
    else:
        # If no match, assign None or some other placeholder
        duolingo_frequency.append([duolingo_word, None, None])

# Create a new DataFrame from the list
duolingo_frequency_df = pd.DataFrame(duolingo_frequency, columns=["Word", "Line_Number", "Count"])

# Convert "Line" and "Count" columns to integers (where applicable)
duolingo_frequency_df["Line_Number"] = duolingo_frequency_df["Line_Number"].astype('Int64')  # 'Int64' allows None values
duolingo_frequency_df["Count"] = duolingo_frequency_df["Count"].astype('Int64')  # Convert to integer

df_sorted = duolingo_frequency_df.sort_values(
    by=["Line_Number"], 
    ascending=[True],  # Ascending for "Line_Number" and descending for "Count"
    na_position="last"  # Place None/NA values at the end
).reset_index(drop=True)

# Save the result to a new CSV
df_sorted.to_csv("DuolingoFrequency.csv", index=False, encoding="utf-8-sig")

# Print the first few rows to confirm
print(df_sorted.head(50))

