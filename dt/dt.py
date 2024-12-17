import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'age2411.csv'
df = pd.read_csv(file_path)

# Step 1: Calculate the percentage of the 16-year-old population for each region
df['16세비율'] = pd.to_numeric(df['2024년11월_계_16세'], errors='coerce') / pd.to_numeric(df['2024년11월_계_총인구수'], errors='coerce') * 100

# Drop rows with missing values
df = df.dropna(subset=['16세비율'])

# Step 2: Identify Daegu regions and calculate the 16-year-old ratio
daegu_regions = df[df['행정구역'].str.contains("대구", na=False)].copy()

# Step 3: Find regions with similar 16-year-old percentage
daegu_mean_ratio = daegu_regions['16세비율'].mean()

# Define a tolerance range for similarity
tolerance = 0.5  # +/- 0.5% of the mean 16-year-old ratio
similar_regions = df[(df['16세비율'] >= daegu_mean_ratio - tolerance) & 
                     (df['16세비율'] <= daegu_mean_ratio + tolerance)]

# Sort for better visualization
similar_regions = similar_regions.sort_values(by='16세비율', ascending=False)

# Step 4: Plot the comparison
plt.figure(figsize=(14, 6))
plt.barh(similar_regions['행정구역'], similar_regions['16세비율'])
plt.xlabel('Percentage of Population Aged 16 (%)')
plt.ylabel('Region')
plt.title(f'Regions with Similar 16-Year-Old Population Percentage (Tolerance ±{tolerance}%)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Step 5: Display regions data
print("Regions with similar 16-year-old population percentages:")
print(similar_regions[['행정구역', '16세비율']])
