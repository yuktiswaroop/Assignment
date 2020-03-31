from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.urls import reverse_lazy


def home(request):
	context = {'posts' : Post.objects.all()}
	return render(request,'home.html', context)

class PostList(ListView):
	model = Post
	template_name = 'home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-created_at']
	paginate_by = 5

class UserPostList(ListView):
	model = Post
	template_name = 'user_posts.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-created_at']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(user=user).order_by('-created_at')



class PostDetail(DetailView):
	model = Post
	template_name = 'post_detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['text']
	template_name = 'post_form.html'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['text']
	template_name = 'post_form.html'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	template_name = 'post_confirm_delete.html'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user:
			return True
		return False

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def about(request):
	return render(request,'about.html', {'title' : 'About'})
