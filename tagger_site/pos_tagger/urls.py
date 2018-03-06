from django.conf.urls import url
from . import views

app_name = 'tagger'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^output/$', views.output, name='output'),
    # url(r'^test/$', views.test, name='test'),
]
