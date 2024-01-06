import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('fruit_sale.csv')

# Plot the growth over time for each fruit with markers
plt.figure(figsize=(10, 6))
for fruit in df['Fruit'].unique():
    fruit_data = df[df['Fruit'] == fruit]
    plt.plot(fruit_data['Date'], fruit_data['Sale'], marker='o', label=fruit)

plt.xlabel('Date')
plt.ylabel('Sale')
plt.title('Sales Over Time for Each Fruit (Line Plot with Markers)')
plt.legend()
plt.show()
