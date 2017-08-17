from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category>\w+)/$', views.get_filter_category, name='category_filter'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', views.get_filter_tags, name='tags'),
]