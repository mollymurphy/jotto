from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import User_Profile, Match 
from django import forms
from .forms import UploadFileForm
from django_boto.s3 import upload

def home(request):
	return render(request, 'jotto/home.html', {})

def register(request):
	if request.method == 'GET' or request.method != 'POST':
		return render(request, 'jotto/register.html', {})
	print request.POST
	user = User.objects.create_user(username = request.POST['user_name'], email = request.POST['email'], password = request.POST['password'])
	user = authenticate(username=request.POST['user_name'],password=request.POST['password']) 
	login(request, user)
	profile = User_Profile(user=user)
	profile.save()
	return redirect('/')

class UploadFileForm(forms.Form):
	file = forms.FileField()

def upload_file(request):
	if request.method == 'GET' or request.method != 'POST': 
		form = UploadFileForm()                                          
		return render(request, "jotto/profilepic.html", {'form': form})
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		print request.FILES['file']
		upload_path = upload(request.FILES['file'])
		print upload_path
		up = User_Profile.objects.get(user=request.user)
		
		up.profilePic = upload_path
		up.save()

	return redirect('/leaderboard')

def login_user(request):
	if request.method == 'GET' or request.method != 'POST':
	   return render(request, 'jotto/login.html', {})
	user = authenticate(username = request.POST['user_name'], password = request.POST['password'])
	if not user:
		print "You did not Properly Login"
		return redirect('/login')
	login(request, user)
	return redirect('/')

def logout_user(request):
	logout(request)
	return redirect('/')

def get_word(request):
	return render(request, 'jotto/getWord.html', {})

def rules(request):
	return render(request, 'jotto/rulesPage.html', {})

def start_play(request):
	if request.user.is_authenticated():
		up = User_Profile.objects.get(user=request.user)
		return render(request, 'jotto/playGame.html', {"pic":up.profilePic})
	else:
		return redirect('/register')

def storeMatch(request):
	match = Match(user=request.user,winningWord=request.POST.get('userGuess'),win=True,userGuesses=request.POST.get('userGuessNum'))
	print request.POST.get('userGuess')
	match.save()
	return HttpResponse("")

def leaderboard(request):
	matches = Match.objects.filter(user=request.user)
	wins = matches.count
	for match in matches:
		print match.winningWord
		print match.userGuesses
	up = User_Profile.objects.get(user=request.user)
	return render(request,'jotto/leaderboard.html', {"wins": wins, "matches": matches,"pic":up.profilePic})


