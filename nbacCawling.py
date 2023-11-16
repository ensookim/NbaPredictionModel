from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


start_year = 2010
end_year = 2023

all_stats = pd.DataFrame()

for year in range(start_year, end_year + 1):
    url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")
    
    # 헤더 추출
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    headers = headers[1:]  # 첫 번째 열(순위)을 제외합니다.
    print(headers)
    
    # 선수 통계 추출
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

    # 현재 연도에 대한 DataFrame 생성
    stats = pd.DataFrame(player_stats, columns=headers)
    
    # 연도 열 추가
    stats['Year'] = year
    all_stats = pd.concat([all_stats, stats], ignore_index=True)
# scv 파일 저장
all_stats.to_csv('nba_stats_{}_to_{}2.csv'.format(start_year, end_year), index=False)
