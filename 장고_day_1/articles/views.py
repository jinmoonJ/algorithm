from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # request : 사용자의 요청 정보가 담겨있다.
    # 사용자에게 보여줄 화면 html 파일 이름
    return render(request, "index.html")

def greeting(request):
    # 화면에 필요한 데이터들
    foods = ["사과", "바나나", "코코넛"]
    info = {"name" : "jinmoon", "age": 25}

    # 각 데이터들을 다시 context라는 큰 딕셔너리로 묶은 다음
    context = {
        "foods" : foods,
        "info" : info,
    }
    # 큰 딕셔너리인 context를 return 해준다
    return render(request, "greeting.html", context)

def dinner(request):
    foods = ["족발", "치킨", "햄버거", "초밥", "슈바인학세"]
    pick = random.choice(foods)
    con = "ABc vvvv eqtt III"
    age = 25
    context = {
        "pick" : pick,
        "foods" : foods,
        "con" : con,
        "my_age": age,
    }
    return render(request, "dinner.html", context)

def throw(request):
    return render(request, "throw.html")

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get("message"))

    message = request.GET.get("message")
    context = {"message": message}

    return render(request, "catch.html", context)

def hello(request,name):
    context = {
        "name" : name
    }
    return render(request,"hello.html", context)
