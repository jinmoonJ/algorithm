# 1. pip
    # 무엇을 위한 명령인지? => faker 패키지를 설치하기 위한 명령어
    # 실행은 어디에서 해야하는지? => git bash, 윈도우는 cmd, 파워쉘도 가능

# 2. Basic Usages
'''
from faker import Faker # 1. Faker 클래스를 faker 패키지에서 불러오기위한 코드
fake = Faker() # 2. Faker 클래스의 인스턴스를 생성 : fake는 Faker클래스의 인스턴스이다.
fake.name() # 3. fake의 메서드 사용 : name()은 fake의 메서드이다.
'''

# 3. Localization
    # (a) => init
    # (b) => self
    # (c) => locale

'''
class Faker():

    def __init__(self, locale="en_US"):
        pass

    # (a) = init
    # (b) = self
    # (c) = locale="en_US"

fake = Faker("fr_FR")
'''

# 4. Seeding the Generator

    # ==> 1. 이진호 2. 강은주
    # ==> Faker의 seed를 고정해 랜덤값이 아니게된다.

    # ==> 클래스 메서드
    # ==> Faker 클래스 내부의 난수 생성 값을 클래스 변수로 설정
    # ==> 설정한 후 생성된 모든 인스턴스가 해당 클래스 변수를 공유
'''
from faker import Faker

fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name()) # 1. 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 2. 강은주
'''

    # ==> 1. 이진호 2. Random 김승현 이정희 등등 
    # ==> fake1의 seed를 고정시켜 fake1의 이름만 고정

    # ==> (인스턴스 메서드)
    # seed_instance 는 인스턴스 변수를 수정하는 메서드
    # ==>
'''
from faker import Faker

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name()) # 1. 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 2. 김승현
'''
