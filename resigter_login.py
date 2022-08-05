from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
def register(request):
  if request.method == 'POST':
  	# Get form values
  	#first_name=request.POST['first_name']
  	#last_name=request.POST['last_name']
  	username=request.POST['username']
  	email=request.POST['email']
  	password1=request.POST['password1']
  	password2=request.POST['password2']
  	
  	# Password match
  	if(password1==password2):
  		# Check Username
  		if User.objects.filter(username=username).exists():
  			messages.error(request,'The username is not available')
  			return redirect('register')
  		else:
  			if User.objects.filter(email=email).exists():
  				messages.error(request,'The Email ID is not available')
  				return redirect('register')
  			else:
  				# Looks good, data entered by user is valid
  				user = User.objects.create_user(username=username,password=password1,
  						email=email)
  				user.save()
  				messages.success(request,"You are now registered and can login")
  				return redirect('login')
  	else:
  		messages.error(request,'Password do not match')
  		return redirect("register")
  else:
  	return render(request,'accounts/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request,user)
			messages.success(request, "You are now logged in")
			return redirect('dashboard')
		else:
			messages.error(request,'Invalid username/password')
			return redirect('login')
	else:
		return render(request,'accounts/login.html')

def logout(request):
  if request.method == 'POST':
  	 auth.logout(request)

  	 return redirect('index')

def dashboard(request):
  return render(request,'accounts/dashboard.html')
