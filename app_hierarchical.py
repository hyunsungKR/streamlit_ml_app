import streamlit as st
import pandas as pd 
import os 
from datetime import date, datetime
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler



def run_hierarchical_app():
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyOb8tsP2NjTzqfQ1nfoznhkT5vBxv3n6eXA&usqp=CAU')
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeGZvfeUiM8a32pMsLpeL5t1rqiWYAXH0Hwg&usqp=CAU',width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTa9LJxXS1Zp7Rf0gysLSwoEtROBqitf0oFFQ&usqp=CAU',width=300)


    st.title('Hierarchical 클러스터링')

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

        st.subheader('Hierarchical를 이용한 클러스터링')
        st.info('문자열로 구성된 컬럼은 2개 이하이면 레이블인코딩')
        st.info('그렇지 않으면 원핫 인코딩 작업 후 숫자로 변환됩니다.')
        
        column_list=df.columns
        
        selected_columns=st.multiselect('X로 사용할 컬럼을 선택하세요.(최소 2개 이상)',column_list)
        if len(selected_columns) >= 2 :

            X = df[selected_columns]

            # 문자열이 들어있으면 처리한 후에 화면에 보여준다.
            X_new = pd.DataFrame()

            for name in X.columns :

                # 각 컬럼데이터를 가져온다.
                data=X[name]
                # 문자열인지 아닌지 나눠서 처리하면 된다.
                if data.dtype == object :
                    
                    # 문자열이니, 갯수가 2개인지 아닌지 파악해서
                    # 2개이면 레이블 인코딩, 그렇지 않으면
                    # 원핫 인코딩 하도록 코드 작성
                    if data.nunique() <= 2 :
                        #레이블 인코딩
                        label_encoder = LabelEncoder()
                        X_new[name]=label_encoder.fit_transform(data)
                    else :
                        # 원핫 인코딩
                        ct = ColumnTransformer ( [('encoder',OneHotEncoder(),[0])],
                                remainder='passthrough')
                        col_names=sorted(data.unique())
                        X_new[col_names]=ct.fit_transform(data.to_frame())
                else :
                    # 숫자 데이터 처리
                    
                    X_new[name] = data
            scaler = MinMaxScaler()
            X_new = scaler.fit_transform(X_new)

            fig2=plt.figure()
            sch.dendrogram(sch.linkage(X_new,method='ward'))
            plt.title('Dendrogram')
            plt.xlabel('Custromers')
            plt.ylabel('Euclidean Distances')
            st.pyplot(fig2)
                
            st.dataframe(X_new)

            st.subheader('Dendogram을 보고 클러스터링 갯수를 선택하세요.')


            k=st.number_input('그룹 갯수 결정',1,20)

            hc = AgglomerativeClustering(n_clusters= k)
            y_pred = hc.fit_predict(X_new)
            df['Group']=y_pred

            st.dataframe(df.sort_values('Group'))
            group_list = df['Group'].unique()

            choice_group=st.selectbox('보고싶은 그룹을 선택하세요.',group_list)
            st.dataframe(df.loc[df['Group']==choice_group,])