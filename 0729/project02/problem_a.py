import requests

def popular_count():
    # 여기에 코드를 작성합니다.  
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=9c939142d902c495cd677f1a997b0328&language=ko-KR&page=1&region=KR"
    response = requests.get(URL).json()
    return len(response.get("results")) # 페이지의 results 인덱스(길이) 값을 출력



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
