# elbow_plot.py
# Run this to generate elbow_plot.png for k=3 justification

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# === CONFIG: Change this path to your CSV ===
CSV_PATH = "normalized/spike_days.csv"  # or your actual file

# Load data
if not os.path.exists(CSV_PATH):
    print(f"Error: {CSV_PATH} not found!")
    print("Download it from the repo first.")
    exit()

data = pd.read_csv(CSV_PATH)
print(f"Loaded {len(data)} rows from {CSV_PATH}")

# Prepare features
X = data[['month', 'day_of_year']].values

# Calculate inertia
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Plot
plt.figure(figsize=(7, 5))
plt.plot(range(1, 11), inertias, 'bo-', markersize=8)
plt.title('Elbow Method for Optimal k', fontsize=14, fontweight='bold')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.axvline(3, color='red', linestyle='--', linewidth=2, label='k=3 (chosen)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save
output_path = "elbow_plot.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"Saved: {output_path}")
