# from django.conf.urls import url # works until django version 3
from django.urls import include, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    # re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
