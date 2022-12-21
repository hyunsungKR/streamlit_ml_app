# ML : KMeans , Hierarchical 👀

## 📌 Project Explanation

* python의 Library들을 활용하여 유저 인터랙티브한 웹 대시보드 개발
* csv 파일을 업로드할 수 있는 앱
* 업로드한 csv파일을 df로 읽을 수 있는 앱
* KMeans,Hierarchical 클러스터링을 하기 위해, X로 사용할 컬럼을 설정할 수 있는 앱
* 그룹의 갯수를 정할 수 있는 앱
* 위에서 유저들이 입력한 데이터로 클러스터링하여 결과를 보여준다.
* AWS EC2를 이용하여 서버를 관리하였습니다.
* Github Actions를 이용한 CI/CD를 사용하였습니다.
* 유지보수작업을 수월하게 하기 위해서 다른 파일에서 함수를 만들고 그 함수를 import해서 작업을 하였습니다.
* 각 컬럼 데이터를 가져온 후 문자열인지 아닌지 나눠서 처리를 하도록 반복문과 조건문을 사용했습니다.
* 데이터의 nunique 갯수가 2개 이하이면 레이블인코딩, 그렇지 안흥면 원핫인코딩 하도록  코드를 작성했습니다.
* MinMaxScaler 피쳐스케일링을 사용하여 좀 더 정교한 클러스터링 결과를 가져올 수 있도록 하였습니다.



## 📌hyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## 📌Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

## 📌 Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> 

<img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=SciPy&logoColor=white"/>   

## 📌Tool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> 

## 📌Code block
```python
 # csv파일을 업로드 받고 NaN 삭제 코드 
    file = st.file_uploader('CSV파일 업로드', type=['csv'])
    st.warning('결측치는 자동으로 삭제됩니다.')
    df = pd.read_csv(file)
    df = df.dropna()
```
```python
# 인코딩 작업 for문과 if문

            X_new = pd.DataFrame()

            for name in X.columns :

                # 각 컬럼데이터를 가져온다.
                data=X[name]
                data.reset_index(inplace=True,drop=True)
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
```
```python
# MinMaxScaler를 이용한 피쳐스케일링과정
            scaler = MinMaxScaler()
            X_new = scaler.fit_transform(X_new)
```
## 📌 ML : KMeans
* Using Model : from sklearn.cluster import KMeans
```python
# wcss (Within Clusters Sum of Squares)
            wcss = []
            for k in np.arange(1,max_number+1):
                kmeans=KMeans(n_clusters=k,random_state=5)
                kmeans.fit(X_new)
                wcss.append(kmeans.inertia_)
```
```python
# WCSS값을, 차트로 나타내라. => 엘보우 메소드(Elbow Method)
            max_number=st.number_input('최대 그룹 선택',2,20,value=10)
            x = np.arange(1,max_number+1)
            fig1 = plt.figure()
            plt.plot(x,wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)
```
```python
# KMeans 학습 과정
            k=st.number_input('그룹 갯수 결정',1,max_number)

            kmeans = KMeans(n_clusters=k,random_state=5)
            y_pred = kmeans.fit_predict(X_new)
```
## 📌 ML : Hierarchical
* Using Model : import scipy.cluster.hierarchy as sch / from sklearn.cluster import AgglomerativeClustering
```python
# Dendrogram을 그려 최적의 클러스터 갯수를 찾아보기
            fig2=plt.figure()
            sch.dendrogram(sch.linkage(X_new,method='ward'))
            plt.title('Dendrogram')
            plt.xlabel('Custromers')
            plt.ylabel('Euclidean Distances')
            st.pyplot(fig2)
```
```python
# Hierarchical 학습 과정
            k=st.number_input('그룹 갯수 결정',1,20)

            hc = AgglomerativeClustering(n_clusters= k)
            y_pred = hc.fit_predict(X_new)
            df['Group']=y_pred
```



## 📌 URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8503/

## 📌 Screen Shot
![image](https://user-images.githubusercontent.com/120348500/208033210-03930c10-2009-4498-8750-8a5cde771de3.png)
![image](https://user-images.githubusercontent.com/120348500/208033299-bfa6ce0a-fd6f-4fad-81a6-cec24ae5e96c.png)
![image](https://user-images.githubusercontent.com/120348500/208033408-f3f6f4ed-362a-4a8c-97ec-c2ec04129a0f.png)
![image](https://user-images.githubusercontent.com/120348500/208033502-543c2e74-344d-46cb-b919-e953f8d923c7.png)
![image](https://user-images.githubusercontent.com/120348500/208033576-ea73a230-400e-4694-b152-696bd883f174.png)

## 📌 Reference

메인화면 동영상 : https://youtu.be/PeMlggyqz0Y
