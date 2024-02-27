import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('path_to_your_dataset.csv')

# Basic Analysis
print(data.describe())  # Descriptive statistics

# Visualization
data['column_of_interest'].plot(kind='bar')  # Replace 'column_of_interest'
plt.show()