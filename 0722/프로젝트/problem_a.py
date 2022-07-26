import json
from pprint import pprint

def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다. 
    

    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


'''
movie_json = {
    'genre_ids': [
        18,
        80
    ],
    'id': 278,
    'original_title': 'The Shawshank Redemption',
    'release_date': '1995-01-28',
    'title': '쇼생크 탈출',
    'vote_average': 8.7,
}

def make_dict(data):
    new_data = {
        '원제': data.get('original_title'),
        '개봉년도': data.get('release_date')[:4],
        '평점': data.get('vote_average')
    }
    return new_data

print(make_dict(movie))

'''