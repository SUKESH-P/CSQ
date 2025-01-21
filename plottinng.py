import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data (assuming the data is in CSV format)
test_matches = pd.read_csv('Test_matches.csv')
odi_matches = pd.read_csv('ODI_matches.csv')
t20_matches = pd.read_csv('T20_matches.csv')

# General Overview of the Data
print(test_matches.info())
print(odi_matches.info())
print(t20_matches.info())

# Descriptive Statistics
print(test_matches.describe())
print(odi_matches.describe())
print(t20_matches.describe())

# 1. Distribution of Runs Scored by Batters in Test Matches
plt.figure(figsize=(10,6))
sns.histplot(test_matches['runs_batter'], kde=True, color='blue')
plt.title('Distribution of Runs Scored by Batters in Test Matches')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.show()

# 2. Runs Scored vs Wickets Taken in ODI Matches
odi_summary = odi_matches.groupby('batting_team').agg({'runs_total':'sum', 'runs_extras':'sum'}).reset_index()
plt.figure(figsize=(10,6))
sns.scatterplot(data=odi_summary, x='runs_total', y='runs_extras', hue='batting_team')
plt.title('Runs Scored vs Extras in ODI Matches')
plt.xlabel('Total Runs')
plt.ylabel('Extras Runs')
plt.show()

# 3. Top 10 Batters with Most Runs in T20 Matches
t20_batter_runs = t20_matches.groupby('batter')['runs_batter'].sum().reset_index()
t20_batter_runs = t20_batter_runs.sort_values(by='runs_batter', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=t20_batter_runs, x='batter', y='runs_batter', palette='viridis')
plt.title('Top 10 Batters with Most Runs in T20 Matches')
plt.xticks(rotation=45)
plt.xlabel('Batter')
plt.ylabel('Total Runs')
plt.show()

# 4. Correlation Heatmap of Runs and Extras
correlation = test_matches[['runs_batter', 'runs_extras', 'runs_total']].corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Test Matches')
plt.show()

# 5. Runs Scored by Each Team in Test Matches (Bar Plot)
test_team_runs = test_matches.groupby('teams')['runs_total'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=test_team_runs, x='teams', y='runs_total', palette='Blues')
plt.title('Total Runs Scored by Each Team in Test Matches')
plt.xticks(rotation=45)
plt.xlabel('Teams')
plt.ylabel('Total Runs')
plt.show()

# 6. Runs Scored by Players Who Did Not Get Dismissed in ODI Matches
odi_no_dismissal = odi_matches[odi_matches['player_dismissed'].isnull()]
odi_no_dismissal = odi_no_dismissal.groupby('batter')['runs_batter'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=odi_no_dismissal, x='batter', y='runs_batter', palette='YlGnBu')
plt.title('Runs Scored by Players Who Did Not Get Dismissed in ODI Matches')
plt.xticks(rotation=45)
plt.xlabel('Batter')
plt.ylabel('Runs Scored')
plt.show()

# 7. Line Plot for Total Runs Scored by Each Team Over Time
test_matches['date'] = pd.to_datetime(test_matches['date'])
team_runs_over_time = test_matches.groupby([test_matches['date'].dt.year, 'teams'])['runs_total'].sum().reset_index()

plt.figure(figsize=(12,8))
sns.lineplot(data=team_runs_over_time, x='date', y='runs_total', hue='teams')
plt.title('Total Runs Scored by Each Team Over Time (Test Matches)')
plt.xlabel('Year')
plt.ylabel('Total Runs')
plt.legend(title='Teams', loc='upper left')
plt.show()

# 8. Boxplot for Runs Scored by Teams in T20 Matches
plt.figure(figsize=(10,6))
sns.boxplot(data=t20_matches, x='batting_team', y='runs_total', palette='Set2')
plt.title('Runs Scored by Teams in T20 Matches')
plt.xticks(rotation=45)
plt.xlabel('Batting Team')
plt.ylabel('Runs Scored')
plt.show()

# 9. Pie Chart for Distribution of Match Types
match_types = ['Test', 'ODI', 'T20']
match_counts = [test_matches.shape[0], odi_matches.shape[0], t20_matches.shape[0]]

plt.figure(figsize=(8,8))
plt.pie(match_counts, labels=match_types, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Match Types')
plt.show()

# 10. 3D Scatter Plot for Runs vs Wickets vs Matches Played
fig = px.scatter_3d(test_matches, x='runs_total', y='runs_extras', z='inning', color='teams')
fig.update_layout(title='3D Scatter Plot: Runs vs Wickets vs Matches Played')
fig.show()
