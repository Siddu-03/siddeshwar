﻿#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("Siddeshwarprasad K R")
usn = st.sidebar.text_input("46")
instructor_name = st.sidebar.text_input("Ashwini")


# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: teal;'>Created by:</h5>"
        f"<p style='color: white;'>{name} (USN: {usn})</p>"
        f"<p style='color: white;'>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )


# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit
fig6 = px.histogram(
tips, x='tip', color='sex',
title='Distribution of Tips (Colored by Gender)',
labels={'tip': 'Tip ($)', 'sex': 'Gender'},
template='plotly_white', # Clean and bright look
)
fig6.show()
st.plotly_chart(fig6) #display chart in streamlit 

#4. Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
fig4 = px.scatter(
tips, x='total_bill', y='tip', color='sex',
title='Total Bill vs Tip (Colored by Gender)',
labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
template='plotly_dark', # Using a cool dark theme
size='size' # The size of points based on the size of the group
)
fig4.show()
st.plotly_chart(fig4)

#5. Box Plot: Distribution of Total Bill by Day (With Color by Time)
fig5 = px.box(
tips, x='day', y='total_bill', color='time',
title='Total Bill Distribution by Day and Time',
labels={'total_bill': 'Total Bill ($)', 'day': 'Day'},
template='ggplot2', # Classic theme for a beautiful look
)
fig5.show()
st.plotly_chart(fig5)
