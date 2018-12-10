from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import re


class LoginStatusMiddleware(MiddlewareMixin):

	def process_request(self, request):
		if request.path in ['/blogmg/login/', '/blogmg/register/']:
			return None
		user_id = request.session.get('user_id')
		if user_id:
			return None
		else:
			return HttpResponseRedirect(reverse('blog_mg:login'))

	def process_response(self, request, response):
		return response