# Importing Required Libraries 
import streamlit as st;
import pandas as pd;
import seaborn as sns;

st.title('Data Analysis');
st.subheader('Data Analysis using Python and Streamlit')

# Upload DataSet 
upload = st.file_uploader("Upload you dataset in (csv format )");

# Let's see if data set is uploaded or not 
if upload is not None :
    data = pd.read_csv(upload);

if upload is not None:
    st.text('Columns in DataSet ');
    st.write(data.columns);

# Show DataSet 
if upload is not None :
    if st.checkbox('Preview DataSet'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail());

# Check the data type of each column
if upload is not None:
    if st.checkbox('Data Types Of Each Column'):
     st.text('Datatypes');
     st.write(data.dtypes);

# Find the sahpe of dataset
if upload is not None :
    data_shape = st.radio("What dimensions do you want t o check",('Rows','Columns'))
    if data_shape =='Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    if data_shape =='Columns':
        st.text('Number of Columns')
        st.write(data.shape[1]);

# Find the null values in the dataset 
# if upload is not None :
#     if st.checkbox("Null Values in data set "):
#         if data.isnull().values.any() == True :
#             st.write("There are : ",data.isnull().sum())
#             sns.heatmap(data.isnull());
#             st.pyplot();
#         else:
#             st.write("There are no null values in your provided dataset")
#             sns.heatmap(data.isnull());
#             st.pyplot();

# In the above code i am not getting my head so writing a new code 
if upload is not None :
    test = data.isnull().values.any();
    if test == True:
        if st.checkbox('Null Values In The DataSet'):
            st.set_option('deprecation.showPyplotGlobalUse', False)
            sns.heatmap(data.isnull());
            st.pyplot()
    else:
            st.success('Congratulations !!!, No Missing Values');

# Find the Duplicate Values in Data Set
if upload is not None :
    test = data.duplicated().values.any()
    if test == True:
        if st.checkbox('Duplicate Values in Dataset'):
            st.warning('This Dataset Contains Some Duplicates Values');
            #st.write('Duplicate Values ',data.duplicates());
            dup = st.selectbox("Do You Want To Remove Duplicate Values ?",("Select One","Yes","No"))
            if dup =="Yes":
                data = data.drop_duplicates()
                st.text("Duplicate Values are Removed");
            if dup =='No':
                st.text('Ok No Problem');
    else:
         st.success('Congratulations !!!, No Missing Duplicate Values');

# Get the Overall info of DataSet
# if upload is not None:
#     st.text('Overall Info Of DataSet ');
#     st.write(data.info());


# Get the Overall Statistics of DataSet
if upload is not None:
    st.text('Overall Statistics Of DataSet ');
    st.write(data.describe());

# About Section Of Our App
if st.button('About App'):
    st.text('Build with Stream lit ')
    st.text('Thanks to Stream lit')

# By 
if st.checkbox('By'):
    st.success('Good Bye');
