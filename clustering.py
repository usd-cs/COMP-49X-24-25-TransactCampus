import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

df_transactions  = pd.read_csv("transactions.csv")

# Filter to last 2 weeks of data
end_date = datetime(2024, 5, 31)
start_date = end_date - timedelta(days=14)
df_transactions['released_datetime'] = pd.to_datetime(df_transactions['released_datetime'])
df_transactions = df_transactions[
    (df_transactions['released_datetime'] >= start_date) &
    (df_transactions['released_datetime'] < end_date)
]

df_menu = pd.read_csv("ScoredGradedCategorizedMenuData.csv")

# Merge transactions with menu to get food_score
df = df_transactions.merge(
    df_menu[['food_id', 'food_score']],
    on='food_id',
    how='left'
)

student_feats = df.groupby('userid').agg(
    avg_score      = ('food_score', 'mean'),
    std_score      = ('food_score', 'std'),
    total_items    = ('number_of_items', 'sum'),
    distinct_foods = ('food_id', 'nunique'),
).fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(student_feats)

# Elbow method to find optimal number of clusters
inertias = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(k_range, inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.tight_layout()
plt.show()

# Run KMeans
n_clusters = 4 # based off of elbow method
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
student_feats['cluster'] = kmeans.fit_predict(X_scaled)

print(student_feats['cluster'].value_counts())

# Scatter plot in original feature space
plt.figure(figsize=(8,6))
plt.scatter(
    student_feats['avg_score'],
    student_feats['total_items'],
    c=student_feats['cluster'],
    cmap='tab10',
    edgecolor='k',
    alpha=0.7
)
plt.xlabel('Average Food Score')
plt.ylabel('Total Items Ordered')
plt.title('Clusters: Avg Score vs Total Items')
plt.colorbar(label='Cluster')
plt.tight_layout()
plt.show()

student_feats.to_csv("student_health_clusters.csv", index=True)