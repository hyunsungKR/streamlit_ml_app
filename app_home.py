import streamlit as st
from PIL import Image

def run_home_app():


    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeEy7Kq1TrMtTaMj1TztZWBGj1bCCHfgXMPQ&usqp=CAU',width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqHnNOfcv6wA4GKJSdgC3HobYdNw-tJLcFvQ&usqp=CAU',width=300)
    st.title('ML : KMeans๐ , Hierarchical๐')
    st.info('๋จธ์ ๋ฌ๋์ KMeans์ hierarchical ๊ธฐ๋ฒ์ ์ด์ฉํ์ฌ ์ ์ ์๊ฒ csvํ์ผ์ ์๋ก๋ ๋ฐ์ผ๋ฉด')
    st.info('์ ์ ์ ์๊ตฌ์ฌํญ์ ๋ง๊ฒ ํด๋ฌ์คํฐ๋งํ ๋ฐ์ดํฐ๋ฅผ ๋ณด์ฌ์ค ์ ์๋ ์ฑ์๋๋ค. ')
    st.video('https://youtu.be/PeMlggyqz0Y',start_time=8,format='video/mp4')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvxst9vRLBY3He2qAf_jwPUb4b4c4XiAscSg&usqp=CAU',use_column_width=True)