from django.urls import path

from .views import *

urlpatterns = [
	path('blog/', blogIndex, name='blogIndex'),
	path('hot/', hot, name='hot'),
	path('tag/bender', tag, name='tag'),
	path('question/35/', question, name='question'),
	path('login/', login, name='login'),
	path('signup/', signup, name='signup'),
	path('settings/', settings, name='settings'),
	path('ask/', ask, name='ask')
]