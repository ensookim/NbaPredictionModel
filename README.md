
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&text=NbaPredictionModel&animation=fadeIn&fontColor=ffffff&fontSize=60" />

<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=flat-square&logo=python&logoColor=white"></div>

# NBA Prediction Model
## Project Overview


#### 평소 좋아하던 분야를 접목하여 도전해보는 것은 매우 가치있고 재미있는 일이라고 생각합니다.

- 저는 NBA에 많은 관심을 가지고 있었고, 최근에는 Node.js를 이용한 웹 프로젝트를 진행하면서 기술과 NBA의 접목에 더욱 흥미를 느꼈습니다.

- 딥러닝 수업을 통해 기술과 스포츠 통계를 결합할 수 있다는 흥미로운 생각에 이 프로젝트를 시작하려합니다.

- 이 프로젝트는 NBA 선수들의 통계 데이터를 기반으로 머신러닝 모델을 활용하여 선수들의 포인트(PTS)를 예측하는 것이 목표입니다. 

- 최종적인 목표는 이 프로젝트를 성공적으로 완료하고 머신러닝 모델을 활용하여 웹 어플리케이션에 'PTS 예측' 기능을 포함하는 것입니다.

- 완벽하지도, 정확하지도 않습니다. 하지만 흥미에서 오는 궁금증은 어떤 공부법보다 효과적일 것 입니다.


---



### Let's GO


## Data Collection

- NBA 선수 통계 데이터는 urllib과 BeautifulSoup 라이브러리를 활용하여 [ NBA 통계 웹사이트](https://www.basketball-reference.com/)에서 추출하였습니다. 추출된 데이터는 CSV 파일로 저장되어 추가적인 분석, 예측에 활용합니다.

## Machine Learning Model Creation

- TensorFlow.Keras를 사용하여 머신러닝 모델을 생성합니다. 수집된 데이터는 sklearn을 사용해 정규화되고, 전처리한 데이터들로 신경망 모델이 구축되고 학습됩니다. (optimizer='adam', loss='mse') 을 사용하여 학습합니다.


## Model Saving and Prediction

- HITMAP을 그려보니 2P%, 3P%, FG% 같은 슈팅 성공률과 PTS(득점) 간의 상관관계가 낮게 나왔습니다.

- 이유는, 득점 자체와의 직접적인 관련성보다는 슛 시도 횟수(FGA, 3PA, 2PA)가 더 큰 영향을 미치기 때문입니다. 즉, 득점은 주로 시도한 슛의 횟수와 강하게 연관되어 있으며, 슛 성공률은 특정 선수가 적은 슛 시도에서 높은 성공률을 기록했어도 전체 득점에는 큰 영향을 주지 않을 수 있습니다.
(실제로)

- 해당 모델은 위와 같은 이유로 정확하지 않습니다. 경기 수, 슛 시도, 득점성공률 등 해당 스텟들과의 상관관계를 모두 파악하여 모델을 설계한다면 더욱 정확한 모델을 생성할 수 있을 것 입니다.



<h2 style="border-bottom: 1px solid #21262d; color: #c9d1d9;"> Thank you😊 </h2>



[![Velog's GitHub stats](https://velog-readme-stats.vercel.app/api?name=nostudynofood)](https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1)

 <div align= "center"> <a href=https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1> <img src="https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=Velog&logoColor=white&link=https://velog.io/@nostudynofood/NBAStats-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%B6%94%EC%B6%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%98%88%EC%B8%A1%EA%B9%8C%EC%A7%80-1"> </a>
          </div>


