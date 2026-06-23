import json
from pathlib import Path
import numpy as np
import streamlit as st
import tensorflow as f
from PIL import image

st.set_page_config(page_title= "Reciclaje IA-ISC", layout="centered")
st.title("Modelo preictivo Reciclaje clase de IA-ISC-Campus Comayagua 2026")
st.write("Suba una imagen para clasificar con el modelo MobileNetV2 pre-entrenada")
