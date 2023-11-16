import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# NBA 선수들의 통계 데이터 불러오기
all_stats = pd.read_csv('nba_stats_2010_to_2023.csv')

# 필요없는 열 삭제
all_stats.drop('FG%', axis=1, inplace=True)
all_stats.drop('Pos', axis=1, inplace=True)
all_stats.drop('Tm', axis=1, inplace=True)
all_stats.drop(['G', 'GS'], axis=1, inplace=True)
all_stats.drop('Age', axis=1, inplace=True)
all_stats.drop('BLK', axis=1, inplace=True)
all_stats.drop('ORB', axis=1, inplace=True)

# 결측치 0으로 채우기
all_stats.fillna(0, inplace=True)

# 예측에 사용할 특성 선택
features = ['MP', 'FG', 'FGA', '3P', 'FT%', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PF']

# # 상관 행렬 계산
# correlation_matrix = all_stats[features].corr()

# # 상관관계 히트맵 시각화
# plt.figure(figsize=(12, 6))
# sns.heatmap(correlation_matrix[['PTS']], annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
# plt.title('Correlation Heatmap between Features and PTS')
# plt.show()

# 예측할 통계 지정
target_stat = 'PTS' 
X = all_stats[features]
y = all_stats[target_stat]

# 데이터 정규화
split_index = int(0.8 * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Scikit-learn의 MinMaxScaler를 사용하여 정규화
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# # 신경망 모델 생성
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(32, activation='relu'),
#     tf.keras.layers.Dense(16, activation='relu'),
#     tf.keras.layers.Dense(1)
# ])

# # 모델 컴파일
# model.compile(optimizer='adam', loss='mse')

# # 모델 학습
# model.fit(X_train_scaled, y_train, epochs=70, batch_size=35, validation_split=0.2)

# # features = ['MP', 'FG', 'FGA', '3P', 'FT%', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PF']
# # 정규화하여 예측할 데이터
# player_stats_to_predict = np.array([[12.3,0.4,1.8,0.2,0.700,2.2,2.5,0.8,0.1,0.4,2.4]])
# player_stats_to_predict_scaled = scaler.transform(player_stats_to_predict)

# # 예측 및 결과 출력
# predicted_stat = model.predict(player_stats_to_predict_scaled).flatten()



# print(f'예측된 포인트 (PTS): {predicted_stat}')
loaded_model = tf.keras.models.load_model('Nba_PTS_model.h5')

# features = ['MP', 'FG', 'FGA', '3P', 'FT%', 'DRB', 'TRB', 'AST', 'STL', 'TOV', 'PF']
# 정규화하여 예측할 데이터
player_stats_to_predict = np.array([[12.3,0.4,1.8,0.2,0.700,2.2,2.5,0.8,0.1,0.4,2.4]])
player_stats_to_predict_scaled = scaler.transform(player_stats_to_predict)

# 예측 및 결과 출력
predicted_stat = loaded_model.predict(player_stats_to_predict_scaled).flatten()
print(f'예측된 포인트 (PTS): {predicted_stat}')


#모델저장
# model.save('Nba_PTS_model.h5')