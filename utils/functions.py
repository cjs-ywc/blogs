from django.http import HttpResponseRedirect
from django.urls import reverse
from blog_mg.models import User
def is_login(func):
	def check_status(request):
		user_id = request.session.get('user_id')
		if user_id:
			username = User.objects.get(pk=user_id).user_name
			return func(request, username)
		else:
			return HttpResponseRedirect(reverse('blog_mg:login'))
	return check_status