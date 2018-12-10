
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from blog_mg.models import  User, Category, Article
# Create your views here.

def blog_index(request):
	"""
	博客主页
	:param request:
	:return:
	"""
	if request.method == 'GET':
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		articles = Article.objects.all().filter(isDelete=0, isRelease=1).filter(
			author=User.objects.filter(pk=request.session.get('user_id')).first())
		return render(request, 'blog_app_tmp/index.html',{'username': username, 'articles': articles})


def blog_about(request):
	"""
	关于博主
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_app_tmp/about.html')


def blog_gbook(request):
	"""

	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_app_tmp/gbook.html')


def blog_info(request, article_id):
	"""
	文章详细内容
	:param request:
	:return:
	"""
	if request.method == "GET":
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		article = Article.objects.filter(pk=article_id).first()
		return render(request, 'blog_app_tmp/info.html', {'username':username, 'article':article})


def blog_infopic(request):
	"""

	:param request:
	:return:
	"""
	if request.method == "GET":
		return render(request, 'blog_app_tmp/infopic.html')


def blog_list(request):
	"""

	:param request:
	:return:
	"""
	if request.method == "GET":
		return render(request, 'blog_app_tmp/list.html')


def blog_share(request):
	"""

	:param request:
	:return:
	"""
	if request.method == "GET":
		return render(request, 'blog_app_tmp/share.html')