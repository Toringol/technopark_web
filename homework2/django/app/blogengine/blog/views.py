from django.shortcuts import render

# Create your views here.

def blogIndex(request):
	return render(request, 'blog/index.html')
def hot(request):
	return render(request, 'blog/question.html')
def tag(request):
	return render(request, 'blog/tag.html')
def question(request):
	return render(request, 'blog/question.html')
def login(request):
	return render(request, 'blog/login.html')
def signup(request):
	return render(request, 'blog/signup.html')
def settings(request):
	return render(request, 'blog/settings.html')
def ask(request):
	return render(request, 'blog/ask.html')