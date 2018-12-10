from django.conf.urls import url
from . import views
mg_name = 'blog_mg'
urlpatterns = [
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.login, name='login'),
	url(r'^index/', views.index, name='index'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^article/', views.article, name='article'),
	url(r'^notice/', views.notice, name='notice'),
	url(r'^comment/', views.comment, name='comment'),
	url(r'^category/', views.category, name='category'),
	url(r'^flink/', views.flink, name='flink'),
	url(r'^manage_user/', views.manage_user, name='manage_user'),
	url(r'^loginlog/', views.loginlog, name='loginlog'),
	url(r'^setting/', views.setting, name='setting'),
	url(r'^readset/', views.readset, name='readset'),
	url(r'^add_article/', views.add_article, name='add_article'),
	url(r'^add_category/', views.add_category, name='add_category'),
	url(r'^add_flink/', views.add_flink, name='add_flink'),
	url(r'^add_notice/', views.add_notice, name='add_notice'),
	url(r'^update_article/(\d+)/', views.update_article, name='update_article'),
	url(r'^update_category/(\d+)/', views.update_category, name='update_category'),
	url(r'^update_flink/(\d+)/', views.update_flink, name='update_flink'),
	url(r'^delete_article/(\d+)/', views.delete_article, name='delete_article'),
	url(r'^delete_category/(\d+)/', views.delete_category, name='delete_category'),
	url(r'^test/', views.test),
]