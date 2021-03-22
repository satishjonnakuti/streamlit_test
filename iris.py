import streamlit as st
import pandas as pd
from PIL import Image,ImageFilter,ImageEnhance
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Title and Subheader
st.title("Iris EDA App")
st.subheader("EDA Web App with Streamlit ")

my_dataset = pd.read_csv('C:\\Users\\satis\\Desktop\\data science\\data science with python\iris.csv')

# st.text_input("user name: ")
# uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','csv'])
# if uploaded_file is not None:
#     file_details = {"FileName":'C:\\Users\\satis\\Desktop\\data science\\data science with python\iris.csv',"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#     st.write(file_details)

#data = my_dataset
data = my_dataset

#Show Dataset
if st.checkbox("Preview DataFrame"):

	if st.button("Head"):
		st.write(data.head())
	if st.button("Tail"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	st.dataframe(data)

# Show Description
if st.checkbox("Show All Column Name"):
	st.text("Columns:")
	st.write(data.columns)

# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
	st.text("Showing Length of Rows")
	st.write(len(data))
if data_dim == 'Columns':
	st.text("Showing Length of Columns")
	st.write(data.shape[1])

#Summary of dataset
if st.checkbox("Show Summary of Dataset"):
	st.write(data.describe())

# Selection
species_option = st.selectbox('Select Columns',('Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Species'))
if species_option == 'Sepal.Length':
	st.write(data['Sepal.Length'])
elif species_option == 'Sepal.Width':
	st.write(data['Sepal.Width'])
elif species_option == 'Petal.Length':
	st.write(data['Petal.Length'])
elif species_option == 'Petal.Width':
	st.write(data['Petal.Width'])
elif species_option == 'Species':
	st.write(data['Species'])
else:
	st.write("Select A Column")

# Show Plots
if st.checkbox("Simple Bar Plot with Matplotlib "):
	data.plot(kind='bar')
	st.pyplot()

#scatter plot
# data.plot(kind='scatter', x='Petal.Width', y='Petal.Length');
# data.plot(kind='scatter', x='Petal.Length', y='Sepal.Length');
# data.plot(kind='scatter', x='Petal.Width', y='Sepal.Length')
# plt.show()

#scatter Plot
# scatter = plt.scatter(data['Sepal.Length'], data['Sepal.Width'], c= "r")
# plt.xlabel('sepl_len(cm)')
# plt.ylabel('sepl_wd(cm)')
# #add legend
# plt.legend(handles = scatter.legend_elements()[0], labels = ["x","y"] )
# plt.show()
#

#scatter plot
with st.echo(code_location='below'):

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(
        data["Sepal.Length"],
        data["Petal.Length"],
    )

    ax.set_xlabel("Sepal.Length")
    ax.set_ylabel("Petal.Length")

    st.write(fig)
