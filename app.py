# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# st.set_option('deprecation.showPyplotGlobalUse', False)
# data = pd.read_csv("tips.csv")

# st.subheader("Visualisasi Dashboard")

# # Bar chart with day against tip
# plt.bar(data['day'], data['tip'])

# # plt.title("Bar Chart")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# # Show plot
# st.pyplot()


# plt.scatter(data['day'], data['tip'], c=data['size'],
#             s=data['total_bill'])
            
# plt.plot(data['tip'])
# plt.plot(data['size'])

# plt.title("Scatter Plot")
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

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

# Bar chart
st.write("## Bar Chart")
plt.bar(data['day'], data['tip'])
plt.title("Bar Chart")
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

# Scatter plot
st.write("## Scatter Plot")
plt.scatter(data['day'], data['tip'])
plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
st.pyplot()

# Note: Make sure to have the 'tips.csv' file in the same directory as this script


