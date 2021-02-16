import pandas as pd
u_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('ml-100k/u.user',sep='|',names=u_cols)
m_cols = ['movie_id','title','release_date', 'video_release_date','imdb_url']
movies = pd.read_csv('ml-100k/u.item',sep='|', names = m_cols, usecols=range(5),encoding='latin1')

#영화 인기 순위 top5
print(movies.head())
