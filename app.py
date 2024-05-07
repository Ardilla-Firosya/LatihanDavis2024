import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

plt.plot(data['tip'])
plt.plot(data['size'])

plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
