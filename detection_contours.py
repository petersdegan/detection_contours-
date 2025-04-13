import streamlit as st 
import cv2
import numpy as np
from PIL import Image


fichier_telecharger=st.file_uploader("Entrez une image ou nous allons identifier les contours",type=["jpg","jpeg","png"])


if fichier_telecharger is not None:
    image=Image.open(fichier_telecharger)
    fab=np.array(image)
    
    
    image_gris=cv2.cvtColor(fab,cv2.COLOR_BGR2GRAY)
    
    contours=cv2.Canny(image_gris,threshold1=80,threshold2=175)
    st.image(image,caption="Image originale")
    st.image(contours,caption="Image avec ses contours ")
