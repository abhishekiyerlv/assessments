# -*- coding: utf-8 -*-
"""LVADSUSE137_AbhishekIyer_Final_assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iYZtLhkdK5d4nynExnY7Rtt7BMjqwq5N
"""

#Importing the data and preliminary analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/Final Dataset - IPL.csv")

df.head()

df.info()

#Cleaning the data and checking for duplicates
df.isna().sum()

#After summing up the NA values, we can see that there are no NULL values

df.duplicated()

_## We can see that there are no null values neither are there any duplicate values

# Descripting statistics

numeric_df = df.select_dtypes([int,float])
numeric_df.head()

#Mean
numeric_df.mean()

#Median
numeric_df.median()

#Std
numeric_df.std()

#Min
numeric_df.min()

#Max
numeric_df.max()

#Range
numeric_df.max() - numeric_df.min()

#Data Visualization
result = df.groupby('team1').first_ings_score.mean().reset_index()
result = pd.DataFrame(result)
result.head()

plt.bar(result.team1, result.first_ings_score)
plt.xticks(rotation = 90)
plt.title("Teams Vs Average_score")
plt.xlabel("Teams")
plt.ylabel('Average score')
plt.show()

#We can see that punjab has scored the most amount of runs whenever they batted first.

result1 = df.groupby('team2').second_ings_score.mean().reset_index()
result1 = pd.DataFrame(result1)
result1.head()

plt.bar(result1.team2, result1.second_ings_score)
plt.xticks(rotation = 90)
plt.title("Teams Vs Average_score")
plt.xlabel("Teams")
plt.ylabel('Average score')
plt.show()

#We can see that Chennai has scored the most amount of runs while batting in the second innnings this season

df.match_winner.value_counts().plot.pie(autopct = '%.f%%')
plt.title('Percentage of wins by Teams')

#Rajasthan has the most amount of wins

POM = df.player_of_the_match.value_counts()
POM = POM.head(5)

sns.barplot(POM)
plt.title("Top 5 Players")
plt.xlabel("Player Name")
plt.ylabel("Count of titles")
plt.xticks(rotation = 45)
plt.show()

#According to the visualizaiton, we can see that Kuldeep Yadav has recieved the
#most amount of Player of the match titles

# TOP BOWLERS
BB = df.best_bowling.value_counts()
BB = BB.head(10)

sns.barplot(BB)
plt.title("Top 10 Best bowlers")
plt.xlabel('Player names')
plt.ylabel('Number titles won')
plt.xticks(rotation = 45)
plt.show()

plt.scatter(df.first_ings_score, df.second_ings_score,color='g')
plt.title("Scatter plot of first and second innings scores")
plt.xlabel("First innings")
plt.ylabel("Seccond innings")
plt.show()

#We can see that there is a degree of correlation between the first innings and second innings scores

sns.histplot(df.first_ings_score, bins=15, alpha=0.5,color='b')
sns.histplot(df.second_ings_score, bins=15, alpha = 0.5,color='r')
plt.show()

#Here we can see that most of the histogram is interesected. The first innings scores and the second innings
#scores are almost similar. We can see that there is a higher frequency of the first team scoring more than
#200 runs than that of the second.

Q3 =  df.first_ings_score.quantile(0.75)
Q1 = df.first_ings_score.quantile(0.25)
iqr = Q3 - Q1
lb = Q1-1.5*iqr
ub = Q3+1.5*iqr
df_out = df[(df['first_ings_score']>lb) & (df['first_ings_score']<ub)]
df

#These are the outliers of the data, we are going to keep this data because it is
#crucial in deciding who wins and who loses the matches.

#Group by TEAM and venue
df['Team1W'] = df.apply(lambda row: 1 if row.team1 == row.match_winner else 0, axis = 1)
df.head()

TeamP = df.groupby(['team1', 'venue']).agg({'Team1W':'sum'}).reset_index()
TeamP = pd.DataFrame(TeamP)
TeamP

#Player of the Match
POM = df.player_of_the_match.value_counts()
POM = POM.head(10)

sns.barplot(POM)
plt.title("Top 5 Players")
plt.xlabel("Player Name")
plt.ylabel("Count of titles")
plt.xticks(rotation = 45)
plt.show()

BB = df.best_bowling.value_counts()
BB = BB.head(10)

sns.barplot(BB)
plt.title("Top 10 Best bowlers")
plt.xlabel('Player names')
plt.ylabel('Number titles won')
plt.xticks(rotation = 45)
plt.show()

#5 Identifying relationships
df.info()
#lambda row: 1 if row['toss_winner'] == row['match_winner']  else 0
df['toss'] = df.apply(lambda row: 1 if row['toss_winner'] == row['match_winner']  else 0, axis = 1)
df.head()

corr = df.groupby('team1').toss.value_counts().reset_index()
corr

#Now we have the data of wins when toss was won or lost
toss_won = corr[corr.toss == 1]
toss_lost = corr[corr.toss == 0]

toss_won.head()

toss_lost.head()

x = np.arange(len(toss_won.team1))
plt.plot(x, toss_won.count, label = 'Won')
plt.plot(x, toss_lost.count, label='Lost')
plt.title()
plt.show()

"""## Analysis:

After analyzing the graphs given below, we have generated several insights on various topics.
The insights generated are as follows:


1.   The difference between the mean and median was not great enough for it to be considered a skewed data.
2.  The data did not contain any duplicate or null values.
3. Most of the histogram is interesected.
4. The first innings scores and the second innings
scores are almost similar. - histogram
5. There is a higher frequency of the first team scoring more than
200+ runs than that of the second. - histogram
6. There is a degree of correlation between the first innings and second innings scores - scatter plot
7. There are the outliers in the data and we decide to keep this data because it is crucial in deciding who wins and who loses the matches.
8. Teams from Bangalore and Delhi perform better in the Mumbai stadiums
9. Chennai performs the least in the Mumbai stadiums -Data from the previous question
10. Kuldeep Yadav is the best player of the season with 4 titles won
11. Yuzvendra chahal is the best bowler of the season with 5 titles won.

"""