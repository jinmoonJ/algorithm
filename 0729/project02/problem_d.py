import requests
from pprint import pprint


def recommendation(title):
    # 여기에 코드를 작성합니다. 
    URL = f"https://api.themoviedb.org/3/search/movie?api_key=9c939142d902c495cd677f1a997b0328&language=ko-KR&query={title}&page=1&include_adult=false"
    response = requests.get(URL).json()
    movie = response.get("results") 

    if movie == []: # movie가 빈 리스트라면
        return      # None 값을 반환
    
    a = movie[0]["id"] # movie의 0번 인덱스의 id 값을 a로 할당한다
    
    URL = f"https://api.themoviedb.org/3/movie/{a}/recommendations?api_key=9c939142d902c495cd677f1a997b0328&language=ko-KR&page=1"
    recommand = requests.get(URL).json()
    recom = recommand.get("results")

    command = [] # title을 넣을 새로운 리스트

    for i in recom:
        command.append(i["title"]) # i의 title 값을 command에 추가

    return command

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
