import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic import View,TemplateView


class PostListView1(View):
    def get(self, request):
        name = "침밴치"
        html = '''
        <h1>원숭이들이 반란을 일으켰다</h1>
        <p>그 앞에  {name} 가 서 있었다.</p>
        <p>{name}은 뚜렸한 발음으로 자유를 외쳤다.</p>
        '''.format(name=name)
        return HttpResponse(html)

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '우랑오탄'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(View):
    def get(self, requset):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
        'message' : '원숭이들이 자유를 왜치며 혁명을 시작했다.',
        'monkeys' :['개코원숭이','우랑오탄','침밴치','그랜드고릴라','여우원숭이','비비원숭이'],
        }

post_list3 = PostListView3.as_view()


class ExcelDownloadView(View):
    filepath = os.path.join(settings.BASE_DIR, 'PROFORMA.xls')
    
    def get(self, request):
        filename = os.path.basename(self.filepath)
        with open(self.filepath, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response
            

excel_download  = ExcelDownloadView.as_view()
