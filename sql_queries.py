import pandas as pd
from sqlalchemy import create_engine

# Database Configuration (replace with your own credentials)
DATABASE_URI = 'mysql+mysqlconnector://root:Amphi%4055@localhost:3306/cs'

# Create SQLAlchemy engine to connect to MySQL
engine = create_engine(DATABASE_URI)

# Query 1: Total runs scored by each batter in Test Matches
query_1 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM test_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_1 = pd.read_sql(query_1, con=engine)
print("Query 1 - Total runs by each batter in Test Matches:")
print(df_1)

# Query 2: Total runs scored by each batter in ODI Matches
query_2 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM odi_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_2 = pd.read_sql(query_2, con=engine)
print("Query 2 - Total runs by each batter in ODI Matches:")
print(df_2)

# Query 3: Total runs scored by each batter in T20 Matches
query_3 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM t20_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_3 = pd.read_sql(query_3, con=engine)
print("Query 3 - Total runs by each batter in T20 Matches:")
print(df_3)

# Query 4: Top 5 players with maximum runs in Test Matches
query_4 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM test_matches
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 5;
"""
df_4 = pd.read_sql(query_4, con=engine)
print("Query 4 - Top 5 players with max runs in Test Matches:")
print(df_4)

# Query 5: Top 5 players with maximum runs in ODI Matches
query_5 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM odi_matches
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 5;
"""
df_5 = pd.read_sql(query_5, con=engine)
print("Query 5 - Top 5 players with max runs in ODI Matches:")
print(df_5)

# Query 6: Top 5 players with maximum runs in T20 Matches
query_6 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM t20_matches
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 5;
"""
df_6 = pd.read_sql(query_6, con=engine)
print("Query 6 - Top 5 players with max runs in T20 Matches:")
print(df_6)

# Query 7: Total wickets taken by each bowler in Test Matches
query_7 = """
SELECT bowler, COUNT(DISTINCT player_dismissed) AS total_wickets
FROM test_matches
GROUP BY bowler
ORDER BY total_wickets DESC;
"""
df_7 = pd.read_sql(query_7, con=engine)
print("Query 7 - Total wickets taken by each bowler in Test Matches:")
print(df_7)

# Query 8: Total wickets taken by each bowler in ODI Matches
query_8 = """
SELECT bowler, COUNT(DISTINCT player_dismissed) AS total_wickets
FROM odi_matches
GROUP BY bowler
ORDER BY total_wickets DESC;
"""
df_8 = pd.read_sql(query_8, con=engine)
print("Query 8 - Total wickets taken by each bowler in ODI Matches:")
print(df_8)

# Query 9: Total wickets taken by each bowler in T20 Matches
query_9 = """
SELECT bowler, COUNT(DISTINCT player_dismissed) AS total_wickets
FROM t20_matches
GROUP BY bowler
ORDER BY total_wickets DESC;
"""
df_9 = pd.read_sql(query_9, con=engine)
print("Query 9 - Total wickets taken by each bowler in T20 Matches:")
print(df_9)

# Query 10: Players who have faced the most balls in Test Matches
query_10 = """
SELECT batter, SUM(runs_batter) AS total_runs, COUNT(runs_batter) AS balls_faced
FROM test_matches
GROUP BY batter
ORDER BY balls_faced DESC
LIMIT 5;
"""
df_10 = pd.read_sql(query_10, con=engine)
print("Query 10 - Players who faced the most balls in Test Matches:")
print(df_10)

# Query 11: Players who have faced the most balls in ODI Matches
query_11 = """
SELECT batter, SUM(runs_batter) AS total_runs, COUNT(runs_batter) AS balls_faced
FROM odi_matches
GROUP BY batter
ORDER BY balls_faced DESC
LIMIT 5;
"""
df_11 = pd.read_sql(query_11, con=engine)
print("Query 11 - Players who faced the most balls in ODI Matches:")
print(df_11)

# Query 12: Players who have faced the most balls in T20 Matches
query_12 = """
SELECT batter, SUM(runs_batter) AS total_runs, COUNT(runs_batter) AS balls_faced
FROM t20_matches
GROUP BY batter
ORDER BY balls_faced DESC
LIMIT 5;
"""
df_12 = pd.read_sql(query_12, con=engine)
print("Query 12 - Players who faced the most balls in T20 Matches:")
print(df_12)

# Query 13: Highest batting strike rate in Test Matches (runs per 100 balls)
query_13 = """
SELECT batter, SUM(runs_batter) / COUNT(runs_batter) * 100 AS strike_rate
FROM test_matches
GROUP BY batter
ORDER BY strike_rate DESC
LIMIT 5;
"""
df_13 = pd.read_sql(query_13, con=engine)
print("Query 13 - Highest batting strike rate in Test Matches:")
print(df_13)

# Query 14: Highest batting strike rate in ODI Matches (runs per 100 balls)
query_14 = """
SELECT batter, SUM(runs_batter) / COUNT(runs_batter) * 100 AS strike_rate
FROM odi_matches
GROUP BY batter
ORDER BY strike_rate DESC
LIMIT 5;
"""
df_14 = pd.read_sql(query_14, con=engine)
print("Query 14 - Highest batting strike rate in ODI Matches:")
print(df_14)

# Query 15: Highest batting strike rate in T20 Matches (runs per 100 balls)
query_15 = """
SELECT batter, SUM(runs_batter) / COUNT(runs_batter) * 100 AS strike_rate
FROM t20_matches
GROUP BY batter
ORDER BY strike_rate DESC
LIMIT 5;
"""
df_15 = pd.read_sql(query_15, con=engine)
print("Query 15 - Highest batting strike rate in T20 Matches:")
print(df_15)

# Query 16: Total number of extra runs (legbyes, noballs, wides) in Test Matches
query_16 = """
SELECT SUM(runs_extras) AS total_extras
FROM test_matches;
"""
df_16 = pd.read_sql(query_16, con=engine)
print("Query 16 - Total number of extra runs in Test Matches:")
print(df_16)

# Query 17: Total number of extra runs (legbyes, noballs, wides) in ODI Matches
query_17 = """
SELECT SUM(runs_extras) AS total_extras
FROM odi_matches;
"""
df_17 = pd.read_sql(query_17, con=engine)
print("Query 17 - Total number of extra runs in ODI Matches:")
print(df_17)

# Query 18: Total number of extra runs (legbyes, noballs, wides) in T20 Matches
query_18 = """
SELECT SUM(runs_extras) AS total_extras
FROM t20_matches;
"""
df_18 = pd.read_sql(query_18, con=engine)
print("Query 18 - Total number of extra runs in T20 Matches:")
print(df_18)

# Query 19: Number of times a batter got out in Test Matches
query_19 = """
SELECT batter, COUNT(player_dismissed) AS outs
FROM test_matches
WHERE player_dismissed IS NOT NULL
GROUP BY batter
ORDER BY outs DESC;
"""
df_19 = pd.read_sql(query_19, con=engine)
print("Query 19 - Number of times a batter got out in Test Matches:")
print(df_19)

# Query 20: Number of times a batter got out in ODI Matches
query_20 = """
SELECT batter, COUNT(player_dismissed) AS outs
FROM odi_matches
WHERE player_dismissed IS NOT NULL
GROUP BY batter
ORDER BY outs DESC;
"""
df_20 = pd.read_sql(query_20, con=engine)
print("Query 20 - Number of times a batter got out in ODI Matches:")
print(df_20)
