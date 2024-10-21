import streamlit as st
import pickle
import numpy as np
import math

# Importing the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

## Tittle
st.title("Laptop Predictor")

## Brand
company = st.selectbox('Brand', df['Company'].unique())

## Type of laptop
type = st.selectbox('Type of Laptop', df['TypeName'].unique())

## Ram
ram = st.selectbox('RAM(GB)', [2, 4, 8, 12, 16, 24, 32, 64])

## Weight
weight = st.number_input("Weight")

## Touchscreen
touchscreen = st.selectbox('Touchscreen', ["YES", "NO"])

## IPS Pannel

ips = st.selectbox('IPS Pannel', ["YES", "NO"])

## Screen Size
screen_size = st.number_input("Screen Size")

## Resolution
resolution = st.selectbox('Screen Resolution',
                          ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                           '2560x1440', '2304x1440'])

## CPU
cpu = st.selectbox("CPU", df['Cpu brand'].unique())

## HDD
hdd = st.selectbox("HDD(in GB)", [0, 32, 128, 256, 512, 1024, 2048])

## SSD

ssd = st.selectbox("SSD(in GB)", [0, 32, 128, 256, 512, 1024, 2048])

## GPU Name
gpu = st.selectbox("Graphic Card", df["Gpu brand"].unique())

## Operating System
os = st.selectbox('Operating System', df['os'].unique())

if st.button("Predict Price"):
    try:
        if touchscreen == "YES":
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == "YES":
            ips = 1
        else:
            ips = 0

        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])

        ppi = (((x_res**2) + (y_res**2))**0.5)/screen_size

        query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, ssd, hdd, gpu, os])
        query = query.reshape(1,12)
        st.title("The Price of the Laptop the given configuration is "+ str(round(np.exp(pipe.predict(query)[0]))))
    except :
        st.title("Please Provide correct details.")

