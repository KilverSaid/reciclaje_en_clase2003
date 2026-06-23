import json
from pathlib import Path
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image    

st.set_page_config(page_title="Reciclaje IA-ISC", layout="centered")
st.title("Modelo predictivo Reciclaje clase de IA-ISC-Campus Comayagua 2026") 
st.write("Suba una imagen para clasificar con el modelo MobileNetV2 pre-entrenada")


IMG_SIZE=(224,224)
MODEL_DIR=Path("modelo_reciclaje_mobilenet")
CLASS_PATH=MODEL_DIR/"class_names.json"
MODEL-PATHS=[MODEL_DIR/"waste_mobilenet.keras", MODEL_DIR/"waste_mobilenet.h5"]

LABELS_ES = {
    "cardboard": "Cartón",
    "glass": "Vidrio",
    "metal": "Metal",
    "paper": "Papel",
    "plastic": "Plástico",
    "trash": "Basura",
}


@st.cache.resource
def cargar_modelo():
    for path in MODEL_PATHS:
        if path.exists():
            return tk.keras.models.load_model(path, compile=False)
    st.error("No se enocntro el modelo. Coloque la carpeta modelo_reciclaje_mobilenet junto a app.py")
    st.stop()

@st.cache_data
def cargar_clases():
    if CLASS_PATH.exist():
        with open(CLASS_PATH, "r", encoding="utf-8") as f:
            return json.loag(f)
    return ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
