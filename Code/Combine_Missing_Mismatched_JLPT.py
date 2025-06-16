#!/usr/bin/env python
# coding: utf-8

# In[16]:


### import pandas as pd

Wordlist = pd.read_csv("Output/Scraped_Wordlist.csv", encoding = "utf-8")
print(Wordlist["JLPT_Levels"].head(20))


# In[33]:


import pandas as pd

Wordlist = pd.read_csv("Output/Scraped_Wordlist.csv", encoding = "utf-8")
    
def processword(word):
    if(word == 'jlpt-n5'):
        print("it was correct")
        return "N5"
    return word


for word in Wordlist["JLPT_Levels"]:
    processword(word)
    print(word)



# In[51]:


import pandas as pd
import ast

# Load the DataFrame
Wordlist = pd.read_csv("Output/Scraped_Wordlist.csv", encoding="utf-8")
print(Wordlist["JLPT_Levels"].head(30))
# Convert string representations of lists to actual lists
Wordlist["JLPT_Levels"] = Wordlist["JLPT_Levels"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("[") else x
)

# Process the JLPT_Levels column
def process_jlpt_levels(levels):
    if not isinstance(levels, list):  # Ensure we handle only lists
        return levels
    processed_levels = []
    for word in levels:
        if word == "jlpt-n5":  # Replace specific word
            processed_levels.append("N5")
        elif word == "jlpt-n4":  # Replace specific word
            processed_levels.append("N4")
        elif word == "jlpt-n3":  # Replace specific word
            processed_levels.append("N3")
        elif word == "jlpt-n2":  # Replace specific word
            processed_levels.append("N2")
        elif word == "jlpt-n1":  # Replace specific word
            processed_levels.append("N1")
        else:
            processed_levels.append(word)  # Keep other words unchanged
    return processed_levels

# Apply the function to the JLPT_Levels column
Wordlist["JLPT_Levels"] = Wordlist["JLPT_Levels"].apply(process_jlpt_levels)

# Display the updated DataFrame
print(Wordlist["JLPT_Levels"].head(30))


# In[52]:





# In[66]:


import pandas as pd
import ast

# Load the DataFrame
Wordlist = pd.read_csv("Output/Scraped_Wordlist.csv", encoding="utf-8")
print(Wordlist["JLPT_Levels"].head(30))

# Convert string representations of lists to actual lists
Wordlist["JLPT_Levels"] = Wordlist["JLPT_Levels"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith("[") else x
)

# Process the JLPT_Levels column
def process_jlpt_levels(levels):
    if not isinstance(levels, list):  # Ensure we handle only lists
        return levels
    processed_levels = []
    for word in levels:
        if word == "jlpt-n5":  # Replace specific word
            processed_levels.append("N5")
        elif word == "jlpt-n4":  # Replace specific word
            processed_levels.append("N4")
        elif word == "jlpt-n3":  # Replace specific word
            processed_levels.append("N3")
        elif word == "jlpt-n2":  # Replace specific word
            processed_levels.append("N2")
        elif word == "jlpt-n1":  # Replace specific word
            processed_levels.append("N1")
        else:
            processed_levels.append(word)  # Keep other words unchanged
    return processed_levels

# Apply the initial cleaning to standardize levels
Wordlist["JLPT_Levels"] = Wordlist["JLPT_Levels"].apply(process_jlpt_levels)

# Function to split levels into main and additional difficulties
def split_levels(levels):
    if not isinstance(levels, list) or not levels:  # Handle empty or non-list entries
        return levels, []  # No changes for empty lists
    
    # Sort the levels based on numeric value (N1 < N2 < N3 < N4 < N5)
    sorted_levels = sorted(levels, key=lambda x: int(x[-1]))
    
    # Keep the lowest level (last in sorted order) and move the rest to additional difficulty
    main_level = [sorted_levels[-1]]
    additional_levels = sorted_levels[:-1]  # All except the lowest level
    
    return main_level, additional_levels

# Apply the function to create two separate columns
Wordlist[["JLPT_Levels", "JLPT_Additional_Difficulty"]] = Wordlist["JLPT_Levels"].apply(
    lambda x: pd.Series(split_levels(x))
)

# Display the updated DataFrame
print("Processed JLPT Levels:")
print(Wordlist[["JLPT_Levels", "JLPT_Additional_Difficulty"]].tail(30))


# In[67]:


# Rename the JLPT_Levels column to JLPT_Jisho_Level
Wordlist.rename(columns={"JLPT_Levels": "JLPT_Jisho_Level"}, inplace=True)

# Display the updated DataFrame to confirm the change
print("Updated Column Names:")
print(Wordlist.columns)

# Display the updated DataFrame
print(Wordlist[["JLPT_Jisho_Level", "JLPT_Additional_Difficulty"]].head(30))


# In[68]:


# Convert the JLPT_Jisho_Level column to a scalar value (not a list)
Wordlist["JLPT_Jisho_Level"] = Wordlist["JLPT_Jisho_Level"].apply(lambda x: x[0] if isinstance(x, list) and x else "NaN")

# Display the updated DataFrame to confirm the change
print("Updated JLPT_Jisho_Level column:")
print(Wordlist[["JLPT_Jisho_Level", "JLPT_Additional_Difficulty"]].head(30))


print(Wordlist[["JLPT_Level", "JLPT_Jisho_Level"]].head(50))


# In[69]:


# Save the combined dataframe to a CSV
Wordlist.to_csv("Output/JLPT_Full_Before_Comparison.csv", index=False, encoding="utf-8-sig")


# In[72]:


Wordlist = pd.read_csv("Output/JLPT_Full_Before_Comparison.csv", encoding="utf-8")
print(Wordlist.head(20))


# In[87]:


import pandas as pd

Wordlist = pd.read_csv("Output/JLPT_Full_Before_Comparison.csv", encoding="utf-8")

# Count rows where JLPT_Level is not NaN but JLPT_Jisho_Level is NaN
only_in_JLPT_Level = Wordlist[Wordlist["JLPT_Jisho_Level"].isna() & Wordlist["JLPT_Level"].notna()]

# Count rows where JLPT_Jisho_Level is not NaN but JLPT_Level is NaN
only_in_JLPT_Jisho_Level = Wordlist[Wordlist["JLPT_Level"].isna() & Wordlist["JLPT_Jisho_Level"].notna()]

# Print the results
print("Rows with value in JLPT_Level but not JLPT_Jisho_Level:")
print(only_in_JLPT_Level[["Word","JLPT_Level","JLPT_Jisho_Level"]])
print(f"Count: {len(only_in_JLPT_Level)}")

print("\nRows with value in JLPT_Jisho_Level but not JLPT_Level:")
print(only_in_JLPT_Jisho_Level[["Word","JLPT_Level","JLPT_Jisho_Level"]])
print(f"Count: {len(only_in_JLPT_Jisho_Level)}")

# Save the combined dataframe to a CSV
only_in_JLPT_Level[["Word","JLPT_Level","JLPT_Jisho_Level"]].to_csv("Output/JLPT_Rating_Only_In_JLPTDOC.csv", index=False, encoding="utf-8-sig")
only_in_JLPT_Jisho_Level[["Word","JLPT_Level","JLPT_Jisho_Level"]].to_csv("Output/JLPT_Rating_Only_In_Jisho.csv", index=False, encoding="utf-8-sig")


# In[88]:


import pandas as pd

# Load the DataFrame
Wordlist = pd.read_csv("Output/JLPT_Full_Before_Comparison.csv", encoding="utf-8")

# Count rows where both columns have values but are different
different_values = Wordlist[Wordlist["JLPT_Level"].notna() & Wordlist["JLPT_Jisho_Level"].notna() & (Wordlist["JLPT_Level"] != Wordlist["JLPT_Jisho_Level"])]

# Print the results
print("Rows where JLPT_Level and JLPT_Jisho_Level have different values:")
print(different_values[["Word","JLPT_Level","JLPT_Jisho_Level","JLPT_Additional_Difficulty"]])
print(f"Count: {len(different_values)}")

# Save the combined dataframe to a CSV
different_values[["Word","JLPT_Level","JLPT_Jisho_Level","JLPT_Additional_Difficulty"]].to_csv("Output/JLPT_Doc_And_Jisho_Differences.csv", index=False, encoding="utf-8-sig")


# In[97]:


import pandas as pd

# Define a function to get the lowest JLPT rating (N5 is the lowest, N1 is the highest)
def get_lowest_jlpt_rating(level1, level2):
    jlpt_order = {"N1": 1, "N2": 2, "N3": 3, "N4": 4, "N5": 5}
    return level1 if jlpt_order[level1] > jlpt_order[level2] else level2

# Load the DataFrame
Wordlist = pd.read_csv("Output/JLPT_Full_Before_Comparison.csv", encoding="utf-8")

# Create the Combined_JLPT_Ratings column
def combine_jlpt_ratings(row):
    jlpt_level = row["JLPT_Level"]
    jlpt_jisho_level = row["JLPT_Jisho_Level"]
    
    if pd.isna(jlpt_level) and pd.isna(jlpt_jisho_level):
        return None  # Both are NaN, no rating
    elif pd.isna(jlpt_level):
        return jlpt_jisho_level  # Only JLPT_Jisho_Level has a value
    elif pd.isna(jlpt_jisho_level):
        return jlpt_level  # Only JLPT_Level has a value
    elif jlpt_level != jlpt_jisho_level:
        return get_lowest_jlpt_rating(jlpt_level, jlpt_jisho_level)  # Both have values but they differ
    else:
        return jlpt_level  # Both have the same value

# Apply the function to each row to create the new column
Wordlist["Combined_JLPT_Ratings"] = Wordlist.apply(combine_jlpt_ratings, axis=1)

# Display the updated DataFrame with the new column
print(Wordlist[["JLPT_Level", "JLPT_Jisho_Level", "Combined_JLPT_Ratings"]].head(50))

# Save the combined dataframe to a CSV
Wordlist.to_csv("Output/JLPT_Combined_Ratings.csv", index=False, encoding="utf-8-sig")


# In[96]:


# Count how many rows have None in the "Combined_JLPT_Ratings" column
none_count = Wordlist["Combined_JLPT_Ratings"].isna().sum()

# Print the result
print(f"Number of rows with None in 'Combined_JLPT_Ratings': {none_count}")

