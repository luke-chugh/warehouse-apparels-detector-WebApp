import streamlit as st
from PIL import Image
import os
import time
import shutil
import subprocess

if os.path.exists('Input\\') == False:
  os.mkdir("Input")
if os.path.exists('Output\\') == False:
  os.mkdir("Output")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def save_uploaded_file(uploadedfile):
  with open(os.path.join("Input",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
  return None

def predict(filename):
  script = "python luke.py --source " + "Input\\" + str(filename) + " --weights best.pt --conf 0.4"
  subprocess.call(script,shell =True)

st.write("""
    ### Warehouse Apparels Detector by **LUKE CHUGH** 
    **This WebApp can detect hats, vests, goggles, gloves and shoes**

    **Upload any image of warehouse operative from google and wait for 10 seconds**
    ***
    """)

uploaded_image = st.sidebar.file_uploader("Choose a JPG, JPEG or PNG file", type=["jpg","png","jpeg","webp"])

if uploaded_image is not None:
    st.sidebar.info('Uploaded image:')
    st.sidebar.image(uploaded_image, width=284)
    save_uploaded_file(uploaded_image)
    filename = "input_image.jpg"
    os.rename(os.path.join("Input",uploaded_image.name),os.path.join("Input",filename))
    with st.spinner('Loading Detections...'):
      predict(filename)
    image= Image.open('Output\\'+ filename)
    st.write("**Detected Warehouse Apparels:**")
    st.image(image,use_column_width=True)


if os.path.exists('Input\\') == True:
  shutil.rmtree('Input')
if os.path.exists('Output\\') == True:
  shutil.rmtree('Output')
