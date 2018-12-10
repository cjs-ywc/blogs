from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from blog_mg.models import  User, Category, Article, Discuss, LeaveWords
from .mg_form import RegisterForm, LoginForm, ArticleAddForm, ArticleUpdateForm
from django.core.paginator import Paginator

# Create your views here.


def register(request):
	"""
	注册
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/register.html')
	if request.method == 'POST':
		form = RegisterForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			age = form.cleaned_data['age']
			gender = form.cleaned_data['gender']
			email = form.cleaned_data['email']
			icon = form.cleaned_data['icon']
			if password1 != password2:
				return render(request, 'blog_mg_tmp/register.html', {'tip':'两次密码设置不一样'})
			else:
				User.objects.create(user_name=username, password=password1, age=age, gender=gender, email=email, head_sculpture=icon)
				return HttpResponseRedirect(reverse('blog_mg:login'))
		else:
			return render(request, 'blog_mg_tmp/register.html', {'form': form})


def login(request):
	"""
	登录
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/login.html')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			passwd = form.cleaned_data['userpwd']
			user = User.objects.filter(user_name=username).first()
			if user and  user.password == passwd:
				request.session['user_id'] = user.id
				return HttpResponseRedirect(reverse('blog_mg:index'))
			else:
				return render(request, 'blog_mg_tmp/login.html', {'tip': '用户名或密码错误'})
		else:
			return render(request, 'blog_mg_tmp/login.html', {'login_form': form})


def index(request):
	"""
	后台主页
	:param request:
	:param username:
	:return:
	"""
	if request.method == 'GET':
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		return render(request, 'blog_mg_tmp/index.html', {'username': username})


def logout(request):
	"""
	退出登录
	:param request:
	:return:
	"""
	request.session.flush()
	return HttpResponseRedirect(reverse('blog_mg:login'))


def article(request):
	"""
	全部文章列表
	:param request:
	:param username:
	:return:
	"""
	if request.method == 'GET':
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		articles = Article.objects.all().filter(isDelete=0).filter(
			author=User.objects.filter(pk=request.session.get('user_id')).first())
		number = int(request.GET.get('page', 1))
		paginator = Paginator(articles, 4)
		page = paginator.page(number)
		return render(request, 'blog_mg_tmp/article.html', {'username': username, 'page': page})


def add_article(request):
	"""
	添加文章
	:param request:
	:return:
	"""
	if request.method == 'GET':
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		return render(request, 'blog_mg_tmp/add-article.html',{'username': username})
	if request.method == 'POST':
		form = ArticleAddForm(request.POST, request.FILES)
		if form.is_valid():
			article_title = form.cleaned_data['title']
			article_text = form.cleaned_data['content']
			author = User.objects.filter(pk=request.session.get('user_id')).first()
			category = form.cleaned_data['tags']
			if not Category.objects.filter(category_name=category):
				Category.objects.create(category_name=category)
			category_name = Category.objects.filter(category_name=category).first()
			desc = form.cleaned_data['describe']
			picture = form.cleaned_data['titlepic']
			isRelease = form.cleaned_data['visibility']
			Article.objects.create(category_name=category_name, article_text=article_text, article_title=article_title, author=author, desc=desc, picture=picture, isRelease=isRelease)
			return HttpResponseRedirect(reverse('blog_mg:article'))
		else:
			return render(request, 'blog_mg_tmp/add-article.html', {'form':form})

def update_article(request, article_id):
	"""
	更新文章
	:param request:
	:return:
	"""
	art = Article.objects.filter(pk=article_id).first()
	if request.method == 'GET':
		username = User.objects.filter(pk=request.session.get('user_id')).first().user_name
		return render(request, 'blog_mg_tmp/add-article.html',{'article':art, 'username': username})
	if request.method == 'POST':
		form = ArticleUpdateForm(request.POST, request.FILES)
		if form.is_valid():
			article_title = form.cleaned_data['title']
			article_text = form.cleaned_data['content']
			author = User.objects.filter(pk=request.session.get('user_id')).first()
			category = form.cleaned_data['tags']
			if not Category.objects.filter(category_name=category):
				Category.objects.create(category_name=category)
			category_name = Category.objects.filter(category_name=category).first()
			desc = form.cleaned_data['describe']
			picture = form.cleaned_data['titlepic']
			isRelease = form.cleaned_data['visibility']
			art.article_title = article_title
			art.article_text = article_text
			art.author = author
			art.category_name = category_name
			art.desc = desc
			art.isRelease = isRelease
			if picture:
				art.picture = picture
			art.save()
			return HttpResponseRedirect(reverse('blog_mg:article'))
		else:
			return render(request, 'blog_mg_tmp/add-article.html', {'form':form, 'article':art })


def delete_article(request, article_id):
	"""
	逻辑删除文章
	:param request:
	:param article_id:
	:return:
	"""
	if request.method == 'GET':
		art = Article.objects.filter(pk=article_id).first()
		art.isDelete =1
		art.save()
		return HttpResponseRedirect(reverse('blog_mg:article'))


def notice(request):
	"""
	网站公告
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/notice.html')


def add_notice(request):
	"""
	发布公告
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/add-notice.html')


def comment(request):
	"""
	评论
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/comment.html')


def category(request):
	"""
	分类
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/category.html')


def add_category(request):
	"""
	增加分类
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/add-category.html')


def update_category(request):
	"""
	更改分类
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/update-category.html')


def delete_category(request):
	pass


def flink(request):
	"""
	友情链接
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/flink.html')


def add_flink(request):
	"""
	增加友情链接
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/add-flink.html')


def update_flink(request):
	"""
	更改友情链接
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/update-flink.html')


def manage_user(request):
	"""
	管理用户
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/manage-user.html')


def loginlog(request):
	"""
	登录日志
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/loginlog.html')


def setting(request):
	"""
	基本设置
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return render(request, 'blog_mg_tmp/setting.html')


def readset(request):
	"""
	阅读设置
	:param request:
	:return:
	"""
	if request.method == 'GET':
		return  render(request, 'blog_mg_tmp/readset.html')



def test(request):
	if request.method == 'GET':
		return render(request, 'test.html')