#do.views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    #nunbers = "1/2/213/214/315/425"
    result = sum(map(lambda s : int(s or 0) , numbers.split('/')))
    return HttpResponse(result)
 
def hello(request, name, age):
    return HttpResponse('Hello, {}님은 {} 살입니다.'.format(name, age))

def post_list1(request):
    name = '침밴지'
    return HttpResponse('''
    <h1>원숭이들이 반란을 일으켰다</h1>
    <p>그 앞에  {name} 가 서 있었다.</p>
    <p>{name}은 뚜렸한 발음으로 자유를 외쳤다.</p>
    '''.format(name=name))