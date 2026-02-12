import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Student Performance Analysis Dashboard")
st.write("An interactive dashboard to analyze factors affecting student academic performance.")

@st.cache_data
def load_data():
    data = pd.read_csv("data/student-mat.csv", sep=";")
    data["final_percentage"] = (data["G3"] / 20) * 100
    return data

mat = load_data()


st.subheader("Dataset Preview")
st.dataframe(mat.head())


st.subheader("Performance Distribution")

plt.figure(figsize=(8,5))
sns.histplot(mat["final_percentage"], bins=20)
plt.xlabel("Final Percentage")
plt.ylabel("Number of Students")
st.pyplot(plt)


st.subheader("Study Time vs Performance")

plt.figure(figsize=(8,5))
sns.boxplot(x="studytime", y="final_percentage", data=mat)
st.pyplot(plt)


st.subheader("Absences vs Performance")

plt.figure(figsize=(8,5))
sns.scatterplot(x="absences", y="final_percentage", data=mat)
st.pyplot(plt)
