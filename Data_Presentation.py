import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
# Load the dataset
data = [12, 15, 18, 20, 22, 25, 30]

plt.hist(data, bins=7, color='blue', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
plt.pie(data, autopct='%1.1f%%', colors=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
plt.title('Pie Chart of Data')
plt.show()

data = np.sort(data)
cf = np.arange(1, len(data)+1)
plt.plot(data, cf)
plt.title('Cumulative Frequency Plot')
plt.xlabel('Value')
plt.ylabel('Cumulative Frequency')
plt.show()


