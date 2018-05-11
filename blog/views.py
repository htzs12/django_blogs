from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


from .models import BlogArticles

class IndexView(View):
	def get(self,request):
		return render(request,'index.html',{})

def blog_title(request):
	blogs=BlogArticles.objects.all()
	return render(request,'blog_titles.html',{'blogs':blogs})

def blog_article(request,article_id):
	article=BlogArticles.objects.get(id=int(article_id))
	pub=article.publish
	return render(request,'blog_article.html',{'article':article,'publish':pub})

