from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response as rtr
from lbb.book.models import *
from lbb.book.methods import *
from lbb.book.login_forms import LoginForm, SignUpForm

def index(request):
	try:
		if request.POST['which_form'] == "signup":
			return HttpResponse("SIGNUP")
		elif request.POST['which_form'] == "login":
			loginform = LoginForm(request.POST)
			signupform = SignUpForm()
			
			# return HttpResponse(login(request, request.POST['login_email'], request.POST['login_password']))
	except KeyError:
		loginform = LoginForm()
		signupform = SignUpForm()
	return rtr("index.html",{
		'loginform': loginform,
		'signupform': signupform
	})
	
def test(request):
	fuckyou = hash_password("2008-05-31", "obonl")
	return HttpResponse(fuckyou)
