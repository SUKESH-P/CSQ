import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

# Database Configuration
DATABASE_URI = 'mysql://root:Amphi%4055@localhost:3306/cs'

engine = create_engine(DATABASE_URI)

# Function to create SQL tables
# Function to create SQL tables with all required columns
def create_tables():
    metadata = MetaData()

    # Define table schema with the exact columns you mentioned
    match_types = ['test_matches', 'odi_matches', 't20_matches']
    for match_type in match_types:
        Table(
            match_type, metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('inning', String(255)),
            Column('over', Integer),
            Column('batting_team', String(255)),
            Column('match_type', String(255)),
            Column('teams', String(255)),
            Column('date', Date),
            Column('venue', String(255)),
            Column('winner', String(255)),
            Column('players', String(255)),  # List of players
            Column('batter', String(255)),
            Column('bowler', String(255)),
            Column('non_striker', String(255)),
            Column('runs_batter', Integer),
            Column('runs_extras', Integer),
            Column('runs_total', Integer),
            Column('extras_wides', Integer),
            Column('extras_byes', Integer),
            Column('extras_noballs', Integer),
            Column('extras_legbyes', Integer),
            Column('extras_penalty', Integer)
        )

    # Create all tables in the database
    metadata.create_all(engine)
    print("SQL tables created successfully!")

# Function to populate data into SQL tables
def populate_data(csv_file, table_name):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Write data to SQL table
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Data from {csv_file} has been inserted into the {table_name} table.")

# Main script
if __name__ == "__main__":
    # Create tables
    create_tables()

    # Define paths to CSV files
    csv_dir = r"C:\Users\Sukkiiii\Desktop\ME_DATA\transformed"
    csv_files = {
        "Test_matches": os.path.join(csv_dir, "Test_matches.csv"),
        "odi_matches": os.path.join(csv_dir, "ODI_matches.csv"),
        "t20_matches": os.path.join(csv_dir, "T20_matches.csv")
    }

    # Populate tables
    for table, csv_file in csv_files.items():
        if os.path.exists(csv_file):
            populate_data(csv_file, table)
        else:
            print(f"CSV file not found for {table}: {csv_file}")
