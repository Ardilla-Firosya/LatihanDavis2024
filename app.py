import streamlit as st
import pandas as pd
import seaborn as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv("tips.csv")

st.subheader("Visualisasi Dashboard")

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])

# plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Show plot
st.pyplot()


plt.scatter(data['day'], data['tip'], c=data['size'],
            s=data['total_bill'])
            
plt.plot(data['tip'])
plt.plot(data['size'])

plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
