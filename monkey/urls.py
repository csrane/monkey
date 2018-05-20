from django.conf import settings
from django.conf.urls import include,url
from django.contrib import admin
from django.shortcuts import redirect, resolve_url

# def root(request):
    # return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$', root, name='root'),
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls' ,namespace='blog')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'^shop/',include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
