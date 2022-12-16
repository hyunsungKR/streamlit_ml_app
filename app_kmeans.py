import streamlit as st
import pandas as pd 
import os 
from datetime import date, datetime
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_kmeans_app():
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyOb8tsP2NjTzqfQ1nfoznhkT5vBxv3n6eXA&usqp=CAU')
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeGZvfeUiM8a32pMsLpeL5t1rqiWYAXH0Hwg&usqp=CAU',width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7uKnApBbyNHtw3Kyt_FKgFyMnkMNRKi_mWQ&usqp=CAU',width=300)


    st.title('K-Means 클러스터링')

    # 1. csv 파일을 업로드할 수 있다.
    file = st.file_uploader('CSV파일 업로드', type=['csv'])
    st.warning('결측치는 자동으로 삭제됩니다.')

    if file is not None :

        df = pd.read_csv(file)
        df = df.dropna()
        st.dataframe( df )
        st.subheader('기본 통계 데이터')
        st.dataframe(df.describe())
        st.subheader('최대 / 최소 데이터 확인하기')
        column_list2 = df.columns[2:]
        selected_column2=st.selectbox('컬럼을 선택하세요.',column_list2)
        df_min=(df.loc[df[selected_column2]==df[selected_column2].min(),])
        df_max=(df.loc[df[selected_column2]==df[selected_column2].max(),])

        st.text('최소값 데이터입니다.')
        st.dataframe(df_min)
        st.text('최대값 데이터입니다.')
        st.dataframe(df_max)

        st.subheader('Kmeans를 이용한 클러스터링')
        st.warning('문자열로 구성된 컬럼은 선택하실 수 없습니다.')
        
        column_list=df.columns
        
        selected_columns=st.multiselect('X로 사용할 컬럼을 선택하세요.(최소 2개 이상)',column_list)
        if len(selected_columns) >= 2 :

            

            
            X = df[selected_columns]

                
            st.dataframe(X)

            st.subheader('WCSS를 위한 클러스터링 갯수를 선택하세요.')

            max_number=st.number_input('최대 그룹 선택',2,20,value=10)

            wcss = []
            for k in np.arange(1,max_number+1):
                kmeans=KMeans(n_clusters=k,random_state=5)
                kmeans.fit(X)
                wcss.append(kmeans.inertia_)


            x = np.arange(1,max_number+1)
            fig1 = plt.figure()
            plt.plot(x,wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)

                # 실제로 그룹핑할 갯수를 선택!
                # k=st.slider('그룹 갯수 결정',1,max_number)
                # slider는 움직일 때마다 계산을 하느라 렉이 걸리기 때문에
                # number_input으로 변경.
            k=st.number_input('그룹 갯수 결정',1,max_number)

            kmeans = KMeans(n_clusters=k,random_state=5)
            y_pred = kmeans.fit_predict(X)
            df['Group']=y_pred

            st.dataframe(df.sort_values('Group'))
            group_list = df['Group'].unique()

            choice_group=st.selectbox('보고싶은 그룹을 선택하세요.',group_list)
            st.dataframe(df.loc[df['Group']==choice_group,])
