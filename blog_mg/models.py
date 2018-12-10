from django.db import models

# Create your models here.
class Category(models.Model):
	"""
	分类模型
	"""
	category_name = models.CharField(max_length=127, verbose_name='类名', unique=True)

	class Meta:
		db_table = 'tb_category'


class User(models.Model):
	"""
	用户模型
	"""
	user_name = models.CharField(max_length=254, unique=True, verbose_name='用户名')
	password = models.CharField(max_length=254, verbose_name='用户密码')
	age = models.IntegerField(verbose_name='用户年龄')
	gender = models.BooleanField(verbose_name='用户性别')
	email = models.EmailField(verbose_name='用户邮箱地址')
	user_create_time = models.DateTimeField(auto_now_add=True, verbose_name='用户注册时间')
	user_update_time = models.DateTimeField(auto_now=True, verbose_name='用户信息修改时间')
	collect_article = models.ManyToManyField(to='Article', related_name='collect_article', verbose_name='收藏的文章')
	#user_id = models.CharField(max_length=8, unique=True, verbose_name='用户ID')
	head_sculpture = models.ImageField(upload_to='userpicture', verbose_name='用户头像', null=True)


	class Meta:
		db_table = 'tb_user'


class Article(models.Model):
	"""
	文章模型
	"""
	article_title = models.CharField(max_length=254, verbose_name='文章标题')
	article_text = models.TextField(verbose_name='文章内容')
	article_create_time = models.DateTimeField(auto_now_add=True, verbose_name='文章创建时间')
	article_update_time = models.DateTimeField(auto_now=True, verbose_name='文章修改时间')
	author = models.ForeignKey(to='User', related_name='author', verbose_name='作者')
	category_name = models.ForeignKey(to='Category', null=True, verbose_name='分类')
	see_number = models.IntegerField(default=0, verbose_name='被查看次数')
	collect_number = models.IntegerField(default=0, verbose_name='被收藏次数')
	desc = models.TextField(null=True, verbose_name='文章描述')
	picture = models.ImageField(upload_to='artpicture', verbose_name='图片',null=True)
	isDelete = models.BooleanField(default=0)
	isRelease = models.BooleanField(default=1)


	class Meta:
		db_table = 'tb_article'


class Discuss(models.Model):
	"""
	评论模型
	"""
	author = models.OneToOneField(User, verbose_name='评论人')
	content = models.TextField(verbose_name='评论内容')
	article = models.ForeignKey(to='Article', verbose_name='评论的文章')

	class Meta:
		db_table = 'tb_discuss'


class LeaveWords(models.Model):
	"""
	留言模型
	"""
	writer = models.OneToOneField(to='User', related_name='writer', verbose_name='留言者')
	content = models.TextField(verbose_name='留言内容')
	following = models.ForeignKey(to='User', related_name='following', verbose_name='留言对象')

	class Meta:
		db_table = 'tb_leavewords'


class Images(models.Model):
	"""
	图片模型
	"""
	img = models.ImageField(verbose_name='图片')
	owner = models.ForeignKey(to='User', verbose_name='所有者')

	class Meta:
		db_table = 'tb_images'


class Relation(models.Model):
	"""
	用户关系
	"""
	myself = models.OneToOneField(to='User', related_name='myself',verbose_name='自己')

	class Meta:
		db_table = 'tb_relation'