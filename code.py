# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the visual style for the plots for a professional look
sns.set_theme(style="whitegrid")
plt.style.use('fivethirtyeight')

print("--- Iris Dataset Exploration Notebook ---")
print("Libraries imported successfully!")


# Load and Inspect the Dataset
print("\n--- Step 1: Loading and Inspecting the Iris Dataset ---")

# Seaborn has a built-in function to load the Iris dataset as a pandas DataFrame
iris_df = sns.load_dataset('iris')
print("Iris dataset loaded successfully.")

# Print the shape of the dataset (rows, columns)
print("\nShape of the dataset:", iris_df.shape)

# Print the column names
print("\nColumn names:", iris_df.columns.tolist())

# Print the first few rows of the dataset to get a quick look at the data
print("\nFirst 5 rows of the dataset:")
print(iris_df.head())


# Get Summary Statistics
print("\n--- Step 2: Getting Summary Statistics ---")

# Use .info() to get a concise summary of the DataFrame.
# This is great for checking data types and non-null counts.
print("\n--- Data Summary using .info() ---")
iris_df.info()

# Use .describe() to get descriptive statistics for the numerical columns.
# This includes count, mean, standard deviation, min/max, and quartiles.
print("\n\n--- Descriptive Statistics using .describe() ---")
print(iris_df.describe())


# Visualizing Relationships with Scatter Plots

print("\n--- Step 3: Visualizing the Data ---")
print("\nPart A: Visualizing relationships with a Pair Plot (matrix of scatter plots)")

# A pairplot is fantastic for visualizing pairwise relationships between all numerical features.
# The 'hue' parameter colors the data points by the 'species' column, which is incredibly useful.
sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"], palette='viridis')
plt.suptitle('Pairwise Relationships in the Iris Dataset', y=1.02) # y > 1 to position title above plot
plt.show()

print("\nObservation: The pairplot clearly shows that the 'setosa' species is linearly separable from the other two,")
print("especially when looking at petal length vs. petal width.")


# Visualizing Distributions with Histograms
print("\nPart B: Visualizing value distributions with Histograms")

# We can create histograms for each feature to see their distributions.
# Let's use subplots to display them all in one figure.
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution of Iris Features', fontsize=16)

# Sepal Length
sns.histplot(ax=axes[0, 0], data=iris_df, x='sepal_length', kde=True, hue='species')
axes[0, 0].set_title('Sepal Length Distribution')

# Sepal Width
sns.histplot(ax=axes[0, 1], data=iris_df, x='sepal_width', kde=True, hue='species')
axes[0, 1].set_title('Sepal Width Distribution')

# Petal Length
sns.histplot(ax=axes[1, 0], data=iris_df, x='petal_length', kde=True, hue='species')
axes[1, 0].set_title('Petal Length Distribution')

# Petal Width
sns.histplot(ax=axes[1, 1], data=iris_df, x='petal_width', kde=True, hue='species')
axes[1, 1].set_title('Petal Width Distribution')

plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust layout to make room for suptitle
plt.show()


# Identifying Outliers with Box Plots
print("\nPart C: Identifying outliers with Box Plots")

# Box plots are excellent for identifying outliers.
# Any data point that falls outside the 'whiskers' of the plot is considered a potential outlier.
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Box Plots of Iris Features by Species', fontsize=16)

# Sepal Length
sns.boxplot(ax=axes[0, 0], data=iris_df, x='species', y='sepal_length')
axes[0, 0].set_title('Sepal Length')

# Sepal Width
sns.boxplot(ax=axes[0, 1], data=iris_df, x='species', y='sepal_width')
axes[0, 1].set_title('Sepal Width')

# Petal Length
sns.boxplot(ax=axes[1, 0], data=iris_df, x='species', y='petal_length')
axes[1, 0].set_title('Petal Length')

# Petal Width
sns.boxplot(ax=axes[1, 1], data=iris_df, x='species', y='petal_width')
axes[1, 1].set_title('Petal Width')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

print("\nObservation: The box plot for 'sepal_width' shows a few data points (dots) outside the main range,")
print("suggesting they might be outliers for their respective species.")
print("\n--- End of Exploration ---")
