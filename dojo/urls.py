from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
] 