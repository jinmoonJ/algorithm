# 1. Type Class
    # object, str, int, bool, complex, dict

# 2. Magic Method
    # __init__ = (초기화)컨스트럭터로 불리는 초기화를 위한 메소드, 처음에 반드시 호출되는 특수한 함수
    # __del__ = (소멸자)객체가 없어질 떄 호출되는 메소드
    # __str__ = 해당 객체의 출력 형태를 지정한다. 인스턴스를 출력하면 __str__의 return값이 출력된다.
    # __repr__ = (프린팅) 문자열 반환, 해당 객체의 클래스에 정의된 __repr__을 실행 결과 반환


# 3. Instance Method
    # update, get, clear, get, pop, del

# 4. 오류의 종류
    # ZeroDivisionError = 0으로 나누려고 할 때 발생
    # NameError = namespace 상에 이름이 없는 경우 발생
    # TypeError = 타입이 일치하지 않을 때, argument의 누락, 개수, 타입의 불일치시 발생
    # IndexError = index가 존재하지 않거나 범위를 벗어나는 경우 발생
    # KeyError = 해당 키가 존재하지 않는 경우 발생
    # ModuleNotFoundError = 모듈을 찾지 못했을때(모듈이 없을때) 발생
    # ImportError = 모듈은 있지만 존재하지 않는 클래스나 함수를 가져오는 경우 발생
