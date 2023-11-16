
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&text=NbaPredictionModel&animation=fadeIn&fontColor=ffffff&fontSize=60" />

<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=flat-square&logo=python&logoColor=white"></div>

# NBA Prediction Model
## Project Overview

- 저는 NBA에 큰 관심을 가지고 있었고, 최근에는 Node.js를 이용한 웹 프로젝트를 진행하면서 기술과 NBA의 접목에 더욱 흥미를 느꼈습니다.

- 딥러닝 수업을 통해 기술과 스포츠 통계를 결합할 수 있는 흥미로운 아이디어가 떠올라 이 프로젝트를 진행합니다.

- 이 프로젝트는 NBA 선수들의 통계 데이터를 기반으로 머신러닝 모델을 활용하여 선수들의 포인트(PTS)를 예측하는 것이 목표입니다. 

- 이 프로젝트를 통해 딥러닝 수업에서 얻은 지식을 바탕으로 나만의 프로젝트를 수행하고자 합니다.

- 이 분야에 초보인 저는 과정에서 얻게 될 지식을 적용하여 나만의 프로젝트를 진행하려는 목표를 가지고 있습니다. 최종적인 목표는 이 프로젝트를 성공적으로 완료하고 머신러닝 모델을 활용하여 웹 어플리케이션에 'PTS 예측' 기능을 포함하는 것입니다.

#### 농구에 대한 관심과 머신러닝이 결합된 독특한 경험을 팬층에게 제공하는 기회로 이어질 것입니다.

## Data Collection

- NBA 선수 통계 데이터는 urllib과 BeautifulSoup 라이브러리를 활용하여 [ NBA 통계 웹사이트](https://www.basketball-reference.com/)에서 추출됩니다. 추출된 데이터는 CSV 파일로 저장되어 추가적인 분석에 활용됩니다.

## Machine Learning Model Creation

- TensorFlow.Keras를 사용하여 머신러닝 모델을 생성합니다. 수집된 데이터는 sklearn을 사용해 정규화되고, 전처리한 데이터들로 신경망 모델이 구축되고 학습됩니다. (optimizer='adam', loss='mse') 을 사용하여 컴파일합니다.


## Model Saving and Prediction

- 학습된 모델은 저장되어 나중에 사용될 수 있으며, 새로운 데이터를 입력하여 예측을 수행할 수 있습니다.
- 이 프로잭트를 통해서 데이터 추출, 데이터 전처리, 모델 생성의 방법을 학습하고 스포츠와 기술의 결합에 더욱 흥미를 느끼게 됐습니다.


## How to use🐬


- nbaCawking.py 를 실행하여 데이터를 크롤링하여 CSV파일로 저장합니다.

- nbaModel.py 를 실행하여 CSV파일을 불러오고 데이터를 가공합니다. 가공된 데이터로 모델을 생성하고 예측을 수행합니다.



<h2 style="border-bottom: 1px solid #21262d; color: #c9d1d9;"> Thank you😊 </h2>



[![Velog's GitHub stats](https://velog-readme-stats.vercel.app/api?name=nostudynofood)](https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1)

 <div align= "center"> <a href=https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1> <img src="https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=Velog&logoColor=white&link=https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1"> </a>
          </div>


