"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views # 현재 경로를 뜻하는 . 을 넣어준다 article 뺴고


urlpatterns = [
    # 화면 추가 path("경로", 해당 경로를 처리해줄 views.py의 함수 이름)
    path("index/", views.index, name="index"),
    path("greeting/", views.greeting, name="greeting"),
    path("dinner/", views.dinner, name="dinner"),
    path("throw/", views.throw, name="throw"),
    path("catch/", views.catch, name="catch"),
    path("hello/<name>/", views.hello, name="hello"),
]
