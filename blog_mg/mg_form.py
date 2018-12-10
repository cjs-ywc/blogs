from django import forms


class RegisterForm(forms.Form):
	"""
	注册表单验证
	"""
	username = forms.CharField(min_length=1, max_length=8, required=True)
	password1 = forms.CharField(min_length=8, max_length=32, required=True)
	password2 = forms.CharField(min_length=8, max_length=32, required=True)
	age = forms.IntegerField(min_value=0, max_value=100, required=True)
	gender = forms.CharField(min_length=1, max_length=2, required=True)
	email = forms.CharField(required=True)
	icon = forms.ImageField(required=False)


class LoginForm(forms.Form):
	"""
	登录表单验证
	"""
	username = forms.CharField(required=True)
	userpwd = forms.CharField(required=True)


class ArticleAddForm(forms.Form):
	"""
	添加文章验证
	"""
	title = forms.CharField(required=True, max_length=31)
	content = forms.CharField(required=True)
	tags = forms.CharField(required=False, max_length=31)
	describe = forms.CharField(required=True,max_length=254)
	titlepic = forms.ImageField(required=False)
	visibility = forms.BooleanField(required=True)


class ArticleUpdateForm(forms.Form):
	"""
	添加文章验证
	"""
	title = forms.CharField(required=True, max_length=31)
	content = forms.CharField(required=True)
	tags = forms.CharField(required=False, max_length=31)
	describe = forms.CharField(required=True,max_length=254)
	titlepic = forms.ImageField(required=False)
	visibility = forms.BooleanField(required=True)