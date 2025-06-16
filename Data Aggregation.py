#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import numpy as np

survey_results_clean = pd.read_json("survey_results_cleaned.json")


# In[2]:


print(survey_results_clean.iloc[22])


# In[3]:


# Introduce wordlists
wordlist = pd.read_csv('C:/Users/mathi/Documents/ブレダ/JP_Text_Analyzer/Output/Combined_Wordlist.csv')
print(wordlist)


# In[4]:


import matplotlib.pyplot as plt

# Overview: Count of App Users vs. Non-App Users
app_users_count = survey_results_clean['has_participant_used_apps'].value_counts()

# Distribution of JLPT Levels
jlpt_distribution = survey_results_clean['current_level'].value_counts()

# Most Common Study Methods
study_methods = survey_results_clean['main_study_method'].explode().value_counts(dropna=False)

# Intermediate Plateau Experience (Both Groups)
plateau_experience = survey_results_clean[['experienced_intermediate_plateau_Apps', 'experienced_intermediate_plateau_noApps']].sum()

# Print Results
print("App Users vs. Non-App Users:")
print(app_users_count)
print("\nJLPT Level Distribution:")
print(jlpt_distribution)
print("\nMost Common Study Methods:")
print(study_methods)
print("\nIntermediate Plateau Experience:")
print(plateau_experience)

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Pie Chart: App Users vs. Non-App Users
app_users_count.plot(kind='pie', autopct='%1.1f%%', ax=axes[0, 0], title="App Users vs. Non-App Users")

# Bar Chart: JLPT Level Distribution
jlpt_distribution.plot(kind='bar', ax=axes[0, 1], title="JLPT Level Distribution")

# Bar Chart: Most Common Study Methods
study_methods.plot(kind='bar', ax=axes[1, 0], title="Most Common Study Methods")

# Bar Chart: Plateau Experience
plateau_experience.plot(kind='bar', ax=axes[1, 1], title="Intermediate Plateau Experience")

plt.tight_layout()
plt.show()


# In[5]:


intermediate_plateau_participants = survey_results_clean[(survey_results_clean["current_level"]!="I really don't know")&((survey_results_clean["experienced_intermediate_plateau_Apps"]==True)|(survey_results_clean["experienced_intermediate_plateau_noApps"]==True))]

intermediate_plateau_participants.count()


# In[6]:


intermediate_plateau_participants = survey_results_clean[(survey_results_clean["experienced_intermediate_plateau_Apps"]==False)|(survey_results_clean["experienced_intermediate_plateau_noApps"]==False)]

intermediate_plateau_participants.count()


# # Current JLPT level vs main study method

# In[7]:


import seaborn as sns

# Load Data
# Explode 'main_study_method' to analyze individual methods
survey_results_exploded = survey_results_clean.explode('main_study_method')

# Count occurrences of each study method per JLPT level
study_method_counts = survey_results_exploded.groupby(['current_level', 'main_study_method']).size().unstack().fillna(0)

# Plot heatmap to visualize study method distribution across JLPT levels
plt.figure(figsize=(12, 6))
sns.heatmap(study_method_counts, cmap='Blues', annot=True, fmt='.0f', linewidths=0.5)
plt.title('Study Methods vs. JLPT Levels flat amounts')
plt.xlabel('Study Method')
plt.ylabel('JLPT Level')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[8]:


main_study_method_exploded = survey_results_clean.explode("main_study_method")

study_method_counts = main_study_method_exploded.groupby(["current_level", "main_study_method"]).size().unstack(fill_value=0)

level_counts = survey_results_clean["current_level"].value_counts().sort_index()

normalized_df = study_method_counts.div(level_counts, axis=0)

print(normalized_df)


# In[9]:


# Plot a heatmap of normalized study methods across JLPT levels
plt.figure(figsize=(10, 6))
sns.heatmap(normalized_df, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Normalized Study Methods Usage Across JLPT Levels")
plt.xlabel("Main Study Methods")
plt.ylabel("JLPT Levels")
plt.show()


# # Native language counts

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = survey_results_clean

### 1. Native & Other Languages Analysis ###
plt.figure(figsize=(10, 5))
native_counts = df['native_languages'].explode().value_counts()

print(native_counts)

sns.barplot(x=native_counts.index, y=native_counts.values)
plt.title("Native Language Distribution")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 8))
native_counts = df['native_languages'].explode().value_counts()

top_n = 15
native_counts_filtered = native_counts[:top_n]
native_counts_filtered["Other"] = native_counts[top_n:].sum()  # Group the rest as "Other"

sns.barplot(y=native_counts_filtered.index, x=native_counts_filtered.values)  # Horizontal bars
plt.title("Native Language Distribution")
plt.xlabel("Count")
plt.ylabel("Languages")
plt.show()


import pandas as pd

table_df = pd.DataFrame({
    "Language": native_counts.index,
    "Count": native_counts.values,
    "Percentage": (native_counts / native_counts.sum() * 100).round(1)
})

top_n = 15
table_df_filtered = table_df[:top_n]
other_sum = table_df[top_n:]["Count"].sum()
table_df_filtered.loc[len(table_df_filtered)] = ["Other", other_sum, (other_sum / native_counts.sum() * 100).round(1)]

print(table_df_filtered.to_markdown(index=False))  # Use `.to_latex()` if using LaTeX formatting


# In[11]:


#!pip install --upgrade tabulate


# # Years of study vs JLPT level

# In[12]:


# Base stats using .agg()
study_years_stats = survey_results_clean.groupby("current_level")["study_years"].agg(
    mean="mean",
    median="median",
    std_dev="std",
    count="count"
)

modes = (
    survey_results_clean.groupby("current_level")["study_years"]
    .apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    .rename("mode")
)

study_years_stats = study_years_stats.join(modes)

study_years_stats = study_years_stats[["mean", "median", "std_dev", "mode", "count"]]

print(study_years_stats)

### 2. Years of Study vs. JLPT Level ###
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['current_level'], y=df['study_years'])
plt.title("Years of Study vs. JLPT Level")
plt.xlabel("JLPT Level")
plt.ylabel("Years of Study")
plt.show()


# ## Conclusion
# 
# Interesting to see is that the general length of studying between N4 - N2 is very close to each other, is this part of the effect of the intermediate plateau?
# Furthermore, N1 clearly takes longer, however, some participants may have been N1 for a long time and since many people adhere to the idea that "you never stop learning a language" I do not know "when" they reached N1, and how much of their total years were spent at N1

# # Study goals

# In[13]:


### 3. Study Goals ###

study_goals_counts = df['study_goals'].explode().value_counts()

print(study_goals_counts)

plt.figure(figsize=(10, 5))
sns.barplot(x=study_goals_counts.index, y=study_goals_counts.values)
plt.title("Study Goals Distribution")
plt.xticks(rotation=45)
plt.show()


# # App usage patterns

# In[14]:


### 4. App Usage Patterns ###
apps_used = df['used_apps_Apps'].explode().value_counts()

print(apps_used)

plt.figure(figsize=(10, 5))
sns.barplot(x=apps_used.index, y=apps_used.values)
plt.title("Most Used Language Learning Apps")
plt.xticks(rotation=45)
plt.show()



# # Most & Least Useful Features

# In[15]:


### 5. Most & Least Useful Features ###
most_useful = df['most_useful_features_Apps'].explode().value_counts()
least_useful = df['least_useful_features_Apps'].explode().value_counts()

print(most_useful)
print()
print(least_useful)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(x=most_useful.index, y=most_useful.values, ax=axes[0])
axes[0].set_title("Most Useful App Features")
axes[0].tick_params(axis='x', rotation=45)

sns.barplot(x=least_useful.index, y=least_useful.values, ax=axes[1])
axes[1].set_title("Least Useful App Features")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()


# # Intermediate Plateau Analysis

# In[16]:


### 6. Intermediate Plateau Analysis ###
plt.figure(figsize=(10, 5))
plateau_counts = df['when_start_intermediatePlateau'].explode().value_counts()

print(plateau_counts)

sns.barplot(x=plateau_counts.index, y=plateau_counts.values)
plt.title("Years Before Hitting Intermediate Plateau")
plt.xticks(rotation=45)
plt.show()


# In[17]:


# When did intermediate plateau start (JLPT level)

### 6. Intermediate Plateau Analysis ###
plt.figure(figsize=(10, 5))
plateau_counts_JLPT = df['what_level_start_intermediatePlateau'].explode().value_counts()

print(plateau_counts_JLPT)

sns.barplot(x=plateau_counts_JLPT.index, y=plateau_counts_JLPT.values)
plt.title("JLPT level Where Hitting Intermediate Plateau")
plt.xticks(rotation=45)
plt.show()


# In[18]:


# How many people of each level experienced the intermediate plateau (normalized)

plateau_counts_JLPT_Normalized = plateau_counts_JLPT.div(level_counts, axis=0)

print(plateau_counts_JLPT_Normalized)

sns.barplot(x=plateau_counts_JLPT_Normalized.index, y=plateau_counts_JLPT_Normalized.values)
plt.title("JLPT level Where Hitting Intermediate Plateau")
plt.xticks(rotation=45)
plt.show()


# In[19]:


print(survey_results_clean["current_level"].explode().value_counts())

intermediate_plateau_df = survey_results_clean[(survey_results_clean["experienced_intermediate_plateau_Apps"] == True)|(survey_results_clean["experienced_intermediate_plateau_noApps"] == True)]

print(intermediate_plateau_df)


# In[20]:


import pandas as pd

stats_table = survey_results_clean.groupby("current_level")["study_years"].agg(
    mean="mean",
    median="median",
    std="std",
    mode=lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    n="count"
).reset_index()

print(stats_table.to_string(index=False))


# In[21]:


survey_results_clean[survey_results_clean["current_level"]=="JLPT N1"]["study_years"]


# In[22]:


import pandas as pd

usage_table = pd.crosstab(
    survey_results_clean["current_level"], 
    survey_results_clean["has_participant_used_apps"], 
    margins=True, 
    margins_name="n"
)

usage_table = usage_table.rename(columns={True: "Used apps", False: "Didn't use apps"}).reset_index()

usage_table["n"] = usage_table["Used apps"] + usage_table["Didn't use apps"]

usage_table["Used apps (%)"] = (usage_table["Used apps"] / usage_table["n"] * 100).round(2)
usage_table["Didn't use apps (%)"] = (usage_table["Didn't use apps"] / usage_table["n"] * 100).round(2)

usage_table = usage_table[["current_level", "Used apps", "Didn't use apps", "Used apps (%)", "Didn't use apps (%)", "n"]]

print(usage_table.to_string(index=False))


# # Correlation matrix of all columns

# # WRQ1: What gamification methods are applied in the current GLA's & GPALT's?

# In[24]:


all_gamification_values = survey_results_clean[
    ["most_useful_features_Apps", "least_useful_features_Apps", "no_longer_useful_Apps"]
].values.ravel()

flat_gamification_values = [
    item
    for sublist in all_gamification_values
    if isinstance(sublist, list)
    for item in sublist
    if item is not None
]

WRQ1_gamification_list = list(set(flat_gamification_values))

WRQ1_gamification_list.sort()

print(WRQ1_gamification_list)


# # WRQ1 Conclusion
# For this step I took the three questions that questioned participants about the gamification mechanics, being:
# - What are the most useful features in apps?
# - What are the least useful features in apps?
# - What are features you thought were useful, but no longer think are?
# 
# I then took all the values in these lists and combined them into a new list that sums up every gamification method mentioned.

# # WRQ2: How do Japanese learners experience these apps, the different gamified mechanics in these apps and their effectiveness for intermediate to higher level language learning?

# Useful columns:
#     
# current_level
# 
# has_participant_used_apps
# 
# used_apps_Apps
# 
# most_useful_Apps
# 
# most_useful_current_level_Apps
# 
# skill_improvement_usage_habits_Apps
# 
# most_useful_features_Apps
# 
# least_useful_features_Apps
# 
# no_longer_useful_Apps
# 
# comparative_enjoyment_other_methods_Apps
# 
# feel_apps_help_Apps
# 
# daily_study_time_Apps
# 
# current_level
# 
# why_continue_usage_Apps
# 
# use_to_overcome_challenges_noApps
# overcoming_challenges_noApps
# daily_study_time_noApps
# structured_vs_flexible_learning_noApps
# 
# other_tools_noApps
# why_other_tools_noApps
# most_effective_noApps
# least_effective_noApps
# 
# - How do they experience the apps
# - How do they experience the mechanics in the apps
# - How do they experience the effectiveness (+ for intermediate to advanced)

# In[25]:


used_apps = survey_results_clean["used_apps_Apps"].explode().value_counts()
most_useful_apps = survey_results_clean["most_useful_Apps"].explode().value_counts()
most_useful_current_level_Apps = survey_results_clean["most_useful_current_level_Apps"].explode().value_counts()
skill_improvement_usage_habits = survey_results_clean["skill_improvement_usage_habits_Apps"].explode().value_counts()
most_useful_features = survey_results_clean["most_useful_features_Apps"].explode().value_counts()
least_useful_features = survey_results_clean["least_useful_features_Apps"].explode().value_counts()
no_longer_useful_features = survey_results_clean["no_longer_useful_Apps"].explode().value_counts()
comparative_enjoyment_other_methods = survey_results_clean["comparative_enjoyment_other_methods_Apps"].explode().value_counts()
feel_apps_help = survey_results_clean["feel_apps_help_Apps"].explode().value_counts()
why_continue_usage = survey_results_clean["why_continue_usage_Apps"].explode().value_counts()


# In[26]:


N1_participants = survey_results_clean[survey_results_clean["current_level"]=="JLPT N1"]
N1_participants_used_apps = N1_participants[N1_participants["has_participant_used_apps"]==True]["used_apps_Apps"].explode().value_counts()
print(f"N1 participants used apps: \n{N1_participants_used_apps.to_string(index=True, header=False)}\n")

N1_participants_most_useful_apps = N1_participants[N1_participants["has_participant_used_apps"]==True]["most_useful_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants most useful apps: \n{N1_participants_most_useful_apps.to_string(index=True, header=False)}\n")

N1_participants_most_useful_current_apps = N1_participants[N1_participants["has_participant_used_apps"]==True]["most_useful_current_level_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants most useful apps at current level: \n{N1_participants_most_useful_current_apps.to_string(index=True, header=False)}\n")

N1_participants_most_useful_features = N1_participants[N1_participants["has_participant_used_apps"]==True]["most_useful_features_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants most useful features: \n{N1_participants_most_useful_features.to_string(index=True, header=False)}\n")

N1_participants_least_useful_features = N1_participants[N1_participants["has_participant_used_apps"]==True]["least_useful_features_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants least useful features: \n{N1_participants_least_useful_features.to_string(index=True, header=False)}\n")

N1_participants_no_longer_useful_features = N1_participants[N1_participants["has_participant_used_apps"]==True]["no_longer_useful_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants no longer useful features: \n{N1_participants_no_longer_useful_features.to_string(index=True, header=False)}\n")

N1_participants_skill_improvement_habits = N1_participants[N1_participants["has_participant_used_apps"]==True]["skill_improvement_usage_habits_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants changes in use of features as skill level increases: \n{N1_participants_skill_improvement_habits.to_string(index=True, header=False)}\n")

N1_participants_comparative_enjoyment = N1_participants[N1_participants["has_participant_used_apps"]==True]["comparative_enjoyment_other_methods_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants comparative enjoyment of apps compared to other methods: \n{N1_participants_comparative_enjoyment.to_string(index=True, header=False)}\n")

N1_participants_feel_apps_help = N1_participants[N1_participants["has_participant_used_apps"]==True]["feel_apps_help_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants do they feel that apps help them?: \n{N1_participants_feel_apps_help.to_string(index=True, header=False)}\n")

N1_participants_why_continue_using = N1_participants[N1_participants["has_participant_used_apps"]==True]["why_continue_usage_Apps"].explode().value_counts(dropna=False)
print(f"N1 participants why do they continue to use these apps?: \n{N1_participants_why_continue_using.to_string(index=True, header=False)}\n")


# In[27]:


main_study_method_exploded = survey_results_clean[survey_results_clean["current_level"] != "I really don't know"].explode("main_study_method")

study_method_counts = main_study_method_exploded.groupby(["current_level", "main_study_method"]).size().unstack(fill_value=0)

level_counts_all = survey_results_clean[survey_results_clean["current_level"] != "I really don't know"]["current_level"].value_counts().sort_index()

level_counts = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know") & 
    (survey_results_clean["has_participant_used_apps"] == True)]["current_level"].value_counts().sort_index()

normalized_df = study_method_counts.div(level_counts_all, axis=0)

percentage_df = normalized_df * 100
percentage_df = percentage_df.round(3)

print(percentage_df)


# In[28]:


main_study_method_exploded = survey_results_clean[survey_results_clean["current_level"] != "I really don't know"].explode("main_study_method")

study_method_counts = main_study_method_exploded.groupby(["current_level", "main_study_method"]).size().unstack(fill_value=0)

level_counts_all = survey_results_clean[survey_results_clean["current_level"] != "I really don't know"]["current_level"].value_counts().sort_index()

study_method_counts["N"] = level_counts_all

normalized_df = study_method_counts.div(level_counts_all, axis=0) * 100

percentage_df = normalized_df.drop(columns=["N"]).round(1)

percentage_df = percentage_df[["Apps", "Classes", "Immersion (Traveling)", "Immersion (living in the country)", "Immersion (through media)", "Language exchange", "Private tutoring", "Self-study", "Textbooks","AI","Websites"]]

print("Actual Values (N per JLPT level included):")
print(study_method_counts)

print("\nPercentage Values:")
print(percentage_df)


# In[29]:


study_method_counts.T


# In[30]:


plt.figure(figsize=(10, 6))
sns.heatmap(percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Study Method Usage per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Study Method")
plt.tight_layout()
plt.show()


# In[31]:


most_useful_current_level_Apps_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("most_useful_current_level_Apps")

most_useful_current_level_Apps_counts = most_useful_current_level_Apps_exploded.groupby(["current_level", "most_useful_current_level_Apps"]).size().unstack(fill_value=0)

most_useful_current_level_Apps_counts["n"] = level_counts

most_useful_current_level_Apps_normalized_df = most_useful_current_level_Apps_counts.div(level_counts, axis=0)

most_useful_current_level_Apps_percentage_df = most_useful_current_level_Apps_normalized_df * 100
most_useful_current_level_Apps_percentage_df = most_useful_current_level_Apps_percentage_df.round(3)  # Optional: round to 1 decimal place

print(most_useful_current_level_Apps_percentage_df)


# In[32]:


most_useful_current_level_Apps_counts.T


# In[ ]:





# In[33]:


plt.figure(figsize=(10, 6))
sns.heatmap(most_useful_current_level_Apps_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Most useful current level app per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Most useful app")
plt.tight_layout()
plt.show()


# ### Features

# In[34]:


# Most useful features per level

most_useful_features_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("most_useful_features_Apps")

most_useful_features_counts = most_useful_features_exploded.groupby(["current_level", "most_useful_features_Apps"]).size().unstack(fill_value=0)

most_useful_features_normalized_df = most_useful_features_counts.div(level_counts, axis=0)

most_useful_features_percentage_df = most_useful_features_normalized_df * 100
most_useful_features_percentage_df = most_useful_features_percentage_df.round(3)

print(most_useful_features_percentage_df)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(most_useful_features_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Most useful features per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Most useful feature")
plt.tight_layout()
plt.show()


# In[35]:


most_useful_features_counts.T


# In[36]:


# Least useful features per level

least_useful_features_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("least_useful_features_Apps")

least_useful_features_counts = least_useful_features_exploded.groupby(["current_level", "least_useful_features_Apps"]).size().unstack(fill_value=0)

least_useful_features_normalized_df = least_useful_features_counts.div(level_counts, axis=0)

least_useful_features_percentage_df = least_useful_features_normalized_df * 100
least_useful_features_percentage_df = least_useful_features_percentage_df.round(3)

print(least_useful_features_percentage_df)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(least_useful_features_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Least useful features per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Least useful feature")
plt.tight_layout()
plt.show()


# In[37]:


least_useful_features_counts["n"] = level_counts  # Adds N per level

least_useful_features_counts.T


# In[38]:


# No longer useful features per level

no_longer_useful_features_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("no_longer_useful_Apps")

no_longer_useful_features_counts = no_longer_useful_features_exploded.groupby(["current_level", "no_longer_useful_Apps"]).size().unstack(fill_value=0)

no_longer_useful_features_normalized_df = no_longer_useful_features_counts.div(level_counts, axis=0)

no_longer_useful_features_percentage_df = no_longer_useful_features_normalized_df * 100
no_longer_useful_features_percentage_df = no_longer_useful_features_percentage_df.round(3)

print(no_longer_useful_features_percentage_df)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(no_longer_useful_features_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("No longer useful features per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("No longer useful feature")
plt.tight_layout()
plt.show()


# In[39]:


no_longer_useful_features_counts["n"] = level_counts  # Adds N per level

no_longer_useful_features_counts.T


# In[40]:


# No longer useful features per level

skill_improvement_usage_habits_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("skill_improvement_usage_habits_Apps")

skill_improvement_usage_habits_counts = skill_improvement_usage_habits_exploded.groupby(["current_level", "skill_improvement_usage_habits_Apps"]).size().unstack(fill_value=0)

skill_improvement_usage_habits_normalized_df = skill_improvement_usage_habits_counts.div(level_counts, axis=0)

skill_improvement_usage_habits_percentage_df = skill_improvement_usage_habits_normalized_df * 100
skill_improvement_usage_habits_percentage_df = skill_improvement_usage_habits_percentage_df.round(3)

print(skill_improvement_usage_habits_percentage_df)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(skill_improvement_usage_habits_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Changes in app usage over time per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Changes in app usage")
plt.tight_layout()
plt.show()


# In[41]:


skill_improvement_usage_habits_counts["n"] = level_counts

skill_improvement_usage_habits_counts.T


# In[42]:


# No longer useful features per level

feel_apps_help_Apps_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("feel_apps_help_Apps")

feel_apps_help_Apps_exploded_counts = feel_apps_help_Apps_exploded.groupby(["current_level", "feel_apps_help_Apps"]).size().unstack(fill_value=0)

feel_apps_help_Apps_exploded_normalized_df = feel_apps_help_Apps_exploded_counts.div(level_counts, axis=0)

feel_apps_help_Apps_exploded_percentage_df = feel_apps_help_Apps_exploded_normalized_df * 100
feel_apps_help_Apps_exploded_percentage_df = feel_apps_help_Apps_exploded_percentage_df.round(3)

print(feel_apps_help_Apps_exploded_percentage_df)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(feel_apps_help_Apps_exploded_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Do participants feel apps help them per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Apps helpfulness")
plt.tight_layout()
plt.show()


# In[43]:


feel_apps_help_Apps_exploded_counts["n"] = level_counts

feel_apps_help_Apps_exploded_counts.T


# In[44]:


# No longer useful features per level

why_continue_usage_Apps_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&(survey_results_clean["has_participant_used_apps"] == True)].explode("why_continue_usage_Apps")

why_continue_usage_Apps_exploded_counts = why_continue_usage_Apps_exploded.groupby(["current_level", "why_continue_usage_Apps"]).size().unstack(fill_value=0)

why_continue_usage_Apps_exploded_normalized_df = why_continue_usage_Apps_exploded_counts.div(level_counts, axis=0)

why_continue_usage_Apps_exploded_percentage_df = why_continue_usage_Apps_exploded_normalized_df * 100
why_continue_usage_Apps_exploded_percentage_df = why_continue_usage_Apps_exploded_percentage_df.round(3)

print(why_continue_usage_Apps_exploded_percentage_df)

# Plot
plt.figure(figsize=(10, 8))
sns.heatmap(why_continue_usage_Apps_exploded_percentage_df, annot=True, fmt=".1f", cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Percentage (%)'})
plt.title("Why do participants continue using apps per JLPT Level (in %)")
plt.ylabel("JLPT Level")
plt.xlabel("Reason for continuing")
plt.tight_layout()
plt.show()


# In[45]:


why_continue_usage_Apps_exploded_counts["n"] = level_counts

why_continue_usage_Apps_exploded_counts.T


# # WRQ3: What is the correlation between the JLPT wordlists and the wordlists in these GLA's?

# In[47]:


print(wordlist)


# In[ ]:





# In[48]:


from matplotlib_venn import venn3

# Calculate overlaps
duolingo_words = set(wordlist[wordlist['Duolingo_Words'] == 1]['Word'])
jlpt_words = set(wordlist[wordlist['JLPT_Words'] == 1]['Word'])
top_10k_words = set(wordlist.iloc[:10000]['Word'])


# Venn diagram
plt.figure(figsize=(8, 8))
venn = venn3([duolingo_words, jlpt_words, top_10k_words], 
             (f'Duolingo ({len(duolingo_words)} words)', 
              f'JLPT ({len(jlpt_words)} words)', 
              f'Top 10K Words ({len(top_10k_words)} words)'))
plt.title("Overlap of Duolingo, JLPT, and Top 10K Words")
plt.show()


# In[49]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.patches as mpatches

# Extract sets
duolingo_words = set(wordlist[wordlist['Duolingo_Words'] == 1]['Word'])
jlpt_words = set(wordlist[wordlist['JLPT_Words'] == 1]['Word'])
top_10k_words = set(wordlist.iloc[:10000]['Word'])

# Venn diagram
plt.figure(figsize=(8, 8))
venn = venn3([duolingo_words, jlpt_words, top_10k_words], ('', '', ''))  # No circle labels

# Update labels with actual word counts
venn.get_label_by_id('100').set_text(len(duolingo_words - jlpt_words - top_10k_words))  # Only Duolingo
venn.get_label_by_id('010').set_text(len(jlpt_words - duolingo_words - top_10k_words))  # Only JLPT
venn.get_label_by_id('001').set_text(len(top_10k_words - duolingo_words - jlpt_words))  # Only Top 10K
venn.get_label_by_id('110').set_text(len(duolingo_words & jlpt_words - top_10k_words))  # Duolingo & JLPT
venn.get_label_by_id('011').set_text(len(jlpt_words & top_10k_words - duolingo_words))  # JLPT & Top 10K
venn.get_label_by_id('101').set_text(len(duolingo_words & top_10k_words - jlpt_words))  # Duolingo & Top 10K
venn.get_label_by_id('111').set_text(len(duolingo_words & jlpt_words & top_10k_words))  # All three

# Title
plt.title("Overlap of Duolingo, JLPT, and Top 10K Words")

# Create a custom legend with counts in the labels
duolingo_patch = mpatches.Patch(color=venn.get_patch_by_id('100').get_facecolor(), label=f'Duolingo ({len(duolingo_words)} words)')
jlpt_patch = mpatches.Patch(color=venn.get_patch_by_id('010').get_facecolor(), label=f'JLPT ({len(jlpt_words)} words)')
top_10k_patch = mpatches.Patch(color=venn.get_patch_by_id('001').get_facecolor(), label=f'Top 10K Words ({len(top_10k_words)} words)')

# Position the legend outside the plot to the right
plt.legend(handles=[duolingo_patch, jlpt_patch, top_10k_patch], loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


# In[50]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.patches as mpatches

# Extract boolean masks
is_duolingo = wordlist['Duolingo_Words'] == 1
is_jlpt = wordlist['JLPT_Words'] == 1
is_top_10k = wordlist.index < 10000  # Top 10K is just first 10K rows

# Compute actual sets
only_duolingo = wordlist[is_duolingo & ~is_jlpt & ~is_top_10k]
only_jlpt = wordlist[is_jlpt & ~is_duolingo & ~is_top_10k]
only_top_10k = wordlist[is_top_10k & ~is_duolingo & ~is_jlpt]
duolingo_jlpt = wordlist[is_duolingo & is_jlpt & ~is_top_10k]
jlpt_top_10k = wordlist[is_jlpt & is_top_10k & ~is_duolingo]
duolingo_top_10k = wordlist[is_duolingo & is_top_10k & ~is_jlpt]
all_three = wordlist[is_duolingo & is_jlpt & is_top_10k]

# Print to verify correctness
print(f"JLPT Words (Expected: 7033): {wordlist[is_jlpt]['Word'].count()}")
print(f"Only JLPT: {only_jlpt.shape[0]}")
print(f"Only Duolingo: {only_duolingo.shape[0]}")
print(f"Only Top 10K: {only_top_10k.shape[0]}")
print(f"Duolingo & JLPT: {duolingo_jlpt.shape[0]}")
print(f"JLPT & Top 10K: {jlpt_top_10k.shape[0]}")
print(f"Duolingo & Top 10K: {duolingo_top_10k.shape[0]}")
print(f"All Three: {all_three.shape[0]}")

# Create Venn diagram
plt.figure(figsize=(8, 8))
venn = venn3([set(wordlist[is_duolingo]['Word']),
              set(wordlist[is_jlpt]['Word']),
              set(wordlist[is_top_10k]['Word'])], ('Duolingo', 'JLPT', 'Top 10K'))

# Update labels
venn.get_label_by_id('100').set_text(only_duolingo.shape[0])
venn.get_label_by_id('010').set_text(only_jlpt.shape[0])
venn.get_label_by_id('001').set_text(only_top_10k.shape[0])
venn.get_label_by_id('110').set_text(duolingo_jlpt.shape[0])
venn.get_label_by_id('011').set_text(jlpt_top_10k.shape[0])
venn.get_label_by_id('101').set_text(duolingo_top_10k.shape[0])
venn.get_label_by_id('111').set_text(all_three.shape[0])

# Title
plt.title("Overlap of Duolingo, JLPT, and Top 10K Words")

# Custom legend
duolingo_patch = mpatches.Patch(color=venn.get_patch_by_id('100').get_facecolor(), label=f'Duolingo ({wordlist[is_duolingo]["Word"].nunique()} words)')
jlpt_patch = mpatches.Patch(color=venn.get_patch_by_id('010').get_facecolor(), label=f'JLPT ({wordlist[is_jlpt]["Word"].count()} words)')
top_10k_patch = mpatches.Patch(color=venn.get_patch_by_id('001').get_facecolor(), label=f'Top 10K ({wordlist[is_top_10k]["Word"].nunique()} words)')

plt.legend(handles=[duolingo_patch, jlpt_patch, top_10k_patch], loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


# In[51]:


with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(wordlist[wordlist['JLPT_Words'] == 1]['Word'].value_counts().sum())


# In[52]:


wordlist[wordlist["Word"]=="食べ"].tail(50)


# In[53]:


# Identify JLPT words not in Duolingo
gap_words = wordlist[(wordlist['JLPT_Words'] == 1) & (wordlist['Duolingo_Words'] == 0)]
print(f"Number of JLPT words not covered by Duolingo: {len(gap_words)}")
print(gap_words.head())


# In[54]:


# Calculate cumulative frequency contribution
df_sorted = wordlist.sort_values(by='Rank')
df_sorted['Cumulative_Frequency'] = df_sorted['Occurrences'].cumsum()

df_sorted['JLPT_Contribution'] = df_sorted.groupby('JLPT_Level')['Occurrences'].cumsum()

pivot_area = df_sorted.pivot_table(index='Rank', columns='JLPT_Level', values='Occurrences', aggfunc='sum')

pivot_area.plot.area(stacked=True, colormap='viridis', figsize=(10, 6))
plt.title('Word Frequency Contribution by JLPT Level')
plt.ylabel('Cumulative Word Frequency')
plt.xlabel('Word Rank')
plt.legend(title='JLPT Level')
plt.show()


# In[55]:


get_ipython().system('pip install wordcloud')

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
def make_word_cloud(words_freq_dict):
  # setup Japanese font for creating the word cloud
  font_path = 'NotoSansJP-Light.ttf'
  # create an image with a Word Cloud with the given word frequencies
  wordcloud = WordCloud(width=1500,
                        height=1000,
                        max_words=900,
                        colormap='PuBu',
                        font_path=font_path,
                        normalize_plurals=True).generate_from_frequencies(words_freq_dict)
  # setup a plot frame without any axis and print the image generated above  
  plt.figure(figsize=(17,14))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()

# Convert df_sorted into the required dictionary format
freq_dict = dict(zip(df_sorted['Word'], df_sorted['Occurrences']))
make_word_cloud(freq_dict)


# In[56]:


# Count words by JLPT Level
jlpt_counts = wordlist['JLPT_Level'].value_counts()

# Plot
plt.figure(figsize=(8, 8))
plt.pie(jlpt_counts, labels=jlpt_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('PuBu'))
plt.title('Word Count Breakdown by JLPT Level')
plt.show()


# In[57]:


# Filter words taught by Duolingo
duolingo_words = df_sorted[df_sorted['Duolingo_Words'] == 1]

# Count words per JLPT level for Duolingo
jlpt_duolingo = duolingo_words['JLPT_Level'].value_counts().sort_index()

# Plot Duolingo coverage by JLPT Level
plt.figure(figsize=(10, 6))
jlpt_duolingo.plot(kind='bar', color='orange')
plt.title("Duolingo Word Coverage by JLPT Level")
plt.xlabel("JLPT Level")
plt.ylabel("Number of Words Covered")
plt.xticks(rotation=0)
plt.show()


# In[58]:


plt.figure(figsize=(12, 6))

# Plot Duolingo Coverage
plt.plot(df_sorted['Rank'], df_sorted['Duolingo_Words'].cumsum(), label="Duolingo Coverage", color='green')

# Plot JLPT Coverage
plt.plot(df_sorted['Rank'], df_sorted['JLPT_Words'].cumsum(), label="JLPT Coverage", color='blue')

plt.xlabel("Word Rank")
plt.ylabel("Cumulative Words Covered")
plt.title("Duolingo vs JLPT Word Coverage by Rank")
plt.legend()
plt.show()


# In[59]:


import seaborn as sns

df_sorted['Rank_Bin'] = pd.cut(df_sorted['Rank'], bins=range(0, 11000, 1000), right=False)

heatmap_data = pd.pivot_table(df_sorted, values='JLPT_Words', index='Rank_Bin', columns='JLPT_Level', aggfunc='sum', fill_value=0)

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='d')
plt.title("JLPT Word Coverage Across Word Rank Segments")
plt.xlabel("JLPT Level")
plt.ylabel("Word Rank Segments")
plt.show()


# In[60]:


total_occurrences = df_sorted['Occurrences'].sum()

df_sorted['Cumulative_Duolingo'] = df_sorted['Duolingo_Words'] * df_sorted['Occurrences']
df_sorted['Cumulative_JLPT'] = df_sorted['JLPT_Words'] * df_sorted['Occurrences']

df_sorted['Duolingo_Percent'] = df_sorted['Cumulative_Duolingo'].cumsum() / total_occurrences * 100
df_sorted['JLPT_Percent'] = df_sorted['Cumulative_JLPT'].cumsum() / total_occurrences * 100

plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Rank'], df_sorted['Duolingo_Percent'], label="Duolingo Coverage", color='green')
plt.plot(df_sorted['Rank'], df_sorted['JLPT_Percent'], label="JLPT Coverage", color='blue')
plt.xlabel("Word Rank")
plt.ylabel("Cumulative Percentage of Word Occurrences")
plt.title("Cumulative Frequency Coverage: Duolingo vs JLPT")
plt.legend()
plt.show()


# In[61]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Combined_Wordlist.csv')
df = df.sort_values(by='Rank')

df['Cumulative_Occurrences'] = df['Occurrences'].cumsum()
df['Coverage_Percentage'] = df['Cumulative_Occurrences'] / df['Occurrences'].sum() * 100

plt.figure(figsize=(10, 6))
plt.plot(df['Rank'], df['Coverage_Percentage'], label='Cumulative Coverage')
plt.axhline(y=80, color='r', linestyle='--', label='80% Threshold')
plt.axhline(y=95, color='g', linestyle='--', label='95% Threshold')
plt.axhline(y=98, color='b', linestyle='--', label='98% Threshold')
plt.xlabel('Word Rank')
plt.ylabel('Cumulative Coverage (%)')
plt.title('Cumulative Vocabulary Coverage')
plt.legend()
plt.show()


# In[62]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Combined_Wordlist.csv')
df = df.sort_values(by='Rank')

df['Cumulative_Occurrences'] = df['Occurrences'].cumsum()
df['Coverage_Percentage'] = df['Cumulative_Occurrences'] / df['Occurrences'].sum() * 100

plt.figure(figsize=(10, 6))
plt.plot(df['Rank'], df['Coverage_Percentage'], label='Cumulative Coverage')
plt.axhline(y=80, color='r', linestyle='--', label='80% Threshold')
plt.axhline(y=95, color='g', linestyle='--', label='95% Threshold')
plt.axhline(y=98, color='b', linestyle='--', label='98% Threshold')

thresholds = [80, 95, 98]
for threshold in thresholds:
    threshold_rank = df[df['Coverage_Percentage'] >= threshold].iloc[0]['Rank']
    plt.axvline(x=threshold_rank, color='black', linestyle=':', label=f'{threshold}% at {threshold_rank.astype(int)} words')

plt.xlabel('Word Rank')
plt.ylabel('Cumulative Coverage (%)')
plt.title('Cumulative Vocabulary Coverage')

plt.legend()
plt.show()


# In[63]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given values for words required to reach certain proficiency levels
proficiency_levels = [0, 80, 95, 98]
words_required = [0, 1452, 5697, 7872]

def exp_func(x, a, b):
    return a * np.exp(b * x)

params, covariance = curve_fit(exp_func, proficiency_levels, words_required, p0=(1, 0.05))

x_range = np.arange(0, 101, 1)
y_pred = exp_func(x_range, *params)

plt.figure(figsize=(10, 6))
plt.plot(x_range, y_pred, label='Predicted Word Count for Proficiency', color='blue')

plt.scatter(proficiency_levels, words_required, color='red', label='Given Data Points')

plt.axvline(x=80, color='r', linestyle='--', label='80% Threshold')
plt.axvline(x=95, color='g', linestyle='--', label='95% Threshold')
plt.axvline(x=98, color='b', linestyle='--', label='98% Threshold')

plt.title('Predicted Word Count for Different Proficiency Levels (Exponential Fit)')
plt.xlabel('Proficiency (%)')
plt.ylabel('Words Required')
plt.legend()

plt.show()

predicted_99 = exp_func(99, *params)
predicted_100 = exp_func(100, *params)

print(f'Predicted words for 99% proficiency: {predicted_99}')
print(f'Predicted words for 100% proficiency: {predicted_100}')


# In[64]:


print(wordlist[["Rank","Occurrences","Duolingo_Words","JLPT_Words"]].corr())

corr_matrix = wordlist[["Rank", "Occurrences", "Duolingo_Words", "JLPT_Words"]].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

plt.title('Correlation Matrix')
plt.show()


# ## When start intermediate plateau?
# This should not be percentages!

# In[70]:


# No longer useful features per level
# Level counts for all the situations where non-app users need to be filtered out
level_counts_intermediatePlateau = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know") &
                                                        ((survey_results_clean["experienced_intermediate_plateau_Apps"] == True) |
                                                        (survey_results_clean["experienced_intermediate_plateau_noApps"] == True))]["current_level"].value_counts().sort_index()

intermediatePlateau_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&((survey_results_clean['experienced_intermediate_plateau_noApps']==True)|(survey_results_clean['experienced_intermediate_plateau_Apps']==True))].explode("when_start_intermediatePlateau")

participants_experienced_intermediatePlateau = (intermediatePlateau_exploded['experienced_intermediate_plateau_Apps'].value_counts()+intermediatePlateau_exploded['experienced_intermediate_plateau_noApps'].value_counts())

intermediatePlateau_exploded_counts = intermediatePlateau_exploded.groupby(["current_level", "when_start_intermediatePlateau"]).size().unstack(fill_value=0)

print(intermediatePlateau_exploded_counts)

# Mean, median etc is based on what each level gave as reply, so columns are "mean", "median", "sd", "mode"

intermediatePlateau_mean = participants_experienced_intermediatePlateau
#print(intermediatePlateau_exploded_counts.value_counts())


# In[71]:


from scipy import stats

index = intermediatePlateau_exploded_counts.index
columns = intermediatePlateau_exploded_counts.columns.astype(int)

means, medians, std_devs, modes, counts = [], [], [], [], []

for i, row in intermediatePlateau_exploded_counts.iterrows():
    values = []
    weights = []
    for year in columns:
        count = row[str(year)] if str(year) in row else 0
        if count > 0:
            values.extend([year] * int(count))
            weights.append(int(count))
    values_array = np.array(values)

    if len(values_array) > 0:
        means.append(np.average(values_array))
        medians.append(np.median(values_array))
        std_devs.append(np.std(values_array, ddof=1))
        mode_result = stats.mode(values_array, keepdims=True)
        modes.append(mode_result.mode[0])
        counts.append(len(values_array))
    else:
        means.append(np.nan)
        medians.append(np.nan)
        std_devs.append(np.nan)
        modes.append(np.nan)
        counts.append(0)

# Assemble into DataFrame
stats_df = pd.DataFrame({
    "n": counts,
    "mean": means,
    "median": medians,
    "std_dev": std_devs,
    "mode": modes
}, index=index)

print(stats_df)


# In[72]:


from scipy import stats
import numpy as np
import pandas as pd

index = intermediatePlateau_exploded_counts.index
columns = intermediatePlateau_exploded_counts.columns.astype(int)

means, medians, std_devs, modes, counts = [], [], [], [], []
actual_counts = {str(year): [] for year in columns}

for i, row in intermediatePlateau_exploded_counts.iterrows():
    values = []
    weights = []
    for year in columns:
        count = row[str(year)] if str(year) in row else 0
        if count > 0:
            values.extend([year] * int(count))
            weights.append(int(count))
        actual_counts[str(year)].append(count)

    values_array = np.array(values)

    if len(values_array) > 0:
        means.append(np.average(values_array))
        medians.append(np.median(values_array))
        std_devs.append(np.std(values_array, ddof=1))
        mode_result = stats.mode(values_array, keepdims=True)
        modes.append(mode_result.mode[0])
        counts.append(len(values_array))
    else:
        means.append(np.nan)
        medians.append(np.nan)
        std_devs.append(np.nan)
        modes.append(np.nan)
        counts.append(0)

stats_df = pd.DataFrame({
    "n": counts,
    "mean": means,
    "median": medians,
    "std_dev": std_devs,
    "mode": modes
}, index=index)

counts_df = pd.DataFrame(actual_counts, index=index)

print("Statistical Summary:")
print(stats_df)

print("\nActual Counts Table:")
print(counts_df)


# In[73]:


import matplotlib.pyplot as plt
import seaborn as sns

stats_df = stats_df.sort_index()

plt.figure(figsize=(12, 6))
sns.barplot(x=stats_df.index, y=stats_df["mean"], palette="PuBu")

for i, (mean, n) in enumerate(zip(stats_df["mean"], stats_df["n"])):
    plt.text(i, mean + 0.1, f"n={int(n)}", ha='center', va='bottom', fontsize=9)

plt.title("Mean Intermediate Plateau Starting Point by Current Level")
plt.ylabel("Mean Plateau Start in years of studying")
plt.xlabel("Current Proficiency Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[74]:


statsinverted_df = stats_df.iloc[::-1]
statsinverted_df


# In[75]:


stats_df


# In[76]:


plt.figure(figsize=(12, 6))

plt.plot(statsinverted_df.index, statsinverted_df["mean"], label="Mean", marker="o")
plt.plot(statsinverted_df.index, statsinverted_df["median"], label="Median", marker="s")
plt.plot(statsinverted_df.index, statsinverted_df["mode"], label="Mode", marker="^")

plt.title("Plateau Onset Statistics by Current Level")
plt.ylabel("Years of studying")
plt.xlabel("Current Proficiency Level")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# In[77]:


plt.figure(figsize=(12, 6))

plt.plot(stats_df.index, stats_df["mean"], label="Mean", marker="o")
plt.plot(stats_df.index, stats_df["median"], label="Median", marker="s")
plt.plot(stats_df.index, stats_df["mode"], label="Mode", marker="^")

plt.title("Plateau Onset Statistics by Current Level")
plt.ylabel("Years of studying")
plt.xlabel("Current Proficiency Level")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# In[78]:


plt.figure(figsize=(12, 6))

plt.errorbar(stats_df.index, stats_df["mean"], yerr=stats_df["std_dev"], fmt="o", capsize=5, label="Mean ± SD")

plt.title("Mean Plateau Start with Standard Deviation")
plt.ylabel("Years of studying")
plt.xlabel("Current Proficiency Level")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# ##  What level did the intermediate plateau start?
# ##  Change this, this way of looking at the data doesn't make sense

# In[79]:


# No longer useful features per level

intermediatePlateau_exploded = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&((survey_results_clean['experienced_intermediate_plateau_noApps']==True)|(survey_results_clean['experienced_intermediate_plateau_Apps']==True))].explode("what_level_start_intermediatePlateau")

participants_experienced_intermediatePlateau = (intermediatePlateau_exploded['experienced_intermediate_plateau_Apps'].value_counts()+intermediatePlateau_exploded['experienced_intermediate_plateau_noApps'].value_counts())

intermediatePlateau_exploded_counts = intermediatePlateau_exploded.groupby(["current_level", "what_level_start_intermediatePlateau"]).size().unstack(fill_value=0)

print(intermediatePlateau_exploded_counts)

intermediatePlateau_mean = participants_experienced_intermediatePlateau


# In[80]:


stats_df = pd.DataFrame(index=intermediatePlateau_exploded_counts.index)
stats_df["n"] = intermediatePlateau_exploded_counts.sum(axis=1)
stats_df["mean"] = intermediatePlateau_exploded_counts.mean(axis=1)
stats_df["median"] = intermediatePlateau_exploded_counts.median(axis=1)
stats_df["std_dev"] = intermediatePlateau_exploded_counts.std(axis=1)
stats_df["mode"] = intermediatePlateau_exploded_counts.mode(axis=1)[0]  # take first mode if multiple

print(stats_df)


# In[81]:


# Compute statistical summary
stats_df = pd.DataFrame(index=intermediatePlateau_exploded_counts.index)
stats_df["n"] = intermediatePlateau_exploded_counts.sum(axis=1)
stats_df["mean"] = intermediatePlateau_exploded_counts.mean(axis=1)
stats_df["median"] = intermediatePlateau_exploded_counts.median(axis=1)
stats_df["std_dev"] = intermediatePlateau_exploded_counts.std(axis=1)
stats_df["mode"] = intermediatePlateau_exploded_counts.mode(axis=1).iloc[:, 0]  # Take first mode if multiple

# Store actual counts per category in a separate table
counts_df = intermediatePlateau_exploded_counts.copy()

# Print both tables
print("Statistical Summary:")
print(stats_df)

print("\nActual Counts Table:")
print(counts_df)


# In[ ]:





# In[82]:


intermediate_plateau_data = survey_results_clean[(survey_results_clean["current_level"] != "I really don't know")&((survey_results_clean['experienced_intermediate_plateau_noApps']==True)|(survey_results_clean['experienced_intermediate_plateau_Apps']==True))]

data = intermediate_plateau_data[["current_level", "what_level_start_intermediatePlateau"]]

df = pd.DataFrame(data)

df_filtered = df[df["current_level"] != "I really don't know"]

df_exploded = df_filtered.explode("what_level_start_intermediatePlateau")

count_table  = pd.crosstab(df_exploded["current_level"], df_exploded["what_level_start_intermediatePlateau"])

n_values = count_table.sum(axis=1)

percentage_table = count_table.div(count_table.sum(axis=1), axis=0) * 100

percentage_table["n"] = n_values

count_table["n"] = n_values

column_order = ["JLPT N1", "JLPT N2", "JLPT N3", "JLPT N4", "JLPT N5", "I do not know", "n"]
percentage_table = percentage_table.reindex(columns=column_order, fill_value=0)
count_table = count_table.reindex(columns=column_order, fill_value=0)

count_table


# In[83]:


import matplotlib.pyplot as plt
import seaborn as sns

counts_percentage_df = intermediatePlateau_exploded_counts.div(intermediatePlateau_exploded_counts.sum(axis=1), axis=0) * 100

column_order = ["JLPT N1", "JLPT N2", "JLPT N3", "JLPT N4", "JLPT N5", "I do not know"]
counts_percentage_df = counts_percentage_df.reindex(columns=column_order, fill_value=0)

plt.figure(figsize=(10, 6))
sns.heatmap(counts_percentage_df, annot=True, fmt=".1f", cmap="Blues", linewidths=0.5, cbar_kws={"label": "Percentage (%)"})

plt.title("Distribution of Responses per JLPT Level (in %)")
plt.ylabel("Current JLPT Level")
plt.xlabel("Started at")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ##  features_helping_intermediatePlateau

# In[84]:


intermediate_plateau_data.groupby("current_level")["features_helping_intermediatePlateau"].value_counts()


# In[85]:


features_helping_counts = pd.crosstab(
    intermediate_plateau_data["current_level"], 
    intermediate_plateau_data["features_helping_intermediatePlateau"]
)

features_helping_counts["n"] = features_helping_counts.sum(axis=1)

features_helping_counts.reset_index(inplace=True)

column_order = ["current_level","Yes", "No", "Not sure", "n"]
features_helping_counts = features_helping_counts.reindex(columns=column_order, fill_value=0)

print(features_helping_counts)


# In[86]:


features_helping_counts


# In[87]:


import matplotlib.pyplot as plt

colors = {"Yes": "green", "No": "red", "Not sure": "gray"}

ax = features_helping_counts.set_index("current_level")[["Yes", "No", "Not sure"]].plot(
    kind="bar",
    stacked=True,
    color=[colors[col] for col in ["Yes", "No", "Not sure"]],
    figsize=(10, 6),
)

plt.xlabel("JLPT Level")
plt.ylabel("Response Count")
plt.title("Responses to Features Helping with Intermediate Plateau per JLPT Level")
plt.xticks(rotation=45)
plt.legend(title="Response Type")

plt.show()


# In[88]:


import matplotlib.pyplot as plt
import seaborn as sns

features_helping_percentage = features_helping_counts.set_index("current_level").div(
    features_helping_counts["n"], axis=0
) * 100

features_helping_percentage = features_helping_percentage.drop(columns=["n"])

plt.figure(figsize=(8, 6))
sns.heatmap(
    features_helping_percentage, 
    annot=True, 
    fmt=".1f", 
    cmap="Blues", 
    linewidths=0.5, 
    cbar_kws={"label": "Percentage (%)"}
)

plt.title("Impact of Features on Overcoming the Intermediate Plateau (%)")
plt.ylabel("Current JLPT Level")
plt.xlabel("Response")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

plt.show()


# In[89]:


print(features_helping_counts.columns)


# ## apps_enough_advanced_content_intermediatePlateau

# In[90]:


intermediate_plateau_data["apps_enough_advanced_content_intermediatePlateau"].value_counts()


# In[91]:


advanced_enough_counts = pd.crosstab(
    intermediate_plateau_data["current_level"], 
    intermediate_plateau_data["apps_enough_advanced_content_intermediatePlateau"]
)

advanced_enough_counts["n"] = advanced_enough_counts.sum(axis=1)

advanced_enough_counts.reset_index(inplace=True)

column_order = ["current_level","Yes", "No", "Not sure", "n"]
advanced_enough_counts = advanced_enough_counts.reindex(columns=column_order, fill_value=0)

print(advanced_enough_counts)


# In[92]:


advanced_enough_counts


# In[93]:


import matplotlib.pyplot as plt

colors = {"Yes": "green", "No": "red", "Not sure": "gray"}

ax = advanced_enough_counts.set_index("current_level")[["Yes", "No", "Not sure"]].plot(
    kind="bar",
    stacked=True,
    color=[colors[col] for col in ["Yes", "No", "Not sure"]],
    figsize=(10, 6),
)

plt.xlabel("JLPT Level")
plt.ylabel("Response Count")
plt.title("Responses to Features Helping with Intermediate Plateau per JLPT Level")
plt.xticks(rotation=45)
plt.legend(title="Response Type")

plt.show()


# # Qualitative results

# In[94]:


survey_results_clean.columns


# In[95]:


with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(survey_results_clean[survey_results_clean["why_other_tools_noApps"].notna()]["why_other_tools_noApps"])


# In[96]:


with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(survey_results_clean[survey_results_clean["overcoming_challenges_noApps"].notna()]["overcoming_challenges_noApps"])


# In[97]:


with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(survey_results_clean[survey_results_clean["tried_techniques_to_combat_intermediatePlateau"]!= "nan"]["tried_techniques_to_combat_intermediatePlateau"])


# In[98]:


with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(survey_results_clean[survey_results_clean["most_challenging_to_progress_intermediatePlateau"]!= "nan"]["most_challenging_to_progress_intermediatePlateau"])


# In[99]:


non_app_users_JLPT = survey_results_clean[survey_results_clean["has_participant_used_apps"]==False]

# Study methods

# Step 2: Count occurrences of each study method per JLPT level
non_app_users_JLPT_counts = non_app_users_JLPT.groupby(["current_level", "has_participant_used_apps"]).size().unstack(fill_value=0)

non_app_users_JLPT_counts

