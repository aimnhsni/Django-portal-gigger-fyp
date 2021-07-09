


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	
	
)
from .models import Post


def get_user_profile(request, username):

    user = User.objects.get(username=username)

    return render(request, 'blog/userprofile.html', {"user":user})




def home(request):


	context = {
	    'posts': Post.objects.all()
	}


	return render(request, 'blog/home.html', context)



class PostListView(ListView):


	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date']
	paginate_by = 10


class UserPostView(ListView):


	model = Post
	template_name = 'blog/mypost.html'
	context_object_name = 'posts'
	ordering = ['-date']
	





class UserProfileView(ListView):


	model = Post
	template_name = 'blog/user_profile.html'
	context_object_name = 'posts'
	paginate_by = 5


	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date')





class PostDetailView(DetailView):
	model = Post








class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'description', 'salary', 'location']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'description', 'salary',  'location']


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/job'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def index(request):
	return render(request, 'blog/index.html', {'title': 'Welcome'})


def dashboard(request):
	return render(request, 'blog/dashboard.html', {'title': 'Dashboard'})


def company(request):
	return render(request, 'blog/company.html', {'title': 'Company Analysis'})

def admin(request):
	return render(request, 'blog/admin.html', {'title': 'Admin Hehe'})


def homepage(request):



	return render(request, 'blog/homepage.html', {'title': 'homepage'})


