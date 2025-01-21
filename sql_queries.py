import pandas as pd
import mysql.connector

# Database Configuration (updated with your connection details)
db_config = {
    "host": "localhost",   # Hostname of the MySQL server
    "user": "root",        # MySQL username
    "password": "Amphi@55",# MySQL password
    "database": "cs",      # Database name
    "port": 3306,          # MySQL server port
}

# Create a connection to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    print("Database connection successful.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Function to execute a query and return the result as a DataFrame
def execute_query(query):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        cursor.close()
        return df
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return pd.DataFrame()

# Query 1: Total runs scored by each batter in Test Matches
query_1 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM test_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_1 = execute_query(query_1)
print("Query 1 - Total runs by each batter in Test Matches:")
print(df_1)

# Query 2: Total runs scored by each batter in ODI Matches
query_2 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM odi_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_2 = execute_query(query_2)
print("Query 2 - Total runs by each batter in ODI Matches:")
print(df_2)

# Query 3: Total runs scored by each batter in T20 Matches
query_3 = """
SELECT batter, SUM(runs_batter) AS total_runs
FROM t20_matches
GROUP BY batter
ORDER BY total_runs DESC;
"""
df_3 = execute_query(query_3)
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
df_4 = execute_query(query_4)
print("Query 4 - Top 5 players with max runs in Test Matches:")
print(df_4)

# Query 5: Total wickets taken by each bowler in Test Matches
query_5 = """
SELECT bowler, COUNT(DISTINCT player_dismissed) AS total_wickets
FROM test_matches
GROUP BY bowler
ORDER BY total_wickets DESC;
"""
df_5 = execute_query(query_5)
print("Query 5 - Total wickets taken by each bowler in Test Matches:")
print(df_5)

# Query 6: Players who have faced the most balls in Test Matches
query_6 = """
SELECT batter, SUM(runs_batter) AS total_runs, COUNT(runs_batter) AS balls_faced
FROM test_matches
GROUP BY batter
ORDER BY balls_faced DESC
LIMIT 5;
"""
df_6 = execute_query(query_6)
print("Query 6 - Players who faced the most balls in Test Matches:")
print(df_6)

# Query 7: Total number of extra runs (legbyes, noballs, wides) in Test Matches
query_7 = """
SELECT SUM(runs_extras) AS total_extras
FROM test_matches;
"""
df_7 = execute_query(query_7)
print("Query 7 - Total number of extra runs in Test Matches:")
print(df_7)

# Closing the database connection
conn.close()
print("Database connection closed.")
