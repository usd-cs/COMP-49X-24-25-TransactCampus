import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

df_transactions  = pd.read_csv("transactions.csv")
df_menu = pd.read_csv("ScoredGradedCategorizedMenuData.csv")

# Merge transactions with menu to get food_score
df_transactions['released_datetime'] = pd.to_datetime(df_transactions['released_datetime'])
df = df_transactions.merge(
    df_menu[['food_id', 'food_score']],
    on='food_id',
    how='left'
)

# Parameters
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 5, 31)
window_size = 14  # days
n_clusters = 4 # based off of elbow method

results = []

window_start = start_date
while window_start + timedelta(days=window_size) <= end_date:
    window_end = window_start + timedelta(days=window_size)
    df_window = df[
        (df['released_datetime'] >= window_start) &
        (df['released_datetime'] < window_end)
    ]
    if df_window.empty:
        window_start += timedelta(days=window_size)
        continue

    student_feats = df_window.groupby('userid').agg(
        avg_score      = ('food_score', 'mean'),
        std_score      = ('food_score', 'std'),
        total_items    = ('number_of_items', 'sum'),
        distinct_foods = ('food_id', 'nunique'),
    ).fillna(0)

    if len(student_feats) < n_clusters:
        window_start += timedelta(days=window_size)
        continue

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(student_feats)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    student_feats['cluster'] = clusters

    cluster_names = {0: 'moderate', 1: 'mixed', 2: 'risky', 3: 'favorable'}
    cluster_sizes = student_feats['cluster'].value_counts().sort_index()
    for cluster_id, size in cluster_sizes.items():
        results.append({
            'window_start': window_start.strftime('%Y-%m-%d'),
            'window_end': (window_end - timedelta(days=1)).strftime('%Y-%m-%d'),
            'cluster': cluster_id,
            'cluster_name': cluster_names.get(cluster_id, str(cluster_id)),
            'size': size
        })

    window_start += timedelta(days=window_size)

# Save results to CSV
df_results = pd.DataFrame(results)
df_results.to_csv("cluster_sizes_over_time.csv", index=False)

# Plot line graph
plt.figure(figsize=(10,6))
for cluster_id in range(n_clusters):
    cluster_data = df_results[df_results['cluster'] == cluster_id]
    plt.plot(
        cluster_data['window_start'],
        cluster_data['size'],
        marker='o',
        label=cluster_names.get(cluster_id, str(cluster_id))
    )
plt.xlabel('Window Start Date')
plt.ylabel('Cluster Size')
plt.title('Cluster Sizes Over Time (2-week windows)')
plt.xticks(rotation=45)
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()