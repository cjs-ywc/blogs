from django.conf.urls import url
from blog_app import views

urlpatterns = [
    url(r'^index/', views.blog_index, name='index'),
    url(r'^about/', views.blog_about, name='about'),
    url(r'^gbook/', views.blog_gbook, name='gbook'),
    url(r'^info/(\d+)', views.blog_info, name='info'),
    url(r'^infopic/', views.blog_infopic, name='infopic'),
    url(r'^list/', views.blog_list, name='list'),
    url(r'^share/', views.blog_share, name='share'),
]