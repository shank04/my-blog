from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth import authenticate,login
from .models import Post
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})
    

def detail(request, try2):
    posts = Post.objects.get(pk=try2)
    #return HttpResponse("<h2>details of blog no." + str(try2) + "</h2>")
    return render(request, 'blog/det.html', {'try2': try2,'posts': posts})

def like(request, try2):
    posts = Post.objects.get(pk=try2)
    if posts.is_liked:
    	posts.is_liked=False
    	posts.save()
    else:
    	posts.is_liked=True
    	posts.save()

    return render(request, 'blog/det.html', {'try2': try2,'posts': posts})


class UserFormView(View):
	form_class=UserForm
	template_name='blog/registration-form.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			
			user.save()
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('post_list')
		return render(request,self.template_name,{'form':form})


class LoginFormView(View):
	form_class=LoginForm
	template_name='blog/login-form.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		# if form.is_valid():
			# user=form.save(commit=True)

		username=request.POST['username']
		password=request.POST['password']
			# user.set_password(password)
			# user.is_staff=True
			# user.save()
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('post_list')
		return render(request,self.template_name,{'form':form})



@login_required
def user_logout(request):
   
    logout(request)

    return redirect('post_list')

    
    

