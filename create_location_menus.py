import pandas as pd
import os

# Define input and output directories
input_file = "CSV/scored_food.csv"
output_dir = "CSV/location_menu_tables"
os.makedirs(output_dir, exist_ok=True)

# Load CSV file
df = pd.read_csv(input_file)

# Get unique locations
unique_locations = df["location_name"].unique()[:10]  # First 10 unique locations

# Split and save CSV files
for location in unique_locations:
    location_df = df[df["location_name"] == location]
    output_file = os.path.join(output_dir, f"{location.replace(' ', '_')}.csv")
    location_df.to_csv(output_file, index=False)
    
print("CSV files successfully created for the first 10 unique locations.")
