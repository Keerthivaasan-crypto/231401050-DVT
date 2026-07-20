import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("" \
"")

# Read only the first 100 rows
df = df.head(100)

# Display first 5 rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset information
print("\nDataset Information")
print(df.info())

# Shape of dataset
print("\nShape:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include='all'))

# Fill missing values
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna("Unknown", inplace=True)

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# -------------------------------
# Visualizations
# -------------------------------

# Rating Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Rating"], bins=10)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# Top 10 Rated Games
top10 = df.sort_values(by="Rating", ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top10["Title"], top10["Rating"])
plt.xticks(rotation=90)
plt.title("Top 10 Rated Games")
plt.xlabel("Game Title")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

# Plays vs Rating
plt.figure(figsize=(8,5))
plt.scatter(df["Plays"], df["Rating"])
plt.title("Plays vs Rating")
plt.xlabel("Plays")
plt.ylabel("Rating")
plt.show()

# Reviews Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Reviews"], bins=10)
plt.title("Reviews Distribution")
plt.xlabel("Reviews")
plt.ylabel("Frequency")
plt.show()

# Wishlist Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Wishlist"], bins=10)
plt.title("Wishlist Distribution")
plt.xlabel("Wishlist")
plt.ylabel("Frequency")
plt.show()

# Top 10 Most Played Games
print("\nTop 10 Most Played Games")
print(df[["Title", "Plays"]].sort_values(by="Plays", ascending=False).head(10))

# Top 10 Most Wishlisted Games
print("\nTop 10 Most Wishlisted Games")
print(df[["Title", "Wishlist"]].sort_values(by="Wishlist", ascending=False).head(10))

# Correlation Matrix
print("\nCorrelation Matrix")
numeric_df = df.select_dtypes(include=["int64", "float64"])
print(numeric_df.corr())

# Save first 100 cleaned rows
df.to_csv("backloggd_games_first100.csv", index=False)

print("\nAnalysis completed successfully!")