import streamlit as st
from PIL import Image

def run_home_app():


    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeEy7Kq1TrMtTaMj1TztZWBGj1bCCHfgXMPQ&usqp=CAU',width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqHnNOfcv6wA4GKJSdgC3HobYdNw-tJLcFvQ&usqp=CAU',width=300)
    st.title('ML : KMeans👀 , Hierarchical👀')
    st.info('머신러닝의 KMeans와 hierarchical 기법을 이용하여 유저에게 csv파일을 업로드 받으면')
    st.info('유저의 요구사항에 맞게 클러스터링한 데이터를 보여줄 수 있는 앱입니다. ')
    st.video('https://youtu.be/PeMlggyqz0Y',start_time=8,format='video/mp4')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvxst9vRLBY3He2qAf_jwPUb4b4c4XiAscSg&usqp=CAU',use_column_width=True)