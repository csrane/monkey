#dojo.views.py
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, GameUserSigupForm
from .models import Post

class DetailView(object):
    '이전 FBV를 CBV버전으로 컨셉만 간단히 구현. 같은 동작을 수행'
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs['id'])

    def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)

    def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
        self.model._meta.model_name: self.get_object(*args, **kwargs),
        })

    @classmethod
    def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view

post_detail = DetailView.as_view(Post)

def create_user(request):
    if request.method == 'POST':
        form = GameUserSigupForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('/dojo')
    else:
        form = GameUserSigupForm
    return render(request, 'dojo/user_form.html', {
        'form' : form,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo') #namespace:name
    else:
        form = PostForm
    return render(request, 'dojo/post_form.html', {
        'form' : form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo') #namespace:name
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form' : form,
    })


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


def post_list2(request):
    name = '우랑오탄'
    response  = render(request, 'dojo/post_list.html', {'name' : name})
    return response


def post_list3(request):
    return JsonResponse({
        'message' : '원숭이들이 자유를 왜치며 혁명을 시작했다.',
        'monkeys' :['개코원숭이','우랑오탄','침밴치','그랜드고릴라','여우원숭이','비비원숭이'],
    },json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    #filepath = '/Users/Waterbeast/monkey/PROFORMA.xls'
    filepath = os.path.join(settings.BASE_DIR, 'PROFORMA.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response