import os
import json
import pandas as pd

# Define input directories for each format
input_dirs = {
    "Test": r"C:\Users\Sukkiiii\Desktop\ME_DATA\tests_json",
    "ODI": r"C:\Users\Sukkiiii\Desktop\ME_DATA\odis_json",
    "T20": r"C:\Users\Sukkiiii\Desktop\ME_DATA\t20s_json"
}

# Define the output directory
output_dir = r"C:\Users\Sukkiiii\Desktop\ME_DATA\transformed"
os.makedirs(output_dir, exist_ok=True)

# Function to parse JSON files
def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract match-level metadata from the "info" section
    info = data.get('info', {})
    match_type = info.get('match_type', 'Unknown')
    teams = info.get('teams', [])
    date = info.get('dates', [None])[0]
    venue = info.get('venue', 'Unknown')  # Adjusted for "venue" field
    toss = info.get('toss', {})
    winner = info.get('outcome', {}).get('winner', 'Unknown')

    # Collecting player data
    players = info.get('players', {})
    players_str = {team: ', '.join(players.get(team, [])) for team in teams}

    # Extracting the deliveries data from innings
    deliveries = []
    innings = data.get('innings', [])
    
    for inning in innings:
        team_name = inning.get('team', 'Unknown')
        for over in inning.get('overs', []):
            over_number = over.get('over', -1)
            for delivery in over.get('deliveries', []):
                delivery_data = {
                    'inning': team_name,
                    'over': over_number,
                    'batting_team': team_name,
                    'match_type': match_type,
                    'teams': ', '.join(teams),
                    'date': date,
                    'venue': venue,
                    'winner': winner,
                    'players': players_str.get(team_name, 'Unknown'),
                    'batter': delivery.get('batter', 'Unknown'),
                    'bowler': delivery.get('bowler', 'Unknown'),
                    'non_striker': delivery.get('non_striker', 'Unknown'),
                    'runs_batter': delivery.get('runs', {}).get('batter', 0),
                    'runs_extras': delivery.get('runs', {}).get('extras', 0),
                    'runs_total': delivery.get('runs', {}).get('total', 0)
                }
                # Adding extras (if any)
                extras = delivery.get('extras', {})
                for extra_type, extra_count in extras.items():
                    delivery_data[f'extras_{extra_type}'] = extra_count

                deliveries.append(delivery_data)

    return pd.DataFrame(deliveries)

# Function to process a directory and save data for a specific match type
def process_matches(match_type, directory, output_dir):
    if not os.path.exists(directory):
        print(f"Directory not found for {match_type}: {directory}")
        return

    match_data = []  # To store data for all matches of this type

    # Iterate through all JSON files in the directory
    json_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json')]
    for file in json_files:
        try:
            print(f"Processing {match_type} match file: {file}")
            df = parse_json(file)
            match_data.append(df)
        except Exception as e:
            print(f"Unexpected error processing {file}: {e}")
            continue

    # Combine all data and save to a CSV file
    if match_data:
        combined_df = pd.concat(match_data, ignore_index=True)
        output_file = os.path.join(output_dir, f"{match_type}_matches.csv")
        combined_df.to_csv(output_file, index=False)
        print(f"Saved {match_type} matches to {output_file}")
    else:
        print(f"No data found for {match_type} matches.")

# Process each match type
for match_type, directory in input_dirs.items():
    process_matches(match_type, directory, output_dir)

print("Data processing complete. Separate CSV files have been generated for Test, ODI, and T20 matches.")
