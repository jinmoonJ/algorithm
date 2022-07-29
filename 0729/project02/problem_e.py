import requests
from pprint import pprint


def credits(title):
    # 여기에 코드를 작성합니다. 
    URL = f"https://api.themoviedb.org/3/search/movie?api_key=9c939142d902c495cd677f1a997b0328&language=ko-KR&query={title}&page=1&include_adult=false"
    response = requests.get(URL).json()
    movie = response.get("results")

    if movie == []:
        return
    a = movie[0]["id"]

    URL = f"https://api.themoviedb.org/3/movie/{a}/credits?api_key=9c939142d902c495cd677f1a997b0328&language=ko-KR"
    credit = requests.get(URL).json()
    cast = credit.get("cast") # credit의 cast 값을 받아옴
    crew = credit.get("crew") # credit의 crew 값을 받아옴

    list1 = []
    for i in cast:
        if i["cast_id"] < 10:    # cast의 i의 "cast_id" 값이 10 미만일때
            list1.append(i["name"])     # list1에 i의 "name"을 추가한다

    list2 = []
    for a in crew:
        if a["department"] == "Directing":
            list2.append(a["original_name"])

    dict1 = dict() # dict1이라는 딕셔너리 생성하고
    dict1["cast"] = list1   # key : "cast", value : list1 을 넣고
    dict1["directing"] = list2 # key : "directing", value : list2로 넣은다

    return dict1

    
    
# 'known_for_department': 'Directing'

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
