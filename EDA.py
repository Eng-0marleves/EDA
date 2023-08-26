import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('listings.csv')  # Replace with your dataset file path

# Display basic information about the dataset
print(data.head())
print(data.info())
print(data.describe())

# Plotting

numeric_columns = data.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_columns.corr()

# Plotting the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# Histogram of review scores
plt.figure(figsize=(10, 6))
sns.histplot(data['review_scores_rating'], bins=20, kde=True)
plt.title('Distribution of Review Scores')
plt.xlabel('Review Scores')
plt.ylabel('Frequency')
plt.show()

data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)

# Box plot of price
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['room_type'], y=data['price'])
plt.title('Price Variation by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()

# Scatter plot of price vs. number of reviews
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['number_of_reviews'], y=data['price'], alpha=0.5)
plt.title('Price vs. Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Price')
plt.show()

# Correlation heatmap
correlation_matrix = numeric_columns.corr()  # Use the numeric columns only
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
