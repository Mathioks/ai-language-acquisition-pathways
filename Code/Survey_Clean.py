#!/usr/bin/env python
# coding: utf-8

# # Importing the survey results
# Get overview of all the different columns in the dataset & remove last three columns regarding whether participants would like to stay updated, receive the final report, and in case they do, where they give their contact details. As this data is only necessary for contacting users at the end, not for the data aggregation.
# 

# In[ ]:


import pandas as pd

survey_results = pd.read_csv("日本語学習者のプロフィール_V3.csv", encoding = "utf-8")


# In[2]:


survey_results.drop(columns={'Would you like to receive updates regarding this research?',
       'Would you like to receive the final report of this research?',
       'If you wish to be updated, please enter your contact details below.'}, inplace=True)

print(survey_results.columns)


# In[3]:


## Start Cleanup: Renaming columns for easy working
survey_results.rename(columns={'What is your current Japanese level? (self-assessment is fine)': 'current_level',
       'How long have you been studying Japanese?': 'study_years',
       'What is (are) your native language(s)?': 'native_languages',
       'What other language(s) do you know?': 'other_languages',
       'How do you primarily learn Japanese?  (Select all that apply)': 'main_study_method',
       'What are your main goals for learning Japanese?': 'study_goals',
       'Have you used any Language Learning Apps?': 'has_participant_used_apps',
       "Is there a reason why you haven't used any language learning apps?": "reason_noApps",
       'Have you considered using any of the following Language Learning Apps? (Select all that apply)': 'considered_using_noApps',
       'Would you be open to trying a Language Learning App if it could help you overcome any specific challenges in your current learning process? If yes, which features would you look for? (Select all that apply)': 'use_to_overcome_challenges_noApps',
       'Have you tried other digital tools for learning Japanese?': 'other_tools_noApps',
       'If you have tried other digital tools, why did you prefer them to Language Learning Apps? (optional)': 'why_other_tools_noApps',
       'What tools or methods do you find most effective for learning Japanese without apps?  (Select all that apply)': 'most_effective_noApps',
       'What tools or methods do you find least effective for learning Japanese without apps? (Select all that apply)': 'least_effective_noApps',
       'How do you typically overcome learning challenges, such as lack of motivation, limited resources, or difficulty with grammar and vocabulary?': 'overcoming_challenges_noApps',
       'How much time do you typically dedicate to studying Japanese each day?': 'daily_study_time_noApps',
       'Do you have a structured study plan or prefer a more flexible learning approach?': 'structured_vs_flexible_learning_noApps',
       'Have you ever felt like you are getting stuck in your language learning journey? (The feeling of progress slowing down despite effort)': 'experienced_intermediate_plateau_Apps',
       'Have you used any of the following language apps? (Select all that apply)': 'used_apps_Apps',
       'Which of these apps have been most helpful in your language learning journey? (Select all that apply)': 'most_useful_Apps',
       'What app do you feel helps you most at your current level? (You can only choose 1)': 'most_useful_current_level_Apps',
       'How often do you use these apps?': 'usage_frequency_Apps',
       'On a day when you use the app(s), how long do you interact with these apps on average in total?': 'daily_study_time_Apps',
       'How have your app usage habits changed over time as your skill level has improved? ': 'skill_improvement_usage_habits_Apps',
       'What are the features you find most useful? (Select all that apply)': 'most_useful_features_Apps',
       'What are the features you find least useful? (Select all that apply)': 'least_useful_features_Apps',
       "Which of these features did you find useful in the past but don't find useful anymore? (Select all that apply)": "no_longer_useful_Apps",
       'Do you feel like Language Learning Apps help you?': 'feel_apps_help_Apps',
       'Why do you continue using Language Learning Apps? (Select all that apply)': 'why_continue_usage_Apps',
       'How much do you enjoy using these apps compared to other studying methods?': 'comparative_enjoyment_other_methods_Apps',
       'Have you ever felt like you are getting stuck in your language learning journey? (The feeling of progress slowing down despite effort).1': 'experienced_intermediate_plateau_noApps',
       'At what point in your learning journey did you start experiencing this feeling of being stuck?': 'when_start_intermediatePlateau',
       'Do you know at what level this started?': 'what_level_start_intermediatePlateau',
       'Do you think gamified features (like points, levels, streaks) are helping you overcome this plateau?': 'features_helping_intermediatePlateau',
       'Do you feel like Language Learning Apps provide enough advanced content to help you improve beyond the intermediate level?': 'apps_enough_advanced_content_intermediatePlateau',
       'What techniques have you tried to combat this? (optional)': 'tried_techniques_to_combat_intermediatePlateau',
       'What do you think is the most challenging part of progressing beyond the intermediate level? (optional)': 'most_challenging_to_progress_intermediatePlateau',
       'How did you find this survey? (Choose the most exact option)': 'how_found_survey_final'}, inplace=True)
print(survey_results)


# # Study Years

# In[4]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['study_years'] = survey_results['study_years'].astype(str).str.strip()

## Print all current values and count them
print(survey_results['study_years'].value_counts())


# In[5]:


## Difficult ones to decide, print the entire row of all the different columns to get more insight in the person's situation
print(survey_results.loc[survey_results['study_years'] == 'On and off for years, but never enough to become competent'])
## Since this person mentions they are still level N5, I will count this as 0 years.
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'Off and on for 10 years'])
## Difficult to decide as they don't know their level either, so will accept their number of 10
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'On and off for about 10 years'])
## They give N3 as level, which, depending on the amount of time spent could fall within a 10 year span
print('----------')
print(survey_results.loc[survey_results['study_years'] == '13 on and off'])
## Again difficult to define, while N4 is rather low for 13 years, everyones goals, time spent etc will vary, will accept the number
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'Tried many times, never learned much, so I could honestly say on and off for the past 4 years but in reality, it’s been only like 4 months'])
## They give both 4 years and 4 months, while I accept "on and off for X amount of years" when that's all I get, in this case the person mentioning their true studying time was only really 4 months, I will accept this number, as it seems the participant chose this as the most accurate representation
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'Technically I started about 10 years ago but didn’t seriously study it until 2024. I ended up becoming fluent in all hiragana and katakana as well as 80 kanji naturally before this point. This year I couldn’t ignore that I was automatically understanding things, so I decided to finally try intentionally studying it this year. I went from 80 to 575 kanji this year.'])
## Seeing as they gave the 2024 start date, I will accept this answer as the most accurate over the 10 years
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'on and off for 20+ years'])
## Any X+ value will be accepted as the value X+1, in this case 20+ becomes 21
print('----------')
print(survey_results.loc[survey_results['study_years'] == 'Not Sure'])
## Given the N5 level and the fact the participant found the survey on the Marumori discord channel, a rather new app only released in 2024, I will count this as 0


# In[ ]:


## Rename 
survey_results['study_years'].replace({
    'Less than 1 year': 0,
    '1 year': 1,
    '2 years': 2,
    '3 years': 3,
    '4 years': 4,
    '5 years': 5,
    '10 years': 10,
    '11 years': 11,
    'Almost 10 years': 9,
    'Over about 10 years but never consistently': 10,
    '7+': 7,
    '7 years': 7,
    'A little over 7 years': 7,
    '1 year and 7 months': 1,
    'On and off for years, less than year actively and purposfully': 0,
    '6 years': 6,
    'since 2004': 21,
    '10+ years': 10,
    'On and off for years, but never enough to become competent': 0,
    '> 5 years': 4,
    'Off and on for 10 years': 10,
    'More than 5 years': 6,
    'On and off for about 10 years': 10,
    '13 on and off': 13,
    'Tried many times, never learned much, so I could honestly say on and off for the past 4 years but in reality, it’s been only like 4 months': 0,
    'Technically I started about 10 years ago but didn’t seriously study it until 2024. I ended up becoming fluent in all hiragana and katakana as well as 80 kanji naturally before this point. This year I couldn’t ignore that I was automatically understanding things, so I decided to finally try intentionally studying it this year. I went from 80 to 575 kanji this year.': 1,
    'more years than I care to remember (twenty? even more?)': 20,
    '18 years': 18,
    '20 years': 20,
    'on and off over a period of 10 years': 10,
    'Over 10 years': 11,
    '7 years': 7,
    'on and off for 20+ years': 21,
    'Not Sure': 0,
    'On and off for 10 Years': 10,
    'On and off for 10 years.': 10,
    'On and off for 10 Years': 10,
    '15 years on-and-off': 15,
    'On & off (mostly off) for the past 20 years': 20,
    '15 years': 15
}, inplace=True)


# In[7]:


## List and count all new values
print(survey_results['study_years'].value_counts())

## The values in the column are now numeric, but these values should not be used for calculation (we cannot divide, multiply, etc the amount of years someone has been studying to come to any useful insights) as such, the column will be kept as a "string" type (object in pandas).
## I no longer agree with this statement, as it is necessary to check whether someone has studied less than X amount of years, for which it will need to be an integer
survey_results['study_years'] = survey_results['study_years'].astype(int)


# In[8]:


## Check datatypes
print(survey_results.dtypes)  # Check data types
print(survey_results.head())  # See sample data


# # Current_Level
# Start going over column per column, looking at the total amount of data, finding outliers, and generalizing data where participants input data differently
# 
# Rename results to become numeral (> 1 year = 0, 1 year = 1, ...)
# 
# 

# In[9]:


print(survey_results['current_level'].value_counts())

## current_level clear


# In[10]:


print(survey_results.loc[survey_results['current_level'] == "I really don't know", 'study_years'])


# In[11]:


# for the participants who gave "I really don't know", if their study years are less than 2, it is very unlikely that their level will be above JLPT N5, as such those will be changed to "JLPT N5" as the "I really don't know" value makes many aggregations done on the participant's data useless

survey_results.loc[
    (survey_results['current_level'] == "I really don't know") & (survey_results['study_years'] < 2), 
    'current_level'
] = "JLPT N5"

print(survey_results.loc[survey_results['current_level'] == "I really don't know", 'study_years'])


# ## Current Level conclusion
# 
# The values where the participant wrote "I really don't know" but has less than 2 years of studying were changed to "JLPT N5", as the odds of them having a higher level are very slim, both because less than 2 years is not that long, and someone who aimed at a high level in a short amount of time is likely to have an idea of their current level. Furthermore doing so makes their data a lot more useful as many aggregations use the JLPT level later down the line.

# # Timestamp

# In[ ]:


## The first column, Timestamp, is still set to string, this should be converted to a datetype
survey_results['Timestamp'] = pd.to_datetime(survey_results['Timestamp'])
print(survey_results.dtypes)  # Check data types
print(survey_results.head())  # See sample data


# # native_languages

# In[13]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['native_languages'] = survey_results['native_languages'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results['native_languages'].value_counts())


# In[ ]:


## Rename 
survey_results['native_languages'].replace({
    'english': 'English',
    'Brazilian Portuguese': 'Portuguese',
    'Malay, English': 'English, Malay',
    'French / English': 'English, French',
    'Filipino (Tagalog)': 'Filipino',
    'Galician, spanish': 'Spanish, Galician',
    'Spanish and Catalan': 'Spanish, Catalan',
    'Italian and English': 'English, Italian',
    'Nederlands': 'Dutch',
    'Swedish, English': 'English, Swedish',
    'Malay and English': 'English, Malay',
    'French/English': 'English, French',
    'English, Mandarin Chinese': 'English, Mandarin',
    'english and hindi': 'English, Hindi',
    'french': 'French',
    '中文': 'Chinese',
    'chinese': 'Chinese',
    'Canadian French': 'French',
    'Mandarin': 'Chinese',
    'Madarin': 'Chinese',
    'Yoruba, English.': 'English, Yoruba',
    'Português': 'Portuguese',
    'English, Mandarin': 'English, Chinese',
}, inplace=True)


# In[15]:


## List and count all new values
print(survey_results['native_languages'].value_counts())

## The values in the column are now numeric, but these values should not be used for calculation (we cannot divide, multiply, etc the amount of years someone has been studying to come to any useful insights) as such, the column will be kept as a "string" type (object in pandas).
## survey_results['study_years'] = survey_results['study_years'].astype(str)


# ## Native_Languages Column conclusion
# 
# #### Some decisions were taken in this part:
# I opted not to separate multiple native languages into individual entries. Doing so would be useful in case I wanted to get insights in how many people spoke a specific language. In this case the idea of what native language each entry spoke is much more interesting to keep
# 
# Dialects like "Brazilian Portuguese" were brought back to "Portuguese" as the specific detailed distinction is not necessary to gather for the research (data minimization)
# 
# When multiple languages included a language that commonly occured in the survey like English or Spanish, that language has been made the first language in the list (for example, "Hindi, English" was turned into "English, Hindi") This was done so that it's easier to see how many of the common languages occurred, as well as being able to get a quick look at the rarer langauges at the end of the list (this was a choice that could have been reversed, this just seemed to make the most sense to me)
# 
# All languages that were entered in a different language (like "Nederlands" for Dutch or "中文" for Chinese) were brough back to English naming conventions

# # Other_Languages

# In[16]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['other_languages'] = survey_results['other_languages'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results['other_languages'].value_counts())


# In[ ]:


import numpy as np
survey_results['other_languages'].replace({
    'none': np.nan,
    'NIL': np.nan,
    'None': np.nan,
    'mome': np.nan,
    'Yeah': np.nan,
    'nan': np.nan,
    'Way too many, besides native languages, 5 languages B1 or higher, ~10 A2, another 10+ A1 level.': np.nan,
    'some French': 'French',
    'Spanish (Elementary level)': 'Spanish',
    'Portuguese, Spanish': 'Spanish, Portuguese',
    'Chinese, English, French': 'English, French, Chinese',
    'English, russian': 'English, Russian',
    'Enlgish': 'English',
    'English, German, Polish, Ukrainian': 'English, German, Ukrainian, Polish',
    'Czech, English, french, german': 'English, French, German, Czech',
    'Englisch, French, some Korean and Chinese': 'English, French, Chinese, Korean',
    'Not fluently: German, Spanish, Latin, French': 'Spanish, French, German, Latin',
    'spanish': 'Spanish',
    'English, also learning Italian and Russian (Around A2?)': 'English, Italian, Russian',
    'Japanese (heritage)': 'Japanese',
    'engels, Frans': 'English, French',
    'English, German, basic french and Chinese': 'English, French, Chinese, German',
    'English, Spanish, Swedish, Latin, some Russian': 'English, Spanish, Russian, Latin, Swedish',
    'German, Korean, Mandarin': 'Mandarin, German, Korean',
    'Italian, Irish, French, Dutch (in order of proficiency highest-lowest)': 'Dutch, French, Italian, Irish',
    'Korean, Spanish': 'Spanish, Korean',
    'Little bit Korean': 'Korean',
    'French and very small amounts of Korean, German, Russian and Spanish': 'Spanish, French, German, Korean, Russian',
    'English and German': 'English, German',
    'Some Spanish': 'Spanish',
    'English, Spanish, Italian, French, Norwegian': 'English, Spanish, French, Italian, Norwegian',
    'French B1': 'French',
    'English, some French, German and Swahili': 'English, French, German, Swahili',
    'English Nederlands': 'English, Dutch',
    'Italian Korean': 'Italian, Korean',
    'A bit of german': 'German',
    'English (native-level)': 'English',
    'A very small amount of German': 'German',
    'Italian and some Portuguese': 'Italian, Portuguese',
    'Some spanish': 'Spanish',
    'Spanish B1': 'Spanish',
    'Italian. Studying Mandarin Chinese with traditional characters': 'Italian, Mandarin',
    'Hokkein, Italian, Chinese, Cantonese': 'Italian, Chinese, Cantonese, Hokkein',
    'french': 'French',
    'Hungarian (mother tongue), English': 'English',
    'Russian, English': 'English, Russian',
    'Arabic (intermediate)': 'Arabic',
    'English, Mandarin Chinese (A2)': 'English, Mandarin',
    '英語': 'English',
    'English, some French': 'English, French',
    'Mongolian,English,French': 'English, French, Mongolian',
    'English, Italian to a certain degree, also Slovak(but as a Czech person I don’t count it, since it’s the same as czech)': 'English, Italian, Slovak',
    'French, English': 'English, French',
    'english, italian': 'English, Italian',
    'English, spanish': 'English, Spanish',
    'French, Spanish, Amharic': 'Spanish, French, Amharic',
    'English, Mandarin': 'English, Chinese',
    'German, English': 'English, German',
    'Inglês': 'English',
    'Mandarin, German, Korean': 'German, Chinese, Korean',
    'English, Spanish, Russian, Latin, Swedish': 'English, Spanish, Russian, Swedish, Latin',
    'English, French, Chinese, German': 'English, French, German, Chinese',
    'English, Spanish, french, Dutch and Italian': 'English, Spanish, French, Italian, Dutch',
    'Darija (moroccan dialect of arabic), basic spanish': 'Darija, Spanish',
    'English, Malay, Cantonese, Japanese, Mandarin': 'English, Chinese, Cantonese, Japanese, Malay',
    'German (A2/B1), Spanish (A2)': 'Spanish, German',
    'Italian, Mandarin': 'Italian, Chinese',
    'English, intermediate Japanese': 'English',
    'Mandarin': 'Chinese',
    'Spanish, Mandarin, French, Korean': 'Spanish, French, Chinese, Korean'
}, inplace=True)


# In[18]:


## List and count all new values
print(survey_results['other_languages'].value_counts())

## The values in the column are now numeric, but these values should not be used for calculation (we cannot divide, multiply, etc the amount of years someone has been studying to come to any useful insights) as such, the column will be kept as a "string" type (object in pandas).
## survey_results['study_years'] = survey_results['study_years'].astype(str)


# ## Other_Languages Column conclusions
# 
# Some participants wrote "Japanese" as one of the "other" languages, I decided to keep this in as I assume it means they feel confident enough in using Japanese to see it as a language they fully master. Upon further inspection all but one of these participants declared their level as N1, with one participants saying they are level N2. This makes it plausible that their mastery of the language is high enough. This introduces a skewing of the data as some other participants of N2-N1 level may have decided not to mention "Japanese" in the "other languages" section as they may have interpreted the questions as "other languages besides your native language and Japanese, the language we are talking about in this survey". Luckily this should not really affect any outcomes, as this should not reflect in aggregations we are aiming for.
# 
# As there were way more languages present in this list to keep track of, it became hard to keep to a good structure of what language to place first. I tried to keep in mind the frequency of each language, but it may not always be fully correct.
# 
# Many people mentioned they speak a specific langauge only to a certain degree, or write 'a little bit of language X or Y'. As it's impossible for me to gauge just how good they really are in these languages, and their proficiency in other languages is not the main focus of this research, I decided to accept every mention of a language as "known" with the ideation that "if a participant feels confident enough to mention they speak a specific language, I should just accept that as the truth". Of course this will give a misguided view on the amount of languages the participants truly know, as some participants will be outliers due to loosely defining a language as "known".
# 
# Some participants were not clear on what other language they know, these have sadly been marked as "none", with one participant in particular mentioning they know 25+ other language to varying degrees, but didn't mention any language specifically by name.

# # main_study_method

# In[19]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['main_study_method'] = survey_results['main_study_method'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results['main_study_method'].value_counts())


# In[20]:


## Separate all values to get correct counts per study method, this separates values based on multiple selections (if a user selected A and B, the resulting string would be "A;B", this splits them into "A" and "B" so we can count the separate values)
## Some users input their own study methods, most seem to have separated these using a ", " (a comma followed by a space), this part of the code will separate these values so that they become separate as well
## Because we have two delimiters, I decided to first replace all the ";" delimiters with a "," and then replace the ", " with ",". This allows us to then split everything at once.
survey_results['main_study_method'] = survey_results['main_study_method'].str.replace(';', ',')  # Normalize separators
survey_results['main_study_method'] = survey_results['main_study_method'].str.replace(', ', ',')  # Normalize separators

survey_results['main_study_method'] = survey_results['main_study_method'].str.split(',')  # Split values

with pd.option_context('display.max_rows', None):
    print(survey_results['main_study_method'])


# In[21]:


## There are some values that need more separating or normalizing like "once a week of conversation with a tutor and found a Japanese friend in my city", in this part I will go through these outliers and normalize them.

# Replace inside lists in 'main_study_method'
def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Tae Kim's Grammar Guide for initial grammar", "Textbooks").replace('WaniKani for kanji', 'Apps').replace("Genki I","Textbooks").replace('idols’ youtubes', 'Immersion (through media)').replace('Anki + sentence mining.', 'Apps').replace('primarly use Lingq', 'Apps').replace('Vacation to Japan every year', 'Immersion (Traveling)').replace('once a week of conversation with a tutor and found a Japanese friend in my city', 'Private tutoring').replace('I do anki(Light novels', 'Apps').replace('Evening classes (2008 -> 2012)', 'Classes').replace('these days since moving to Japan only immersion', 'Immersion (living in the country)').replace('postgraduate studies in Japan some years ago', 'Immersion (living in the country)').replace("MaruMori","Apps").replace("Anki","Apps").replace("Wanikani","Apps").replace("LinQ","Apps").replace("Self study as best as I can", "Private tutoring").replace("but also get classes and private teachers (when possible)", "Classes").replace("YouTube", "Immersion (through media)").replace("anki", "Apps")
    return value  # Keep non-string values as is

survey_results['main_study_method'] = survey_results['main_study_method'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('main_study_method')['main_study_method'].unique())  # Check unique values


# In[22]:


## Some values no longer make sense, these are leftover values created by separating sentences where people used a comma.
## Examples are "these reflect different methods i've used over time" and "Need to explain"

# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["Need to explain", "these reflect different methods i've used over time", "II", "film based vocab)", "anime", "Idols’ twitcast", "idols’ tiktok lives", "Immersion (through media) Grammar videos", 'Immersion (through media) videos']

# Apply to the column and remove the specific values
survey_results['main_study_method'] = survey_results['main_study_method'].apply(lambda x: remove_values_from_list(x, values_to_remove))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('main_study_method')['main_study_method'].unique())  # Check unique values


# In[23]:


main_study_method_counts = survey_results['main_study_method'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(main_study_method_counts)


# ## main_study_method conclusions
# 
# The outcome is based on a multiple choice question, this means the outcome per row will be an aggregation of all the choices any given participant made. The issue here is that when checking how many times option "A" was chosen, it will only show the times where _only_ option "A" was chosen. Participants who chose option "A" and option "B" will be counted together only with participants who also chose "A" and "B". As such I decided to separate the given values so that I will not get data of who chose what specifically, but instead get general data of how many times each option was chosen.
# 
# Some details were left out as they are not necessary for the research, an example was a participant mentioning "idols' youtubes", this was changed to "YouTube" as the exact type of content is not necessary data to collect.

# # Study Goals

# In[24]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['study_goals'] = survey_results['study_goals'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results['study_goals'].value_counts())


# In[25]:


## Separate all values to get correct counts per study method, this separates values based on multiple selections (if a user selected A and B, the resulting string would be "A;B", this splits them into "A" and "B" so we can count the separate values)
## Some users input their own study methods, most seem to have separated these using a ", " (a comma followed by a space), this part of the code will separate these values so that they become separate as well
## Because we have two delimiters, I decided to first replace all the ";" delimiters with a "," and then replace the ", " with ",". This allows us to then split everything at once.
survey_results['study_goals'] = survey_results['study_goals'].str.replace(';', ',')  # Normalize separators
#survey_results['study_goals'] = survey_results['study_goals'].str.replace(', ', ',')  # Normalize separators

survey_results['study_goals'] = survey_results['study_goals'].str.split(',')  # Split values


with pd.option_context('display.max_rows', None):
    print(survey_results['study_goals'])


# In[26]:


## Check the complete list of study methods
print(survey_results.explode('study_goals')['study_goals'].unique())  # Check unique values


# In[27]:


## Normalizing values.

# Replace inside lists in 'main_study_method'
def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("I like language learning", "Linguistic interest").replace("To get a better chance at winning a scholarship to pursue higher education in Japan.", "Career advancement").replace("Master Japanese", "Personal interest").replace("¯\_(ツ)_/¯ I'm a part of a club that helps people learn Japanese", "Linguistic interest").replace("Linguistics interest", "Linguistic interest").replace("I moved to Japan last year and intend to stay here for the long haul", "Connecting with others").replace("Challenging myself and curiosity", "Personal interest").replace("love of linguistics", "Linguistic interest").replace("Dating japanese girls", "Personal interest")
    return value  # Keep non-string values as is

# Function to replace 'nan' in lists and properly handle NaN values
def clean_study_goals(x):
    if isinstance(x, list):
        # Replace "nan" if it exists in the list
        return ["Personal interest", "Manga/Anime", "Travel"] if "nan" in x else [replace_in_list(i) for i in x]
    else:
        return [replace_in_list(x)]

# Apply normalization inside lists
survey_results['study_goals'] = survey_results['study_goals'].apply(
    lambda x: [replace_in_list(i).strip() for i in x] if isinstance(x, list) else [replace_in_list(x)]
)

# Apply cleaning function
survey_results['study_goals'] = survey_results['study_goals'].apply(clean_study_goals)

# Explode the list for proper counting
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('study_goals')['study_goals'].unique())  # Check unique values


# In[28]:


## Removing unneccesary parts of data caused by leftovers, or information that was already given (for example, someone already clicked "Manga/Anime" and then mentioned "aside from the common stuffs like anime", this gets removed because changing it back to "Manga/Anime would cause their value to be added twice")

# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["so chatting with neighbours and being an active part of our small community is important to me","its really H stuffs cause its bonkers expensive to translate it. $30-$40 for 1 translation for 30 pages yep~","love the language", "Scholarly challenge", "I'm a musician and have toured in Japan and want to do that again so need some better Japanese!", "aside from the common stuffs like anime", "gotta keep up with them 💪"]

# Apply to the column and remove the specific values
survey_results['study_goals'] = survey_results['study_goals'].apply(lambda x: remove_values_from_list(x, values_to_remove))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('study_goals')['study_goals'].unique())  # Check unique values


# In[29]:


survey_results['study_goals'] = survey_results['study_goals'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

study_goals_counts = survey_results['study_goals'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(study_goals_counts)


# ## Study Goals conclusion
# 
# It was difficult to normalize certain goals, things like "To get a better chance at winning a scholarship to pursue higher education in Japan." felt like it leaned most towards "Career advancement" however, it's never certain that the participant truly meant it this way.
# 
# Some others wrote things like "love the language", which seems to align most with "personal interest" but also already selected "personal interest", so changing this value would have resulted in a duplicate entry for one participant. It was important to keep a clear eye on who replied what.

# # Used apps?

# In[30]:


print(survey_results['has_participant_used_apps'].value_counts())


# In[31]:


# Convert 'Yes' to True and 'No' to False
survey_results['has_participant_used_apps'] = survey_results['has_participant_used_apps'].map({'Yes': True, 'No': False})

# Check the updated column
print(survey_results['has_participant_used_apps'])
print(survey_results['has_participant_used_apps'].value_counts())


# ## Used apps? conclusion
# 
# Since this is a Yes/No question, the answers are clearly divided. I decided to change it to "bool" datatype and change th values from Yes/No to True/False as this will help with easier calculations down the line and for the next steps.

# # No Apps - Reason

# In[32]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['reason_noApps'] = survey_results['reason_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['reason_noApps'].value_counts())


# ## No Apps - Reason conclusion
# 
# No additional data cleaning necessary.
# [survey_results['has_participant_used_apps'] == False] is used to filter out the rows where has_participants_used_apps is True, as we only have data from participants who replied "No" to that question in this part of the data and this would lead to NaN values for all the datapoints where the participant replied "Yes".

# # No Apps - Considered using

# In[33]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['considered_using_noApps'] = survey_results['considered_using_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['considered_using_noApps'].value_counts())


# In[34]:


## Splitting on ";"
survey_results['considered_using_noApps'] = survey_results['considered_using_noApps'].str.replace(';', ',')  # Normalize separators
#survey_results['study_goals'] = survey_results['study_goals'].str.replace(', ', ',')  # Normalize separators

survey_results['considered_using_noApps'] = survey_results['considered_using_noApps'].str.split(', ')  # Split values


# In[35]:


with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['considered_using_noApps'])


# In[36]:


## Removing unneccesary parts of data caused by leftovers, or information that was already given (for example, someone already clicked "Manga/Anime" and then mentioned "aside from the common stuffs like anime", this gets removed because changing it back to "Manga/Anime would cause their value to be added twice")

# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["None"]

# Apply to the column and remove the specific values
survey_results['considered_using_noApps'] = survey_results['considered_using_noApps'].apply(lambda x: remove_values_from_list(x, values_to_remove))


# In[37]:


survey_results['considered_using_noApps'] = survey_results['considered_using_noApps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

considered_using_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['considered_using_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(considered_using_noApps_counts)


# ## No Apps - Considered using conclusion
# 
# For the most part very straightforward, only one outlier:
# 156 [Anki, None]
# 
# This person selected both "Anki" and then "None", which is seen as an option when the participant doesn't want to try any apps, so it is unexpected to have both "None" and another value selected. Normally this value would be changed into "NaN" (not a number/ a null value), but since the participant also selected "Anki", this would lead to a wrong view on the "None" values (people who do not want to try apps). As such the "None" value was removed to avoid this.

# # No Apps - Use to Overcome Challenges

# In[38]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['use_to_overcome_challenges_noApps'] = survey_results['use_to_overcome_challenges_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['use_to_overcome_challenges_noApps'].value_counts())


# In[39]:


## Splitting on ";"

survey_results['use_to_overcome_challenges_noApps'] = survey_results['use_to_overcome_challenges_noApps'].str.replace(';',',')  # Split values
#survey_results['use_to_overcome_challenges_noApps'] = survey_results[survey_results["use_to_overcome_challenges_noApps"]!="No, I do not want to use Language Learning Apps"]['use_to_overcome_challenges_noApps'].str.split(', ')  # Split values
survey_results['use_to_overcome_challenges_noApps'] = survey_results['use_to_overcome_challenges_noApps'].apply(
    lambda x: x.split(', ') if isinstance(x, str) and x != "No, I do not want to use Language Learning Apps" else x
)


# In[40]:


with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['use_to_overcome_challenges_noApps'])


# In[41]:


use_to_overcome_challenges_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['use_to_overcome_challenges_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(use_to_overcome_challenges_noApps_counts)
    


# ## No Apps - Use to Overcome Challenges conclusion
# 
# Nothing much to note, general data cleaning was done, no outliers found

# # No Apps - Other Tools

# In[42]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['other_tools_noApps'] = survey_results['other_tools_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['other_tools_noApps'].value_counts())


# In[43]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Sites, books(日本語総まとめ N5-N1 grammar book only), 原稿用紙, non-live service apps (anki, iKanji)", "Websites")
    return value  # Keep non-string values as is

survey_results['other_tools_noApps'] = survey_results['other_tools_noApps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('other_tools_noApps')['other_tools_noApps'].unique())  # Check unique values


# In[44]:


survey_results['other_tools_noApps'] = survey_results['other_tools_noApps'].replace("nan", np.nan)

other_tools_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['other_tools_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(other_tools_noApps_counts)


# ## No Apps - Other Tools conclusion
# 
# Only one outlier, one participant gave a list of items they used, however, "books" are not seen as digital tools, which this question specifically looks for, and "anki, ikanji" are apps/web services. As such, I decided to put this all under "Websites"

# # No Apps - Why other tools?

# In[45]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['why_other_tools_noApps'] = survey_results['why_other_tools_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['why_other_tools_noApps'].value_counts())


# In[46]:


with pd.option_context('display.max_rows', None):
    print(survey_results.explode('other_tools_noApps')['why_other_tools_noApps'].unique())  # Check unique values


# In[47]:


survey_results['why_other_tools_noApps'] = survey_results['why_other_tools_noApps'].replace("nan", np.nan)

why_other_tools_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['why_other_tools_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(why_other_tools_noApps_counts)


# ## No Apps - Why other tools? conclusion
# 
# Nothing much to note here either, this was an optional, open question, so this data gives a lot of interesting additional information on the thought process of the participants

# # No Apps - Most effective?

# In[48]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['most_effective_noApps'] = survey_results['most_effective_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['most_effective_noApps'].value_counts())


# In[49]:


## Splitting on ";"
survey_results['most_effective_noApps'] = survey_results['most_effective_noApps'].str.split(', ')  # Split values


# In[50]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['most_effective_noApps'].value_counts())


# In[51]:


most_effective_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['most_effective_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(most_effective_noApps_counts)


# ## No Apps - Most effective? conclusion
# 
# Not much to mention here either, no outliers, cleaned up the data to show the individual values and make them countable

# # No Apps - Least effective?

# In[52]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['least_effective_noApps'] = survey_results['least_effective_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['least_effective_noApps'].value_counts())


# In[53]:


## Splitting on ";"
survey_results['least_effective_noApps'] = survey_results['least_effective_noApps'].str.split(', ')  # Split values


# In[54]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['least_effective_noApps'].value_counts())


# In[55]:


# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["The given options are effective in some way or the other"]

# Apply to the column and remove the specific values
survey_results['least_effective_noApps'] = survey_results['least_effective_noApps'].apply(lambda x: remove_values_from_list(x, values_to_remove))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('least_effective_noApps')['least_effective_noApps'].unique())  # Check unique values


# In[56]:


survey_results['least_effective_noApps'] = survey_results['least_effective_noApps'].apply(
    lambda lst: [np.nan if item in ["Nothing", "nan", "Not sure"] else item for item in lst] if isinstance(lst, list) else lst
)

least_effective_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['least_effective_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(least_effective_noApps_counts)


# ## No Apps - Least effective? conclusion
# 
# The last value in "[Classes, Self-study, The given options are effective in some way or the other]" suggests that every option has some value, as such I would have changed this to "Nothing", but since the participant also mentioned two other options as "least useful", I have decided to delete the last value. Reason being is that "least useful" does not necessarily imlply "not useful", it just helps us understand what these participants think is the least useful option available.

# # overcoming_challenges-noApps

# In[57]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['overcoming_challenges_noApps'] = survey_results['overcoming_challenges_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['overcoming_challenges_noApps'].value_counts())


# In[58]:


survey_results['overcoming_challenges_noApps'] = survey_results['overcoming_challenges_noApps'].replace("nan", np.nan)

overcoming_challenges_noApps_counts = survey_results[survey_results['has_participant_used_apps'] == False]['overcoming_challenges_noApps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(overcoming_challenges_noApps_counts)


# ## overcoming_challenges-noApps conclusion
# 
# This one was also an open, optional question aiming to get more insights into the participant's thinking patterns. As such there is not a lot of data cleaning needed, as this data cannot be used for aggregation, but is rather used to get additional information. This was also the only optional question that did not have the (optional) notation in the survey. This was done on purpose, as I didn't want to bog down the users with forcing them to write down additional information (this could also lead to bad data). Yet at the other hand I really wanted this data point from as many participants as possible, as I think it can lead to very interesting insights. The hope was that participants would look for the (optional) notation to know which questions they can skip, and this way they would decide to fill this one in. Participants who really didn't want to fill it in would quickly notice it's not obligatory and can click through to the next questions.

# # daily_study_time-noApps

# In[59]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['daily_study_time_noApps'] = survey_results['daily_study_time_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['daily_study_time_noApps'].value_counts())


# In[60]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("first 2 years: 8-12 hours daily (learning basics up to N1). 3rd-4th year: ~4 hours (Active immersion only), last year: ~6 hours (Active + passive immersion)", "6 hours").replace("No ‘Study’ 2-5 hours of media consumption", "3.5 hours").replace("I’ve stopped studying now", "0 minutes")

survey_results['daily_study_time_noApps'] = survey_results['daily_study_time_noApps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('daily_study_time_noApps')['daily_study_time_noApps'].unique())  # Check unique values


# In[61]:


import pandas as pd

# Convert to Timedelta
survey_results['study_duration'] = pd.to_timedelta(survey_results[survey_results['has_participant_used_apps'] == False]['daily_study_time_noApps'])

# Check the results
print(survey_results[survey_results['has_participant_used_apps'] == False]['study_duration'])


# In[62]:


survey_results['study_duration_minutes'] = survey_results[survey_results['has_participant_used_apps'] == False]['study_duration'].dt.total_seconds() / 60
print(survey_results[survey_results['has_participant_used_apps'] == False]['study_duration_minutes'])


# ## daily_study_time-noApps conclusion
# 
# Cleaned the outliers, one person explained how much they studied throughout the years, Since I cannot keep all this data, I decided to only keep the most recent hours studied, as the rest of the data is also based on the participants current stats (fe, what level are you now?)
# 
# Another participant said they study/immerse anywhere between 2-5 hours, so I took the average.
# 
# The data was changed to datetime, from where I could change it to a numeral "minutes" version. Both are kept and can later be combined with the hours studied for the other group if necessary (can still be recognized what list it comes from due to the has_participant_used_apps True/False datapoint)

# # structured_vs_flexible_learning-noApps

# In[63]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['structured_vs_flexible_learning_noApps'] = survey_results['structured_vs_flexible_learning_noApps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == False]['structured_vs_flexible_learning_noApps'].value_counts())


# ## structured_vs_flexible_learning-noApps conclusion
# 
# While the last datapoint is very long and it could be added to "I prefer a structured study plan", I don't want to lose the valuable notions in the text the participant wrote, as such I will leave the answer as is

# # experienced_intermediate_plateau-noApps

# In[64]:


## Print all current values and count them, make sure to print all the values

with pd.option_context('display.max_rows', None):
    print(survey_results['experienced_intermediate_plateau_noApps'].value_counts())


# In[65]:


# Convert 'Yes' to True and 'No' to False
survey_results['experienced_intermediate_plateau_noApps'] = survey_results['experienced_intermediate_plateau_noApps'].map({'Yes': True, 'No': False})

# Check the updated column
print(survey_results[survey_results['has_participant_used_apps'] == False]['experienced_intermediate_plateau_noApps'])
print(survey_results[survey_results['has_participant_used_apps'] == False]['experienced_intermediate_plateau_noApps'].value_counts())


# ## experienced_intermediate_plateau-noApps conclusion
# 
# Just like the has_participant_used_apps column, this is a bool and is as such changed to one. It will help with combining the data of both "noApps" and "Apps" groups on their intermediate plateau experiences. 

# # used_apps-Apps

# In[66]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['used_apps_Apps'] = survey_results['used_apps_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].value_counts())


# In[67]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].value_counts())


# In[68]:


used_apps_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(used_apps_Apps_counts)


# In[69]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Lingodeer", "LingoDeer").replace("Marumori", "MaruMori").replace("italki", "Italki").replace("bunpo", "Bunpo").replace("wanikani", "WaniKani").replace("trying out Ringotan. pretty good but the stroke order is really limited in terms of how you want to put your strokes.", "Ringotan").replace("Flaming Durtles (Wanikani)", "WaniKani").replace("Wanikani", "WaniKani").replace("Kanji study", "Kanji Study").replace("kanji study", "Kanji Study").replace("ringotan", "Ringotan").replace("Tsurukame (for WaniKani)", "WaniKani").replace("Wanikani and Bunpro", "WaniKani, BunPro").replace("webapp called wanikani", "WaniKani").replace("Refold Timer app", "Refold App").replace("mazii.net & jpdb.io", "Mazii.net, jpdb.io").replace("bunpro and wanikani", "WaniKani, BunPro").replace("Buusuu", "Busuu").replace("WaniKani  NihongoShark (NativShark)", "WaniKani, NativShark").replace("Mainly use Lingq", "LingQ").replace("Akebi / Kanji Study / Obenkyo", "Akebi, Kanji Study, Obenkyo").replace("Tsurukame", "WaniKani").replace("kawainihongo", "kawaiiNihongo").replace("WaniKani (web site)", "WaniKani").replace("bunpro", "BunPro").replace("minato", "Minato").replace("langotalk", "Langotalk").replace("umi", "Umi").replace("falou", "Falou").replace("flashcards deluxe", "Flashcards Deluxe").replace("chatgpt", "ChatGPT").replace("webapp called WaniKani", "WaniKani").replace("lingual ninja", "Lingual Ninja").replace("WaniKani and Bunpro", "Wanikani, Bunpro").replace("kanji.garden", "Kanji.Garden").replace("bunpro and WaniKani", "Wanikani, Bunpro").replace("yomuyomu", "Yomu Yomu").replace(" Kanji Garden", "Kanji Garden").replace("WaniKani (WaniKani)", "WaniKani").replace("Bunpro,Kanji Garden", "Bunpro, Kanji Garden").replace("tandem", "Tandem").replace("SatoriReader", "Satori Reader").replace("Kanji.Garden", "Kanji Garden").replace("Bunpro", "BunPro").replace("iTalki","italki").replace("Italki","italki").replace("Wanikani", "WaniKani").replace("BunPro and WaniKani", "BunPro, WaniKani").replace("MigiiJLPT", "Migii JLPT")
    return value  # Keep non-string values as is

survey_results['used_apps_Apps'] = survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'])


# In[70]:


## Seeing as some values were written as "X and Y", these were replaced to "X, Y" but this comma is a text, not a separator, se we need to split on ";" and ", " again
## Splitting on ";" and ", "
import re

survey_results['used_apps_Apps'] = survey_results['used_apps_Apps'].apply(
    lambda x: re.split(r';|, ', str(x)) if pd.notna(x) else x
)


# In[71]:


used_apps_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(used_apps_Apps_counts)


# In[72]:


# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["Countless others","and many","many others", "probably others dont remember", "Genki Vocab", "Genki Conjugation", "I use websites mostly rather than installing apps..."]

# Apply to the column and remove the specific values
survey_results['used_apps_Apps'] = survey_results['used_apps_Apps'].apply(lambda x: remove_values_from_list(x, values_to_remove))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('used_apps_Apps')['used_apps_Apps'].unique())  # Check unique values


# In[73]:


used_apps_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['used_apps_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(used_apps_Apps_counts)


# ## used_apps-Apps conclusion
# 
# Lots of fixes needed to be done, between mistyped app names (capitalisation or typo's) and different separators (spaces, slashes, comma's, "and", ...) Luckily, not many entries were unclear in what they wanted to convey, the only confusing one was the fact that both "Bunpo" and "BunPro" are different apps, and WaniKani seems to have some add-ons which people mentioned specifically. These have just been counted under "WaniKani" as I use these app names as umbrella terms which cover everything that is part of the app (as in Duolingo having both "Super" and "Regular" plans, and Anki having hundreds of plugins)

# # most_useful-Apps

# In[74]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['most_useful_Apps'] = survey_results['most_useful_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_Apps'].value_counts())


# In[75]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Wanikani", "WaniKani").replace("Marumori", "MaruMori").replace("Kanji study", "Kanji Study").replace("Bunpro", "BunPro").replace("Wanikani, bunpro", "WaniKani, BunPro").replace("Italki, Kanji Study", "italki, Kanji Study").replace("Lingodeer", "LingoDeer").replace("Bunpro, Wanikani", "WaniKani, BunPro").replace("lingual ninja", "Lingual Ninja").replace("“Kanji!” and “Japanese!” on the app store, the names are very generic but they’re a godsend", "Kanji, Japanese").replace("flashcards deluxe", "Flashcards Deluxe").replace("WaniKani, Bunpro, MigiiJLPT", "WaniKani, BunPro, Migii JLPT").replace("minato", "Minato").replace("Lingodeer, Migaku", "LingoDeer, Migaku").replace("KawaiiNihongo", "kawaiiNihongo").replace("WaniKani, chatgpt", "WaniKani, ChatGPT").replace("Lingq", "LingQ").replace("NativShark & MaruMori", "NativShark, MaruMori").replace("mazii.net & jpdb.io", "Mazii.net, jpdb.io").replace("bunpro and wanikani", "BunPro, WaniKani").replace("WaniKani and NihongoShark", "WaniKani, NativShark").replace("Akebi / kanji Study", "Akebi, Kanji Study").replace("wanikani", "WaniKani").replace("BunPro, Tsurukame (for WaniKani)", "BunPro, WaniKani").replace("WaniKani, Bunpro, SatoriReader", "WaniKani, Bunpro, Satori Reader").replace("Bunpro, Wanikani", "Bunpro, WaniKani").replace("WaniKani (Tsurukame)", "WaniKani").replace("bunpro", "BunPro")
    return value  # Keep non-string values as is

survey_results['most_useful_Apps'] = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_Apps'])


# In[76]:


## Seeing as some values were written as "X and Y", these were replaced to "X, Y" but this comma is a text, not a separator, se we need to split on ";" and ", " again
## Splitting on ";" and ", "

survey_results['most_useful_Apps'] = survey_results['most_useful_Apps'].apply(
    lambda x: re.split(r';|, ', str(x)) if pd.notna(x) else x
)


# In[77]:


most_useful_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(most_useful_Apps_counts)


# In[78]:


# Function to remove multiple values from lists
def remove_values_from_list(value, targets):
    if isinstance(value, list):
        # Remove all items in the list that are in the 'targets' list
        return [item for item in value if item not in targets]
    return value  # Keep non-list values as is

# List of values to remove
values_to_remove = ["None","any and all dictionary apps", "I use websites and they are really helpful..."]

# Apply to the column and remove the specific values
survey_results['most_useful_Apps'] = survey_results['most_useful_Apps'].apply(lambda x: remove_values_from_list(x, values_to_remove))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('most_useful_Apps')['most_useful_Apps'].unique())  # Check unique values


# In[79]:


survey_results['most_useful_Apps'] = survey_results['most_useful_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

most_useful_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(most_useful_Apps_counts)


# ## most_useful-Apps conclusion
# 
# Most apps from the previous part seem to be coming back here, interesting was an app named "Kanji" I eventually found it on the app store, but it seems to only have around 100 users, not sure this is the app the participant meant. Toggle is not a language learning app but a time tracking app, however, I decided to keep it as the intended use of an app does not dictate how people end up utilising it. I have used Toggle to "gamify" immersion time myself in the past, so I can see where it could be used as a language learning app.

# # most_useful_current_level-Apps

# In[80]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['most_useful_current_level_Apps'] = survey_results['most_useful_current_level_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_current_level_Apps'].value_counts())


# In[81]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Wanikani", "WaniKani").replace("Marumori", "MaruMori").replace("Kanji study", "Kanji Study").replace("minato", "Minato").replace("Flashcards deluxe", "Flashcards Deluxe").replace('“Kanji!”', 'Kanji').replace("Italki, Kanji Study", "italki").replace("iTalki", "italki").replace("Bunpo, wanikani", "Bunpo").replace("Anki would be the best if I was progressing at all right now", "Anki").replace("Lingq", "LingQ").replace("bunpro", "BunPro").replace("wanikani", "WaniKani").replace("WaniKani (Tsurukame)", "WaniKani").replace("WaniKani, Bunpro", "WaniKani").replace("Bunpro, WaniKani", "BunPro").replace("Bunpro", "BunPro").replace("Minato and the main website of marugoto...", "Minato")
    return value  # Keep non-string values as is

survey_results['most_useful_current_level_Apps'] = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_current_level_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_current_level_Apps'])


# In[82]:


survey_results['most_useful_current_level_Apps'] = survey_results['most_useful_current_level_Apps'].replace("nan", np.nan)

most_useful_current_level_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_current_level_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(most_useful_current_level_Apps_counts)


# ## most_useful_current_level-Apps conclusion
# 
# This question was a "choose only one" question. There were options to choose from and a "other" option. Three participants however wrote two apps in the "other" section, these were:
# 
# Italki, Kanji Study
# Bunpro, Wanikani
# Wanikani, Bunpro
# 
# Since this would skew the data, I decided to keep only the first mentioned app, going by the mindset that the one they think of first is the one that's top of mind.
# 
# Next, one participant wrote "Anki would be the best if I was progressing at all right now".
# Here I decided to count this as an entry towards "Anki"

# # usage_frequency-Apps

# In[83]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['usage_frequency_Apps'] = survey_results['usage_frequency_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['usage_frequency_Apps'].value_counts())


# In[84]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Normally daily, currently other priorities with work", "Daily").replace("I use Anki daily but I only check HelloTalk once every few days because I spend too much time on it otherwise.", "Daily").replace("taking a hiatus right now - I used to use it daily", "Daily").replace("i've been taking a break in the past year, so my answers will be from when i was still active, in which case it was daily", "Daily").replace("Burned out, intending to get started again. Used to be daily", "Daily").replace("Wanikani I use daily, the others not very much", "Daily").replace("I try my best to use them as often as I can but being stupid to remember kanji demotivates you and doesnt sink into the brain. repetition can work but eventually you just dont remember", "A few times a week")
    return value  # Keep non-string values as is

survey_results['usage_frequency_Apps'] = survey_results[survey_results['has_participant_used_apps'] == True]['usage_frequency_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['usage_frequency_Apps'])


# In[85]:


usage_frequency_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['usage_frequency_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(usage_frequency_Apps_counts)


# ## usage_frequency-Apps conclusion
# 
# There were a few decisions that needed to be made here, I'll go over them one by one:
# 
# Normally daily, currently other priorities with work
# - Since this participant seems to have taken a break of studying Japanese, it makes sense to me to use the data from when they were active -> Daily
# 
# I use Anki daily but I only check HelloTalk once every few days because I spend too much time on it otherwise.
# - The fact they use an app daily decides the value for this entry -> Daily
# 
# taking a hiatus right now - I used to use it daily
# - Same as the first one -> Daily
# 
# i've been taking a break in the past year, so my answers will be from when i was still active, in which case it was daily
# - Same as the first one -> Daily
# 
# Burned out, intending to get started again. Used to be daily
# - This participant also seems to be on a break, hoping to get back into it, though maybe the fact he used to do it daily aided in them having a burn-out -> Daily
# 
# Wanikani I use daily, the others not very much
# - Same as the second entry -> Daily
# 
# I try my best to use them as often as I can but being stupid to remember kanji demotivates you and doesnt sink into the brain. repetition can work but eventually you just dont remember
# - Since this person mentions "as often as I can", it's difficult to pinpoint a value, the most general value here seems to be "a few times a week" -> A few times a week

# # daily_study_time-Apps

# In[86]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['daily_study_time_Apps'] = survey_results['daily_study_time_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['daily_study_time_Apps'].value_counts())


# In[87]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Currently dormant, but the interest is still there", "0 minutes").replace("Over an hour on mosr days, weekends usually about 3+", "1 hour").replace("1 to 2 hours dialy when I was going hard on it", "1.5 hours").replace("Around 15/20 minutes for anki/renshuu, for hello talk it depends, sometimes I just check the notifications and sometimes talk im voice rooms for 2 hours.", "20 minutes").replace("30 mins to 1 hour", "45 minutes").replace("Depends between 10 min and open end", "10 minutes").replace("It used to be 40 min, now it's closer to 60 min.", "1 hour").replace("I prefer youtube videos and chatgpt", "0 minutes").replace("5+ hours", "5 hours").replace("I don't really use these apps anymore", "0 minutes").replace("As much as I can, usually 1 and a half to more than 3 hours.", "2 hours").replace("3-4", "210 minutes")

survey_results['daily_study_time_Apps'] = survey_results['daily_study_time_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('daily_study_time_Apps')['daily_study_time_Apps'].unique())  # Check unique values


# In[88]:


# Convert to Timedelta
survey_results['study_duration_App'] = pd.to_timedelta(survey_results[survey_results['has_participant_used_apps'] == True]['daily_study_time_Apps'])

# Check the results
print(survey_results[survey_results['has_participant_used_apps'] == True]['daily_study_time_Apps'])


# In[89]:


survey_results['study_duration_minutes_App'] = survey_results[survey_results['has_participant_used_apps'] == True]['study_duration_App'].dt.total_seconds() / 60
print(survey_results[survey_results['has_participant_used_apps'] == True]['study_duration_minutes_App'])


# In[90]:


study_duration_minutes_App_counts = survey_results[survey_results['has_participant_used_apps'] == True]['study_duration_minutes_App'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(study_duration_minutes_App_counts)


# ## daily_study_time-Apps conclusion
# 
# Did the exact same thing as with the daily_study_time_noApp section.
# A few decisions had to be made.
# 
# Currently dormant, but the interest is still there
# - this indicates the person is not using them at the moment, thus -> 0 minutes
# 
# Over an hour on mosr days, weekends usually about 3+
# - particularly difficult to gauge, I want to avoid coming up with rules or estimations of participants values as much as possible, as such I will base myself on values that were mentioned, in this case "over an hour on most days" reads like an average of less than an hour per day, coupled with the weekends outlier, I decided to avoid overcomplicating it with new values the participant didn't mention themselves -> 1 hour
# 
# 1 to 2 hours dialy when I was going hard on it
# - In this case it makes sense to take an average, while the text indicates they aren't doing this anymore, they didn't give me additional data to gauge their current most accurate value -> 1.5 hours
# 
# As much as I can, usually 1 and a half to more than 3 hours.
# - Was changed to 2 hours to find a balance between the 1.5 - 3+ hours they mentioned
# 
# Around 15/20 minutes for anki/renshuu, for hello talk it depends, sometimes I just check the notifications and sometimes talk im voice rooms for 2 hours.
# 
# 
# 30 mins to 1 hour
# 
# 
# Depends between 10 min and open end
# 
# 
# It used to be 40 min, now it's closer to 60 min.
# 
# 
# I prefer youtube videos and chatgpt
# 
# 

# # skill_improvement_usage_habits-Apps

# In[91]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['skill_improvement_usage_habits_Apps'] = survey_results['skill_improvement_usage_habits_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['skill_improvement_usage_habits_Apps'].value_counts())


# In[92]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("Hasn't change that much. Usage usually only goes down when my life is busy (holiday, work is more intense + exhausting than ususal)", "I still use them about the same amount").replace("I use different ones", "I still use them about the same amount").replace("WaniKani is used less (reviews only), Anki is used more (transition to 30 daily cards).", "I still use them about the same amount").replace("I stopped using it even while still pursuing Japanese.", "I use them less now").replace("Burnout really meant I had to take a break. I'd otherwise go back to daily usage", "I use them less now").replace("It varies a lot based on how interested I am in the language at the moment", "I still use them about the same amount").replace("Less, But I Plan To Use Them More", "I use them less now")
    
survey_results['skill_improvement_usage_habits_Apps'] = survey_results['skill_improvement_usage_habits_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('skill_improvement_usage_habits_Apps')['skill_improvement_usage_habits_Apps'].unique())  # Check unique values


# In[93]:


# Replace 'nan' with 'new text' where 'has_participant_used_apps' is True
survey_results.loc[
    (survey_results["skill_improvement_usage_habits_Apps"] == "nan") & 
    (survey_results["has_participant_used_apps"] == True), 
    "skill_improvement_usage_habits_Apps"
] = "I still use them about the same amount"

# Display the updated dataframe (optional)
print(survey_results)


# In[94]:


skill_improvement_usage_habits_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['skill_improvement_usage_habits_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(skill_improvement_usage_habits_Apps_counts)


# ## skill_improvement_usage_habits-Apps conclusion
# 
# Also here there were some interpretations to be made:
# 
# Less, But I Plan To Use Them More
# - Since they use them less at the moment -> I use them less now
# 
# It varies a lot based on how interested I am in the language at the moment
# - This is very hard to define, but it seems like this type of ideation is something that persists and is not dependent on his current level, as such I am willing to assume this participant has had this type of action when it comes to stuyding -> I still use them about the same amount
# 
# Burnout really meant I had to take a break. I'd otherwise go back to daily usage
# - At the moment this participant is using them less, burnout may be caused by many things, but it could also be part of the level he's at now (intermediate plateau?) as such, it's interesting to gather the data as is -> I use them less now
# 
# I stopped using it even while still pursuing Japanese.
# -> I use them less now
# 
# WaniKani is used less (reviews only), Anki is used more (transition to 30 daily cards).
# - This participant seems to have shifted their attention from one app to another with no indication that they are now using them more, nor less -> I still use them about the same amount
# 
# I use different ones
# - Same as above -> I still use them about the same amount
# 
# Hasn't change that much. Usage usually only goes down when my life is busy (holiday, work is more intense + exhausting than ususal)
# - This participant is similar to the second entry -> I still use them about the same amount

# # most_useful_features-Apps

# In[95]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['most_useful_features_Apps'] = survey_results['most_useful_features_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_features_Apps'].value_counts())


# In[96]:


## Splitting on ";"
survey_results['most_useful_features_Apps'] = survey_results['most_useful_features_Apps'].str.split(', ')  # Split values


# In[97]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_features_Apps'].value_counts())


# In[98]:


most_useful_features_Apps_counts = survey_results['most_useful_features_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(most_useful_features_Apps_counts)


# In[99]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value.replace("long-term reliability resulting from open source nature and non-cloud options","None").replace("spaced repetition","Flashcards").replace("content agnosticism","None").replace("The gammification of the apps make the experience of learning more interesting in general.","None").replace("Having an all in one place to study","None").replace("search","None").replace("export/import","None").replace("decentralization","None").replace("AnkiConnect for integration with mpvacious and Rikaitan.","None").replace("SRS", "Flashcards").replace("Flexibility to create my own flashcards and decide myself exactly what I will review.", "Flashcards").replace("Spaced Repetition", "Flashcards").replace("SRS timings", "Flashcards").replace("Refresher exercises", "Flashcards").replace("SRS", "Flashcards").replace("I havent found an app or something that combines both the kanji and vocabulary into a sentence", "None").replace("Several kanken apps", "None").replace("Dictionary", "None").replace("mnemonics", "None").replace("teaching radicals", "None").replace("randomized example sentences (in bunpro)", "Randomized example sentences").replace("Kanji dedication", "None").replace("Having everything (grammar", "None").replace("kanji", "None").replace("vocab) in one place.","None").replace("Personalization (customized learning)", "Personalization").replace("Intergration with other tools and programms like yomichan/yomitan or mpv", "None").replace("Aesthetics (it looks nice/fun)", "Aesthetics").replace("Spaced repetition", "Flashcards").replace("or DDMLL).  I used to spend more time using Stable Diffusion XL (SDXL) recreationally than studying Japanese—until I discovered Migaku and realized I could combine both. By generating None tailored to personal interests and high-dopamine visual triggers","None").replace("AI-generated visual None for flashcards (what I call Dopamine-Driven Mnemonic Language Learning","None").replace("I made studying far more engaging. Over the past two months","None").replace("DDMLL has improved my retention and study efficiency by 3-5x. Because the process is self-rewarding","None").replace("it makes consistency almost effortless for me.","None").replace("Flashcards timings","Flashcards")
    return value  # Keep non-string values as is

# Apply function to lists inside the column
survey_results['most_useful_features_Apps'] = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_features_Apps'].apply(
    lambda lst: [replace_in_list(item) for item in lst] if isinstance(lst, list) else replace_in_list(lst)
)
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_features_Apps'])


# In[100]:


survey_results['most_useful_features_Apps'] = survey_results['most_useful_features_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

most_useful_features_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['most_useful_features_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(most_useful_features_Apps_counts)


# In[101]:


print(survey_results['most_useful_features_Apps'].explode().value_counts())
#print(survey_results['most_useful_features_Apps'].explode().unique())


# ### most_useful_features-Apps conclusion
# 
# In this question I aimed to get a view on the most useful features in apps. Some participants gave answers that don't directly answer this question, these were dealt with as follows:
# 
# SRS, search, export/import, decentralization, AnkiConnect for integration with mpvacious and Rikaitan
# - This entry mostly talked about SRS (spaced repetition systems) and ways to more easily make flashcards for SRS -> Spaced repetition
# 
# Flexibility to create my own flashcards and decide myself exactly what I will review.
# - -> Flashcards
# 
# SRS timings
# - -> Spaced repetition
# 
# Refresher exercises
# - -> Spaced repetition
# 
# SRS
# - -> Spaced repetition
# 
# I havent found an app or something that combines both the kanji and vocabulary into a sentence
# - This participant didn't mention anything specific -> None
# 
# Several kanken apps
# - This participant mentioned apps, not features, so it's impossible to gather what features they think are most useful -> None
# 
# Dictionary, mnemonics, teaching radicals
# - This participant mentioned techniques, not features, I tried to find what feature is closest, but none are close enough -> None
# 
# randomized example sentences (in bunpro)
# - This is a feature I hadn't taken into account, so I decided to add it -> Randomized example sentences
# 
# Kanji dedication
# - This does not seem to be aiming at a feature -> None
# 
# Having everything (grammar, kanji, vocab) in one place.
# - This is not 100% a feature, but it seems like it could be something people think is very important, and might be a feature. Another person also mentioned this, so I decided to add it -> Having an all in one place to study
# 
# Intergration with other tools and programms like yomichan/yomitan or mpv
# - This is talking about specific add-ons of the 'Anki' app -> None
# 
# Chat with native speakers
# - An interesting feature I hadn't thought of, added it -> Chat with native speakers
# 
# Community help
# - Same as above -> Community help
# 
# ### Additional changes later on
# Since spaced repetition was not an option initially and was added by multiple people, I have decided to change it to "flaschards" as it is seen to combine both flashcards and spaced repetition, since that is the most common form in which flashcards are used. If spaced repetition is kept as is, it will score very low on the "most useful features" whilst flashcards scores very high for the reason that most people probably saw them as a combined thing as most people only use flashcards for the sake of spaced repetition. As such these two are now combined.

# # least_useful_features-Apps

# In[102]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['least_useful_features_Apps'] = survey_results['least_useful_features_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['least_useful_features_Apps'].value_counts())


# In[103]:


## Splitting on ";"
survey_results['least_useful_features_Apps'] = survey_results['least_useful_features_Apps'].str.split(', ')  # Split values


# In[104]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['least_useful_features_Apps'].value_counts())


# In[105]:


least_useful_features_Apps_counts = survey_results['least_useful_features_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(least_useful_features_Apps_counts)


# In[106]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  
        if value == "SRS, plugin support":  
            return ["Flashcards", "Plugin support"]  # Return a list directly
        
        # Apply replacements only if it's a string
        return value.replace("Aesthetics (it looks nice/fun)", "Aesthetics")\
                    .replace("Personalization (customized learning)", "Personalization")\
                    .replace("They are all useful in one way or another", "None")\
                    .replace("Spaced Repetition", "Flashcards")\
                    .replace("SRS", "Flashcards")\
                    .replace("plugin support", "None")\
                    .replace("Gamification", "None")
    
    return value  # Keep non-string values as is

# Apply the transformation to lists
survey_results['least_useful_features_Apps'] = survey_results['least_useful_features_Apps'].apply(
    lambda x: sum(([replace_in_list(i)] if isinstance(replace_in_list(i), str) else replace_in_list(i) for i in x), []) 
    if isinstance(x, list) else replace_in_list(x)
)

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('least_useful_features_Apps')['least_useful_features_Apps'].unique())  # Check unique values


# In[107]:


survey_results['least_useful_features_Apps'] = survey_results['least_useful_features_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

least_useful_features_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['least_useful_features_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(least_useful_features_Apps_counts)


# ## least_useful_features-Apps conclusion
# 
# Most of the work here was similar to the previous column, there were a few interesting cases though:
# 
# 
# Spaced Repetition, Plugin support
# - This participant marked both Spaced repetition and plugin support as least effective. Since this participant is the only participant to mark spaced repetition as least useful, and is the only participant to add "Plugin support" in other, I'm unsure if they realised this question was asking for the "least" useful. Either way I will have to accept their entry, and it is possible that they feel different about this from all the other participants. Plugin support was a very interesting addition I did not think of beforehand, but may be very interesting to take into account for future app developers, as such I have added it -> Spaced repetition, Plugin support
# 
# They are all useful in one way or another
# - This seems like a more nuanced way to say "None" -> None

# # no_longer_useful-Apps

# In[108]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['no_longer_useful_Apps'] = survey_results['no_longer_useful_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['no_longer_useful_Apps'].value_counts())


# In[109]:


## Splitting on ";"
survey_results['no_longer_useful_Apps'] = survey_results['no_longer_useful_Apps'].str.split(', ')  # Split values


# In[110]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['no_longer_useful_Apps'].value_counts())


# In[111]:


no_longer_useful_Apps_counts = survey_results['no_longer_useful_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(no_longer_useful_Apps_counts)


# In[112]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value\
        .replace("Aesthetics (it looks nice/fun)", "Aesthetics")\
        .replace("Personalization (customized learning)", "Personalization")\
        .replace("They are all useful in one way or another to facilitate language learning", "None")\
        .replace("I used to use premade Anki decks", "None")\
        .replace("now I review cards I sentenced mined myself exclusively", "None")\
        .replace("Don't use apps anymore", "None")\
        .replace("Duolingo moves *so* slowly. In terms of focusing on content too long", "None")\
        .replace("in terms of interface quirks just taking up a lot of time over time. It's *so* slow and *so* boring.", "None")
    return value  # Keep non-string values as is

# Apply the transformation to lists
survey_results['no_longer_useful_Apps'] = survey_results['no_longer_useful_Apps'].apply(
    lambda x: sum(([replace_in_list(i)] if isinstance(replace_in_list(i), str) else replace_in_list(i) for i in x), []) 
    if isinstance(x, list) else replace_in_list(x)
)

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('no_longer_useful_Apps')['no_longer_useful_Apps'].unique())  # Check unique values


# In[113]:


survey_results['no_longer_useful_Apps'] = survey_results['no_longer_useful_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

no_longer_useful_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['no_longer_useful_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(no_longer_useful_Apps_counts)


# ## no_longer_useful_Apps conclusion
# 
# Again quite similar process to above, the following entries were changed to "none":
# 
# They are all useful in one way or another to facilitate language learning
# - This participant thinks they are all still useful, so none
# 
# I used to use premade Anki decks, now I review cards I sentenced mined myself exclusively
# - premade decks are not features, they are content made by a community member(s) of a certain app (Anki)
# 
# Don't use apps anymore
# - Difficult to decide here, but since the person doesn't use apps anymore and doesn't specifically mention a feature that is no longer useful to them, counting this as "none" seems like the most accurate decision

# # feel_apps_help-Apps

# In[114]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['feel_apps_help_Apps'] = survey_results['feel_apps_help_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['feel_apps_help_Apps'].value_counts())


# In[115]:


## Splitting on ";"
survey_results['feel_apps_help_Apps'] = survey_results['feel_apps_help_Apps'].str.split(';')  # Split values


# In[116]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['feel_apps_help_Apps'].value_counts())


# In[117]:


feel_apps_help_Apps_counts = survey_results['feel_apps_help_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(feel_apps_help_Apps_counts)


# In[118]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value\
        .replace("To a certain degree", "Yes")\
        .replace("Yes, if I spend time with target language media beyond it.", "Yes")\
        .replace("Yes but not as much as textbooks and classes do", "Yes")\
        .replace("Kind of…", "Maybe")\
        .replace("Most of them do not, with exception for SRS like Anki which helps to retain memories.", "Yes")\
        .replace("not sure.", "Maybe")\
        .replace("The reason anki is good for me is maybe because I can customize it to do whatever I need to", "Yes")\
        .replace("Yes, to some extent. They can be a hinderance because I have found I don't learn as much as I think I am through the apps.", "Yes")\
        .replace("Not really, The Gamified Stuff wastes a lot of time... But Memrise is the only one in this list that still have YouTube shorts, or short videos by natives and AI Roleplay Chatbot for different scenarios", "Maybe")
    return value  # Keep non-string values as is

survey_results['feel_apps_help_Apps'] = survey_results['feel_apps_help_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('feel_apps_help_Apps')['feel_apps_help_Apps'].unique())  # Check unique values


# In[119]:


survey_results['feel_apps_help_Apps'] = survey_results['feel_apps_help_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan"] else item for item in lst] if isinstance(lst, list) else lst
)

feel_apps_help_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['feel_apps_help_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(feel_apps_help_Apps_counts)


# ## feel_apps_help-Apps conclusion
# 
# This column was quite straightforward, although some very interesting comments were added that I was not able to keep in the dataset, but want to mention here to keep the datapoint.
# 
# 
# Yes, to some extent. They can be a hinderance because I have found I don't learn as much as I think I am through the apps.
# - This is a very interesting point, and depending on the apps being used, seems to fall in line with what the initial data of some apps like Duolingo's wordlists imply, also the literature seems to support this to some extent. But this should not necessarily be a general truth for all language learning apps -> Yes
# 
# The reason anki is good for me is maybe because I can customize it to do whatever I need to
# - This participant repeats the usefulness and value of personalisation -> Yes
# 
# To a certain degree
# - -> Yes
# 
# Yes, if I spend time with target language media beyond it.
# - This question is not trying to see if participants think solely using apps is enough, using other methods next to apps is a very valid process, and is likely to help improve the users skills -> Yes
# 
# Yes but not as much as textbooks and classes do
# - A very interesting piece of data, as textbook and classes were voted as least useful by the non-app users, the person clearly said yes so -> Yes
# reference of non-app users votings of least useful study methods
# 1) Classes                              6
# 2) Textbooks                            4
# 
# Kind of…
# - This seems like a way to say "maybe" to me -> Maybe
# 
# Most of them do not, with exception for SRS like Anki which helps to retain memories.
# - This participant is critical of many apps, which is perfectly valid, but also says that a specific app is helping him (anki)/ a specific feature (Space repetition system) -> Yes
# 
# not sure.
# - This feels like a -> Maybe
# 

# # why_continue_usage-Apps

# In[120]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['why_continue_usage_Apps'] = survey_results['why_continue_usage_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['why_continue_usage_Apps'].value_counts())


# In[121]:


## Splitting on ";"
survey_results['why_continue_usage_Apps'] = survey_results['why_continue_usage_Apps'].str.split(', ')  # Split values


# In[122]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['why_continue_usage_Apps'].value_counts())


# In[123]:


why_continue_usage_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['why_continue_usage_Apps'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(why_continue_usage_Apps_counts)


# In[124]:


## Normalizing values.

def replace_in_list(value):
    if isinstance(value, str):  # Only replace if the value is a string
        return value\
        .replace("vocabulary", "nan")\
        .replace("I don't anymore", "I don't use them anymore")\
        .replace("Memorization", "nan")\
        .replace("to retain vocab I come across in immersion", "To build vocabulary")\
        .replace("Review. I have found that is the only good use of apps.", "To build vocabulary")\
        .replace("Everything I have to remember", "nan")\
        .replace("I put into anki. So yes", "nan")\
        .replace("but also grammar points or cultural notes (e.g. I have a flashcard with the question: What and when is the coming of age day?)", "nan")\
        .replace("I stopped using most after reaching high-intermediate level.", "I don't use them anymore")\
        .replace("I don’t really use them anymore", "I don't use them anymore")\
        .replace("To help me study for kanken", "Because they provide a structured learning path")\
        .replace("Study kanji", "To study kanji")\
        .replace("To keep my long streak", "To keep my streak")\
        .replace("I do not currently use apps for language learning", "I don't use them anymore")\
        .replace("to retain kanji", "To study kanji")\
        .replace("Importing my own content or finding what people imported already", "For community reasons")\
        .replace("They are the best way to keep doing it in a pinch", "They help keep me motivated")\
        .replace(" revision). So learning important words thats uncommon is very helpful.", "nan")\
        .replace("I think the repetition part is helpful(you learn something then the same thing comes up again the other day", "To build vocabulary")\
        .replace("It has become a habit at this point.", "It has become a habit")\
        .replace("I don't", "I don't use them anymore")\
        .replace("I don’t", "I don't use them anymore")\
        .replace("free", "nan")\
        .replace("I don't use them anymore use them anymore", "I don't use them anymore")\
        .replace("To build nan", "To build vocabulary")\
        .replace("To build vocabulary;nan","To build vocabulary")\
        .replace("Only Memrise is okay...The Rest Shit..","nan")\
        .replace("culture -- which I find enjoyable. As a note", "nan")\
        .replace("grammar", "To build vocabulary")\
        .replace("To familiarize with all aspects of the language -- vocab","To build vocabulary")\
        .replace("As of Now","nan")\
        .replace("To pass the JLPT,","To pass the JLPT")\
        .replace("I make Anki cards very large context so they're very linguistically/culturally informative.","To build vocabulary")
        
    return value  # Keep non-string values as is

survey_results['why_continue_usage_Apps'] = survey_results['why_continue_usage_Apps'].apply(lambda x: [replace_in_list(i) for i in x] if isinstance(x, list) else replace_in_list(x))

# Check the updated column
with pd.option_context('display.max_rows', None):
    print(survey_results.explode('why_continue_usage_Apps')['why_continue_usage_Apps'].unique())  # Check unique values


# In[125]:


survey_results['why_continue_usage_Apps'] = survey_results['why_continue_usage_Apps'].apply(
    lambda lst: [np.nan if item in ["None", "nan", ""] else item for item in lst] if isinstance(lst, list) else lst
)

## NaN is not possible here, as "none" is replaced by "I don't use them anymore" as such NaN are just faulty values here, so they are not included
why_continue_usage_Apps_counts = survey_results[survey_results['has_participant_used_apps'] == True]['why_continue_usage_Apps'].explode().value_counts()

with pd.option_context('display.max_rows', None):
    print(why_continue_usage_Apps_counts)


# ## why_continue_usage_Apps conclusion
# 
# Quite some entries had to be normalized here:
# 
# First of all, all the different versions of "I don't", "I don't anymore",... were changed to "I don't use them anymore"
# 
# Next some other entries were interpreted in case they seemed like they did indeed fit inside of an existing category:
# 
# I stopped using most after reaching high-intermediate level.
# - This participant doesn't seem to use them anymore -> I don't use them anymore
# I do not currently use apps for language learning
# - This participant also doesn't use apps anymore -> I don't use them anymore
# 
# to retain vocab I come across in immersion 
# - This is the same as building vocab -> To build vocabulary
# Review. I have found that is the only good use of apps. 
# - reviewing (vocab), even when it's grammar points, leads to the bigger umbrella term of building vocab -> To build vocabulary
# I think the repetition part is helpful(you learn something then the same thing comes up again the other day
# - While this seems to aim at an SRS system, SRS systems are mostly used to retain and build vocabulary -> To build vocabulary
# 
# Study kanji
# - Kanji, while they can be learnt individually and out of the context of the words for which they are used, are essentially vocabulary pieces, However, I have decided to keep this as a new category -> To study kanji
# to retain kanji
# - This is also added to the new 'to study kanji' category, as retaining is a part of studying until they are known well enough to be used in reading/writing -> To study kanji
# 
# To practice pitch accent
# - This is an interesting additional category I had not thought of -> To practice pitch accent
# 
# To help me study for kanken
# - Kanken is a specific exam and has books/apps that help prepare for this exam, these apps have a clear path with as goal passing the Kanken exam -> Because they provide a structured learning path
# 
# To keep my long streak
# - An interesting one I hadn't thought of but was covered in the literature review, I expected this to be more of a subconscious thought, it's interesting to see that some people actively think this and know it's their main reason for continuing -> To keep my streak
# 
# Importing my own content or finding what people imported already
# - This is most likely based on Anki, which has a huge community of learners uploading their decks for download by other users -> For community reasons
# 
# They are the best way to keep doing it in a pinch
# - In a pinch can mean many things, while on the train, while short on time, while low on motivation, either way, the closest fitting parameter is motivation -> They help keep me motivated
# 
# It has become a habit at this point.
# - Another very interesting idea I hadn't considered, will be added as is -> It has become a habit
# 
# free
# - This entry doesn't necessarily give a clear reasoning, speaking to people in your native language can also be free, there are also many free book resources (like Tae Kim's grammar guide) etc, so it doesn't feel like a deciding factor to use something, yet none of the existing options seem to fit this answer close enough, so it is kept as is -> Because there are free options
# 
# The following ones were changed to "nan" (empty) as they were additions next to other options, and the options that closest fit these additions were already selected by the participant, as such this would otherwise lead to duplicate data in one row.
# 
# Memorization -> nan
# Everything I have to remember, I put into anki. So yes, vocabulary, but also grammar points or cultural notes (e.g. I have a flashcard with the question: What and when is the coming of age day?) -> nan
#  revision). So learning important words thats uncommon is very helpful. -> nan

# # comparative_enjoyment_other_methods-Apps

# In[126]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['comparative_enjoyment_other_methods_Apps'] = survey_results['comparative_enjoyment_other_methods_Apps'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['comparative_enjoyment_other_methods_Apps'].value_counts())


# In[127]:


##  Turn the datatype into int as I don't need comma values
survey_results['comparative_enjoyment_other_methods_Apps'] = (
    survey_results['comparative_enjoyment_other_methods_Apps']
    .astype(float)  # Convert string numbers like "4.0" to float
    .fillna(0)      # Handle NaN values (optional)
    .astype(int)    # Convert to integer
)

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['comparative_enjoyment_other_methods_Apps'].value_counts())


# ## comparative_enjoyment_other_methods-Apps conclusion
# 
# This was a likert scale question, the datatype is changed to integers without comma values for easier reading and aggregation later on.

# # experienced_intermediate_plateau-Apps

# In[128]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['experienced_intermediate_plateau_Apps'].value_counts())


# In[129]:


# Convert 'Yes' to True and 'No' to False
survey_results['experienced_intermediate_plateau_Apps'] = survey_results['experienced_intermediate_plateau_Apps'].map({'Yes': True, 'No': False})

# Check the updated column
print(survey_results[survey_results['has_participant_used_apps'] == True]['experienced_intermediate_plateau_Apps'])
print(survey_results[survey_results['has_participant_used_apps'] == True]['experienced_intermediate_plateau_Apps'].value_counts())


# In[130]:


## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[survey_results['has_participant_used_apps'] == True]['experienced_intermediate_plateau_Apps'].value_counts())


# ## experienced_intermediate_plateau-Apps conclusion
# 
# Just like with the noApps version, all values were changed to True and False to adhere to the boolean datatype

# # when_start-intermediatePlateau

# In[131]:


test = survey_results[(survey_results["current_level"] != "I really don't know") &
                                                        ((survey_results["experienced_intermediate_plateau_Apps"] == True) |
                                                        (survey_results["experienced_intermediate_plateau_noApps"] == True))]
with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(test[test["current_level"]=="JLPT N4"]["when_start_intermediatePlateau"])


# In[132]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['when_start_intermediatePlateau'] = survey_results['when_start_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['when_start_intermediatePlateau'].value_counts()
         )


# In[133]:


survey_results["when_start_intermediatePlateau"] = survey_results["when_start_intermediatePlateau"]\
.replace("In my 1st year", "0")\
.replace("After 2 years", "2")\
.replace("After 1 year", "1")\
.replace("After 3 years", "3")\
.replace("After 5 years", "5")\
.replace("After 4 years", "4")\
.replace("No idea, comes in waves", "nan")\
.replace("Have experienced it in waves throughout my journey, but I would say early 2022 since it was before I met my tutor", "4")\
.replace("Don't remember", "nan")\
.replace("> 5 years", "4")\
.replace("not sure", "nan")\
.replace("After I left my high school Japanese course (~4 years)", "4")\
.replace("I get stuck when I either know the vocab and but not enough grammar, or know the grammar but don’t know the vocab. I swap between studying these as a I get stuck.", "nan")\
.replace("After i passed N3", "nan")\
.replace("no idea", "nan")\
.replace("After my third year. Then I took a break for a while, and after starting again after 2 years", "3, 5")\
.replace("after around 8 years or so, when my job was stressful", "8")\
.replace("When I started out with Duolingo, about 1 month, I knew progress was slow because it was mainly speaking and listening I needed...but Duolingo is not helpful at all for listening or speaking..", 0)

with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['when_start_intermediatePlateau'].value_counts()
         )


# In[134]:


test = survey_results[(survey_results["current_level"] != "I really don't know") &
                                                        ((survey_results["experienced_intermediate_plateau_Apps"] == True) |
                                                        (survey_results["experienced_intermediate_plateau_noApps"] == True))]
with pd.option_context('display.max_rows', None, 'display.max_colwidth', None):
    print(test[test["current_level"]=="JLPT N4"]["when_start_intermediatePlateau"])


# In[135]:


# Since it unexpetedly made sense to have a double value in one cell, I'll convert everything to lists and split on ", "

##  Turn the datatype into str to split as I don't need comma values
survey_results['when_start_intermediatePlateau'] = (
    survey_results['when_start_intermediatePlateau']
    .astype(str)    # Convert to integer
)
## Splitting on ", "
survey_results['when_start_intermediatePlateau'] = survey_results['when_start_intermediatePlateau'].str.split(', ')  # Split values


# In[136]:


with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['when_start_intermediatePlateau'].value_counts()
         )


# In[137]:


survey_results['when_start_intermediatePlateau'] = survey_results['when_start_intermediatePlateau'].apply(
    lambda lst: [np.nan if item in ["nan"] else item for item in lst] if isinstance(lst, list) else lst
)

## NaN is not possible here, as "none" is replaced by "I don't use them anymore" as such NaN are just faulty values here, so they are not included
when_start_intermediatePlateau_counts = survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['when_start_intermediatePlateau'].explode().value_counts()
    
with pd.option_context('display.max_rows', None):
    print(when_start_intermediatePlateau_counts)


# ## when_start-intermediatePlateau conclusion
# 
# The values were changed from text to numbers to allow for easier aggregation later on.
# "In my first year" was changed to 0 as 0 years have passed since the participant encountered the plateau.
# Participants who were unsure or unclear were changed to 'NaN' or no value since the data is not conclusive for these participants.
# 
# "Have experienced it in waves throughout my journey, but I would say early 2022 since it was before I met my tutor"
# - This participant wrote "A little over 7 years" in the question "how long have you been studying" It is now 2025 and the participant explained they experienced it in 2022 = after 4 years -> 4
# 
# After my third year. Then I took a break for a while, and after starting again after 2 years
# - Since this participant claims to have encountered it twice, two values were kept, namely 3 for the first time, and 5 since the participant experienced it again in the fifth year. -> 3, 5

# # what_level_start-intermediatePlateau

# In[138]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['what_level_start_intermediatePlateau'] = survey_results['what_level_start_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['what_level_start_intermediatePlateau'].value_counts()
         )


# In[139]:


survey_results.loc[
    (survey_results['what_level_start_intermediatePlateau'] == "JLPT N1") & 
    (survey_results["current_level"] == "JLPT N4"), 
    "what_level_start_intermediatePlateau"
] = survey_results["what_level_start_intermediatePlateau"].replace("JLPT N1", "JLPT N5")


# In[140]:


survey_results.loc[
    (survey_results['what_level_start_intermediatePlateau'] == "JLPT N4") & 
    (survey_results["current_level"] == "JLPT N5"), 
    "what_level_start_intermediatePlateau"
] = survey_results["what_level_start_intermediatePlateau"].replace("JLPT N4", "JLPT N5")


# In[141]:


survey_results["what_level_start_intermediatePlateau"] = survey_results["what_level_start_intermediatePlateau"]\
.replace("The very beginning - being most stuck memorising the alphabets.", "JLPT N5")\
.replace("havent done jplt but its so hard to be motivated without guidance and not everyone can self learn", "I do not know")\
.replace("I'm not even at the lowest level yet", "JLPT N5")

with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['what_level_start_intermediatePlateau'].value_counts()
         )


# ## what_level_start-intermediatePlateau conclusion
# 
# In this question, I know some participants whom were still at the lowest levels took the "JLPT N5" level broadly and chose this as they are at that point working towards N5, even though they are not there yet.
# I could have circumvented the >N5 and N5+ groups from being grouped together by creating a "No JLPT level yet" option, but this could have resulted in people who self declare as higher levels, but haven't/hadn't taken an actual exam yet from clicking this as well and creating more disbalance in the data. Now at least I know the N5 group is the only one that contains potentially two (neighboring) groups. On top of that the data of the higher level people is thought to potentially be more valuable for this question, as they have been through the levels and can define what felt like a plateau, even though they may have felt stuck early on, they may later realize that was not the "plateau" but that only happened at a later level for example.
# The fact there are more N5 and N4 people experiencing this is also because there are more N5/N4 participants, it will be interesting to see the values when we normalize the values based on the amount of participants per level and look at the percentages.
# 
# The very beginning - being most stuck memorising the alphabets.
# - Seeing as this participant mentioned the very beginning -> N5
# 
# havent done jplt but its so hard to be motivated without guidance and not everyone can self learn
# - This one is too hard to judge without more context -> NaN
# 
# I'm not even at the lowest level yet
# - This participant is very honest about their current level, but seeing as others have selected N5 in this case -> N5

# # features_helping?-intermediatePlateau

# In[142]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['features_helping_intermediatePlateau'] = survey_results['features_helping_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['features_helping_intermediatePlateau'].value_counts()
         )


# In[143]:


survey_results["features_helping_intermediatePlateau"] = survey_results["features_helping_intermediatePlateau"]\
.replace("To some degree. Streaks become more of a chore, whereas levels and achievements still provide a visual representation of how much you progressed. The latter also provides a goal to strive toward.", "Yes")\
.replace("I think it would help if I actively used those features", "Yes")\
.replace("Gamification helps a Lot for me. But Levels and so on are ony Chocolate coverd Broccoli","Yes")

with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['features_helping_intermediatePlateau'].value_counts()
         )


# ## features_helping?-intermediatePlateau conclusion
# 
# The following values were edited:
# 
# To some degree. Streaks become more of a chore, whereas levels and achievements still provide a visual representation of how much you progressed. The latter also provides a goal to strive toward.
# - While they start with "to some degree", they go on to give examples of parts that they think work, in this sense it seems they agree that they do indeed work -> Yes
# 
# I think it would help if I actively used those features
# - This person thinks they work, but they just don't use it actively enough -> Yes

# # apps_enough_advanced_content-intermediatePlateau

# In[144]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['apps_enough_advanced_content_intermediatePlateau'] = survey_results['apps_enough_advanced_content_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['apps_enough_advanced_content_intermediatePlateau'].value_counts()
         )


# In[145]:


survey_results["apps_enough_advanced_content_intermediatePlateau"] = survey_results["apps_enough_advanced_content_intermediatePlateau"]\
.replace("The only one I've found that helped past this point has been MaruMori", "Yes")\
.replace("nan", "Not sure")\
.replace("On Duolingo, no. As a person in the Unit 30’s of Section 3 on the app, my skill level of understanding is above the lesson usually, and there’s not enough kanji to challenge me either. The only reason I try the lessons at this level is so I can get more vocabulary I might have missed before skipping the rest of that lesson.", "No")\
.replace("Only custom SRS ones like Anki", "Yes")\
.replace("Depends of the app, for Anki definitely since I make my own decks, but other apps like duolingo etc are very beginner focused.", "Yes")\
.replace("only if you provide the content yourself as e.g. in anki", "Yes")\
.replace("I only used flashcards created myself in Anki, so this was never an issue", "Yes")\
.replace("The content is provided by user sentence mining media created by natives for natives.", "Yes")\
.replace("Yes, depending on the app", "Yes")\
.replace("Yes and no - they can provide the tools but they're not enough on their own. To get past the intermediate level they should be a supplement to reading/listening to native materials and speaking to people", "Yes")\
.replace("Depends, as for standart apps, certainly not, there is just not enough areas covered", "No")\
.replace("Kind of...", "Not sure")\
.replace("I use apps where I manage my content myself", "Yes")\
.replace("Pre-made content absolutely not. Anki can if you make your own content.", "Yes")

with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['apps_enough_advanced_content_intermediatePlateau'].value_counts()
         )


# ## apps_enough_advanced_content-intermediatePlateau conclusion
# 
# In this question the idea was to gather whether participants think apps provide enough content to help them get over the intermediate plateau. This is seen as a general question about "apps" where every app is taken into the equation. Some participants explained how they think certain apps are useful for this, while others are not. These have generally been changed to "Yes" as the specific apps themselves are not important for this question, those are most likely answered in the "what apps are most/least useful" parts.
# 
# A few answers were interpreted as follows:
# 
# The only one I've found that helped past this point has been MaruMori
# - Since they mention that an app seems to help them -> Yes
# 
# nan
# - This participant ended up filling in an empty "other" -> Not sure
# 
# On Duolingo, no. As a person in the Unit 30’s of Section 3 on the app, my skill level of understanding is above the lesson usually, and there’s not enough kanji to challenge me either. The only reason I try the lessons at this level is so I can get more vocabulary I might have missed before skipping the rest of that lesson.
# - While this person specifically talks about duolingo, they don't introduce other apps that may lead to believing they think "Yes" -> No
# 
# Depends, as for standart apps, certainly not, there is just not enough areas covered
# - They don't mention anything that makes me believe they think "yes", whilst specifically mentioning for "standard apps no" -> No
# 
# Only custom SRS ones like Anki
# - They have an app that helps them -> Yes
# 
# Depends of the app, for Anki definitely since I make my own decks, but other apps like duolingo etc are very beginner focused.
# - They have an app that helps them -> Yes
# 
# only if you provide the content yourself as e.g. in anki
# - They have an app that helps them -> Yes
# 
# I only used flashcards created myself in Anki, so this was never an issue
# - They have an app that helps them -> Yes
# 
# The content is provided by user sentence mining media created by natives for natives.
# - Based on the explanation I can say with pretty good confidence that they are talking about the anki community decks, as such they have an app that helps them -> Yes
# 
# Yes, depending on the app
# - They have an app that helps them -> Yes
# 
# Yes and no - they can provide the tools but they're not enough on their own. To get past the intermediate level they should be a supplement to reading/listening to native materials and speaking to people
# - While they bring up interesting points for both sides, the fact they say apps can help with this makes me lean towards "Yes" for this answer -> Yes

# # tried_techniques_to_combat-intermediatePlateau

# In[146]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['tried_techniques_to_combat_intermediatePlateau'] = survey_results['tried_techniques_to_combat_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['tried_techniques_to_combat_intermediatePlateau'].value_counts()
         )


# ## tried_techniques_to_combat-intermediatePlateau conclusion
# 
# As this was an optional, open question, the answers are kept as is. Interesting is that a good amount of people decided to give their opinion, which can lead to interesting insights!

# # most_challenging_to_progress-intermediatePlateau

# In[147]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['most_challenging_to_progress_intermediatePlateau'] = survey_results['most_challenging_to_progress_intermediatePlateau'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results[
        (survey_results['experienced_intermediate_plateau_Apps'] == True)|
          (survey_results['experienced_intermediate_plateau_noApps'] == True)
    ]['most_challenging_to_progress_intermediatePlateau'].value_counts()
         )


# ## most_challenging_to_progress-intermediatePlateau conclusion
# 
# Just like above, this was also an optional, open question, thus the answers are kept as is. even more people gave their opinion in this part, which is very exciting to see!

# # how_found_survey-final

# In[148]:


## First step, remove leading and trailing spaces so that values can easily be targeted for alteration
survey_results['how_found_survey_final'] = survey_results['how_found_survey_final'].astype(str).str.strip()

## Print all current values and count them, make sure to print all the values
with pd.option_context('display.max_rows', None):
    print(survey_results['how_found_survey_final'].value_counts(dropna=False)
         )


# ## how_found_survey-final conclusion
# 
# This column is only used to put answers in perspective when necessary (for example if there is a big disconnect in the amount of people voting for Duolingo, I can then find out how many of those came from the duolingo subreddit, which will have a specific bias to said application)

# In[149]:


# Deduplicate per row so that in case someone selected that they use "Apps", but then also selected other and wrote "Duolingo" which then got changedt to "Apps", that participant doesn't have "Apps, Apps" as a value, adding false data

def remove_duplicates_ordered(lst):
    if isinstance(lst, list):  # Ensure it's a list
        return list(dict.fromkeys(lst))  # Preserves order while removing duplicates
    return lst  # Return as is if not a list

# Apply to entire DataFrame (each cell in every column)
survey_results = survey_results.map(remove_duplicates_ordered)


# In[150]:


survey_results.to_csv("survey_results_cleaned.csv", index=False)
# First exported as CSV, but then realised this means I lose all my code data and lists become strings etc when re-imported later on


# In[151]:


survey_results.to_json("survey_results_cleaned.json", orient="records")  # Save


# In[152]:


main_study_method_counts = survey_results['main_study_method'].explode().value_counts(dropna=False)

with pd.option_context('display.max_rows', None):
    print(main_study_method_counts)

