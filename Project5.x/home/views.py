
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .models import User

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
