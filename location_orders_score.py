import pandas as pd

df_txn  = pd.read_csv("transactions.csv")
df_menu = pd.read_csv("ScoredGradedCategorizedMenuData.csv")
df = df_txn.merge(df_menu[['food_id','food_score']], on='food_id', how='left')

# Sort weight by quantity
df['weighted_score'] = df['food_score'] * df['number_of_items']

# Group by location:
loc_stats = df.groupby('locationid').agg(
    avg_score = ('food_score', 'mean'),
    total_weighted = ('weighted_score', 'sum'),
    total_items = ('number_of_items', 'sum'),
).reset_index()

# Get average
loc_stats['weighted_avg_score'] = (
    loc_stats['total_weighted'] / loc_stats['total_items']
)

loc_avg_scores = loc_stats[['locationid','avg_score','weighted_avg_score']]

print(loc_avg_scores.head())

loc_avg_scores.to_csv("location_avg_scores.csv", index=False)

print("Wrote location averages to location_avg_scores.csv")