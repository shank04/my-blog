from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/(?P<try2>[0-9]+)/$', views.detail, name='detail'),
    url(r'^posts/(?P<try2>[0-9]+)/liked/$', views.like, name='like'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^post-blog/$', views.postblog.as_view(), name='postblog'),
    url(r'^posts/edit/(?P<pk>[0-9]+)/$', views.editblog.as_view(), name='edit'),


]