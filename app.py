import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
from keras.models import load_model
import shutil

st. set_page_config(layout="wide")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

model = load_model('resnet50.h5')
feature_list = np.array(pickle.load(open('embeddings.pkl','rb')))
filenames = pickle.load(open('filenames.pkl','rb'))

st.markdown("<h1 style='text-align: center; color: blue;'>FURNITURE RECOMMENDATION SYSTEM BY LUKE CHUGH</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>Note: This WebApp can only recommend chairs, couches/sofa, beds, and tables</h5>", unsafe_allow_html=True)
#st.write('##### **Note:** This WebApp can only recommend chairs, couches/sofa, beds, and tables.')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0

def feature_extraction(img_path,model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)
    return normalized_result

def recommend(features,feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([features])
    return indices

uploaded_file = st.file_uploader("Upload an image and wait for a few seconds.",type=["jpg","png","jpeg","webp"])
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        resized_image = display_image.resize((400,400))
        st.write('#### **Uploaded Image:**')
        st.image(resized_image)
        st.write('#### **Recommendations:**')
        with st.spinner('Preparing Recommendations..'):
            # feature extract
            features = feature_extraction(os.path.join("uploads",uploaded_file.name),model)
            # recommendention
            indices = recommend(features,feature_list)
            # Show Recommendations
            col1,col2,col3,col4,col5 = st.columns(5)
        
            with col1:
                st.image(Image.open(filenames[indices[0][0]]).resize((300,300)))
            with col2:
                st.image(Image.open(filenames[indices[0][1]]).resize((300,300)))
            with col3:
                st.image(Image.open(filenames[indices[0][2]]).resize((300,300)))
            with col4:
                st.image(Image.open(filenames[indices[0][3]]).resize((300,300)))
            with col5:
                st.image(Image.open(filenames[indices[0][4]]).resize((300,300)))
    else:
        st.header("Some error occured in file upload")


