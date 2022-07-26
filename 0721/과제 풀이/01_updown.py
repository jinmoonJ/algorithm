import random

is_playing = True # 게임을 실행 중인지 나타내는 변수

while is_playing: # while 반복문이 실행되는 동안 -- > 게임이 실행중이다
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    while True:
        print() #띄어쓰기
        # 1-1. 숫자를 입력 받기(정수만 입력한다고 가정)
        number = int(input("1이상 10000이하의 숫자를 입력하세요"))
        
        # 1-2. 범위 바깥의 숫자를 입력했을때, 잘못되었다고 알려준후 1-1로 돌아간다
        if number > 10000 or number < 1:
            print("잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.")
            continue # 실행하지 않고 반복문의 시작으로 돌아감 ## 1-1로 돌아가야하기 떄문에 1-1 에서 다시 반복문

        # 플레이어의 시도 횟수를 1증가시킨다.
        counts += 1

        # 2-1. 플레이어가 입력한 숫자와 정답을 비교하여 up, down을 출력한다.
        # number : 플레이어가 입력한 숫자
        # answer : 정답

        if number > answer:
            print("Down!!!")
        elif number < answer:
            print("Up!!!")
        else:
            # 2-2. 정답이라면 시도 회수와 함께 정답 문구를 출력한다.
            print(f"Correct!!! {counts}회 만에 정답을 맞히셨습니다.")
            print()
            break # 정답을 맞힌 경우 반복문 종료

    # 3. 게임 재시작 여부 파악하기
    # 3-1. 재시작 여부를 묻는 문구를 출력
    command = input("게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. : ")

    # 3-2. y를 입력받으면 게임을 재시작
    if command == "y":
        print()
        continue # continue로 게임을 종료하지않고 반복하도록 한다.

    # 3-3. n을 입력받으면 게임을  종료한다.
    # 3-4. y와 n 이외의 다른 문자를입력받으면 종료
    elif command == "n":
        print("이용해주셔서 감사합니다. 게임을 종료합니다")
    else:
        print("잘못된 값을 입력하셨습니다. 게임을 종료합니다.")

    is_playing = False # 다음 반복문에서 조건을 검사할때 False이면 반복문을 종료한다.


