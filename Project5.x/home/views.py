
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def homeView(request):
	context = {
		# "users": User.objects.all(),
		# "usersCount": User.objects.all().count()
	}
	return render(request, 'home/home.html', context)


def register(request):
    '''
        if the page gets a POST request, the POST's data gets instantiated to the UserCreationForm,
        otherwise, it instantiates a blank form.
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()     # to make sure that the registering user gets saved to the database
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    # arguments == "request", the_template, the_context(dictionary))
    return render(request, 'auth/register.html', {'form': form})

@login_required
def profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        # posts = Post.objects.all().filter(author=user).count()
        # todos = ToDoList.objects.filter(author=user)
        return render(request, 'home/profile.html',
            {
                "user": user,
                # "posts": posts,
                # "todos": todos,
            }
        )
        
    else:
        return render ("User not found.")


@login_required
def profile_edit(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        if request.method == 'POST':    # for the new info to be saved, this if block is needed
            # the forms from forms.py
            u_form = UserUpdateForm(request.POST, instance=request.user)        # instance is for the fields to auto-populate with user info
            # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                # p_form.save()
                messages.success(request, f"Account info has been updated.")
                return render(request, "home/profile_detail.html", {"user":user})

        else:
            u_form = UserUpdateForm(instance=request.user)
            # p_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'u_form': u_form,
            # 'p_form': p_form,
        }
        return render(request, 'home/profile_edit.html', context)

    else:
        return render ("User not found.")