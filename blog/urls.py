from django.urls import path ,re_path
from .views import blog_title,blog_article

app_name='blog'

urlpatterns=[
		path('list/',blog_title,name='blog_title'),
		re_path('detail/(?P<article_id>\d+)/',blog_article,name='blog_article')

]