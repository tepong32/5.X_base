
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