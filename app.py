
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("tips.csv")

# Streamlit app
st.title("Tips Analysis")

# Display the dataframe
st.write("## Tips Data")
st.write(data)

# Scatter plot
st.write("## Scatter Plot")
plt.scatter(data['day'], data['tip'])
plt.title("Jumlah tip per hari dengan Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
st.pyplot()

# Note: Make sure to have the 'tips.csv' file in the same directory as this script

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("tips.csv")

# Streamlit app
st.title("Tips Analysis")

# Display the dataframe
st.write("## Tips Data")
st.write(data)

# Line plot
st.write("## Line Plot")
plt.plot(data['tip'], label='Tip')
plt.plot(data['size'], label='Size')
plt.title("Line Plot")
plt.xlabel('Day')
plt.ylabel('Value')
plt.legend()
st.pyplot()

# Note: Make sure to have the 'tips.csv' file in the same directory as this script



