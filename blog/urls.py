from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<try2>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<try2>[0-9]+)/liked/$', views.like, name='like')

]