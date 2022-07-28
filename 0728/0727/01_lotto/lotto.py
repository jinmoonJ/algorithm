# 여기에 필요한 모듈을 추가합니다.
import random
import json



class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        # 빈 리스트를 인스턴스 변수인 number_lines에 할당한다.
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        # 로또 당첨 번호를 n줄 생성해서 인스턴스 변수인 number_lines에 추가
        for _ in range(n):
            # 1부터 45 까지의 수 중에서 중복없이 6개 뽑기 + 정렬까지
            line = sorted(random.sample(range(1,46),6))
            self.number_lines.append(line)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = Lotto.get_draw_date(draw_number) # 스태틱 부를때 self. 써도 되고 Lotto처럼 클래스 써도 된다.

        print("=============================================")
        print(f"           제 {draw_number} 회 로또")
        print("=============================================")
        print(f"추첨일 : {year}/{month}/{day} (토)")
        print("=============================================")

        # 아스키 코드를 이용해서 A ~ E 로 줄 번호 출력
        # A 는 아스키 숫자로 65
        # B 는 아스키 숫자로 66
        # E 는 아스키 숫자로 69

        # for i in range(len(self.number_lines)):

        for i, line in enumerate(self.number_lines): # enumerate 사용 해서  두가지 다 알아올수있음
            print(f"{chr(65 + i)} : {line}")

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        # 메인 번호, 보너스 번호를 추출해서 가져오기
        main_numbers, bonus_numbers = Lotto.get_lotto_numbers(draw_number)

        print("=============================================")
        print(f"당첨 번호 : {main_numbers} + {bonus_number}")
        print("=============================================")

        for i, line in enumerate(self.number_lines):
            # 우리가 뽑은 번호와 당첨 번호를 비교
            # 일치하는 갯수, 보너스 번호 일치 여부
            same_main_counts, is_bonus = Lotto.get_same_info(
                main_numbers, bonus_number, line
            )

            # 당첨 결과(등수)
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)

            # 각 로또 번호 줄에 대해서 당첨 결과를 출력
            result = f"{chr(65+i)} : {same_main_counts}개 "

            if is_bonus:
                result += "+ 보너스"
            result += "일치"
            result += "(낙첨)" if ranking == -1 else f"{ranking}등 당첨!"

            print(result)

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f"data/lotto_{draw_number}.json") # 파일 열기
        lotto_dict = json.load(lotto_json) # json ==> dict로
        draw_date = lotto_dict.get("drwNoDate") # 추첨 날짜 정보 추출
        # 날짜 형식이 2022-07-09
        year, month,day = draw_date.split("-") # "-" 를 기준으로 문자열 쪼개기

        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f"data/lotto_{draw_number}.json")
        lotto_dict = json.load(lotto_json) # json => dict로 바꿔줌

        main_numbers = sorted([value for key, value in lotto_dict.items() if key.startswith("drwt")])

        #[Lotto_dict.get(f"drwtNo{i+1}") for i in range(6)]

        bonus_number = lotto_dict.get("bnusNo")
        
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        
        # 한줄의 로또 번호와 메인 번호를 비교해서 몇개가 일치하는지
        same_main_counts = 0
            
        # 집합을 사용해서 겹치는 번호의 개수 알아내기
        same_main_counts = len(set(main_numbers) & set(line)) # "&" set 사이에 오면 교집합을 나타낸다(두집합에 포함된 원소만 )

        # 보너스 번호가 일치하는지
        is_bonus = True

        if bonus_number in line:
            is_bonus = True
        else:
            is_bonus = False
        
        # is_bonus = True if bonus_number in line else False

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking = -1 # 기본값, 등수가 없을때

        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5:
            ranking = 2 if is_bonus else 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5

        return ranking
