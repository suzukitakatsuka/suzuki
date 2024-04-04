import os
from flask import Flask, render_template
import pandas as pd
import socket
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import cv2
import numpy as np
from PIL import Image

app = Flask(__name__, static_folder='./templates/images')
@app.route('/', methods=['GET','POST'])
@app.route('/start', methods=['GET','POST'])

def index():

    text = "こちらFlaskスネーク。応答せよ。"
    while True:
    
        return render_template('index.html', text="こちらFlaskスネーク。応答せよ。")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)
