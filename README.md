# ML : KMeans , Hierarchical ๐

## ๐ Project Explanation

* python์ Library๋ค์ ํ์ฉํ์ฌ ์ ์  ์ธํฐ๋ํฐ๋ธํ ์น ๋์๋ณด๋ ๊ฐ๋ฐ
* csv ํ์ผ์ ์๋ก๋ํ  ์ ์๋ ์ฑ
* ์๋ก๋ํ csvํ์ผ์ df๋ก ์ฝ์ ์ ์๋ ์ฑ
* KMeans,Hierarchical ํด๋ฌ์คํฐ๋ง์ ํ๊ธฐ ์ํด, X๋ก ์ฌ์ฉํ  ์ปฌ๋ผ์ ์ค์ ํ  ์ ์๋ ์ฑ
* ๊ทธ๋ฃน์ ๊ฐฏ์๋ฅผ ์ ํ  ์ ์๋ ์ฑ
* ์์์ ์ ์ ๋ค์ด ์๋ ฅํ ๋ฐ์ดํฐ๋ก ํด๋ฌ์คํฐ๋งํ์ฌ ๊ฒฐ๊ณผ๋ฅผ ๋ณด์ฌ์ค๋ค.
* AWS EC2๋ฅผ ์ด์ฉํ์ฌ ์๋ฒ๋ฅผ ๊ด๋ฆฌํ์์ต๋๋ค.
* Github Actions๋ฅผ ์ด์ฉํ CI/CD๋ฅผ ์ฌ์ฉํ์์ต๋๋ค.
* ์ ์ง๋ณด์์์์ ์์ํ๊ฒ ํ๊ธฐ ์ํด์ ๋ค๋ฅธ ํ์ผ์์ ํจ์๋ฅผ ๋ง๋ค๊ณ  ๊ทธ ํจ์๋ฅผ importํด์ ์์์ ํ์์ต๋๋ค.
* ๊ฐ ์ปฌ๋ผ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์จ ํ ๋ฌธ์์ด์ธ์ง ์๋์ง ๋๋ ์ ์ฒ๋ฆฌ๋ฅผ ํ๋๋ก ๋ฐ๋ณต๋ฌธ๊ณผ ์กฐ๊ฑด๋ฌธ์ ์ฌ์ฉํ์ต๋๋ค.
* ๋ฐ์ดํฐ์ nunique ๊ฐฏ์๊ฐ 2๊ฐ ์ดํ์ด๋ฉด ๋ ์ด๋ธ์ธ์ฝ๋ฉ, ๊ทธ๋ ์ง ์ํฅ๋ฉด ์ํซ์ธ์ฝ๋ฉ ํ๋๋ก  ์ฝ๋๋ฅผ ์์ฑํ์ต๋๋ค.
* MinMaxScaler ํผ์ณ์ค์ผ์ผ๋ง์ ์ฌ์ฉํ์ฌ ์ข ๋ ์ ๊ตํ ํด๋ฌ์คํฐ๋ง ๊ฒฐ๊ณผ๋ฅผ ๊ฐ์ ธ์ฌ ์ ์๋๋ก ํ์์ต๋๋ค.



## ๐hyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## ๐Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

## ๐ Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> 

<img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=SciPy&logoColor=white"/>   

## ๐Tool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> 

## ๐Code block
```python
 # csvํ์ผ์ ์๋ก๋ ๋ฐ๊ณ  NaN ์ญ์  ์ฝ๋ 
    file = st.file_uploader('CSVํ์ผ ์๋ก๋', type=['csv'])
    st.warning('๊ฒฐ์ธก์น๋ ์๋์ผ๋ก ์ญ์ ๋ฉ๋๋ค.')
    df = pd.read_csv(file)
    df = df.dropna()
```
```python
# ์ธ์ฝ๋ฉ ์์ for๋ฌธ๊ณผ if๋ฌธ

            X_new = pd.DataFrame()

            for name in X.columns :

                # ๊ฐ ์ปฌ๋ผ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์จ๋ค.
                data=X[name]
                data.reset_index(inplace=True,drop=True)
                # ๋ฌธ์์ด์ธ์ง ์๋์ง ๋๋ ์ ์ฒ๋ฆฌํ๋ฉด ๋๋ค.
                if data.dtype == object :
                    
                    # ๋ฌธ์์ด์ด๋, ๊ฐฏ์๊ฐ 2๊ฐ์ธ์ง ์๋์ง ํ์ํด์
                    # 2๊ฐ์ด๋ฉด ๋ ์ด๋ธ ์ธ์ฝ๋ฉ, ๊ทธ๋ ์ง ์์ผ๋ฉด
                    # ์ํซ ์ธ์ฝ๋ฉ ํ๋๋ก ์ฝ๋ ์์ฑ
                    if data.nunique() <= 2 :
                        #๋ ์ด๋ธ ์ธ์ฝ๋ฉ
                        label_encoder = LabelEncoder()
                        X_new[name]=label_encoder.fit_transform(data)
                    else :
                        # ์ํซ ์ธ์ฝ๋ฉ
                        ct = ColumnTransformer ( [('encoder',OneHotEncoder(),[0])],
                                remainder='passthrough')
                        col_names=sorted(data.unique())
                        X_new[col_names]=ct.fit_transform(data.to_frame())
                else :
                    # ์ซ์ ๋ฐ์ดํฐ ์ฒ๋ฆฌ
                    
                    X_new[name] = data
```
```python
# MinMaxScaler๋ฅผ ์ด์ฉํ ํผ์ณ์ค์ผ์ผ๋ง๊ณผ์ 
            scaler = MinMaxScaler()
            X_new = scaler.fit_transform(X_new)
```
## ๐ ML : KMeans
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
# WCSS๊ฐ์, ์ฐจํธ๋ก ๋ํ๋ด๋ผ. => ์๋ณด์ฐ ๋ฉ์๋(Elbow Method)
            max_number=st.number_input('์ต๋ ๊ทธ๋ฃน ์ ํ',2,20,value=10)
            x = np.arange(1,max_number+1)
            fig1 = plt.figure()
            plt.plot(x,wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)
```
```python
# KMeans ํ์ต ๊ณผ์ 
            k=st.number_input('๊ทธ๋ฃน ๊ฐฏ์ ๊ฒฐ์ ',1,max_number)

            kmeans = KMeans(n_clusters=k,random_state=5)
            y_pred = kmeans.fit_predict(X_new)
```
## ๐ ML : Hierarchical
* Using Model : import scipy.cluster.hierarchy as sch / from sklearn.cluster import AgglomerativeClustering
```python
# Dendrogram์ ๊ทธ๋ ค ์ต์ ์ ํด๋ฌ์คํฐ ๊ฐฏ์๋ฅผ ์ฐพ์๋ณด๊ธฐ
            fig2=plt.figure()
            sch.dendrogram(sch.linkage(X_new,method='ward'))
            plt.title('Dendrogram')
            plt.xlabel('Custromers')
            plt.ylabel('Euclidean Distances')
            st.pyplot(fig2)
```
```python
# Hierarchical ํ์ต ๊ณผ์ 
            k=st.number_input('๊ทธ๋ฃน ๊ฐฏ์ ๊ฒฐ์ ',1,20)

            hc = AgglomerativeClustering(n_clusters= k)
            y_pred = hc.fit_predict(X_new)
            df['Group']=y_pred
```



## ๐ URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8503/

## ๐ Screen Shot
![image](https://user-images.githubusercontent.com/120348500/208033210-03930c10-2009-4498-8750-8a5cde771de3.png)
![image](https://user-images.githubusercontent.com/120348500/208033299-bfa6ce0a-fd6f-4fad-81a6-cec24ae5e96c.png)
![image](https://user-images.githubusercontent.com/120348500/208033408-f3f6f4ed-362a-4a8c-97ec-c2ec04129a0f.png)
![image](https://user-images.githubusercontent.com/120348500/208033502-543c2e74-344d-46cb-b919-e953f8d923c7.png)
![image](https://user-images.githubusercontent.com/120348500/208033576-ea73a230-400e-4694-b152-696bd883f174.png)

## ๐ Reference

๋ฉ์ธํ๋ฉด ๋์์ : https://youtu.be/PeMlggyqz0Y
