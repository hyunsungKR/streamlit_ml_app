import streamlit as st
import pandas as pd 
import os 
from datetime import date, datetime
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from app_home import run_home_app
from app_kmeans import run_kmeans_app
from app_hierarchical import run_hierarchical_app

def main() :
    menu = ['Home','Kmeans','Hierarchical ']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'Kmeans' :
        run_kmeans_app()
    elif choice == 'Hierarchical ':
        run_hierarchical_app()


        



if __name__ == '__main__' :
    main()