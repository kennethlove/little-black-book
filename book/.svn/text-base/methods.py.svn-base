import hashlib, re
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from lbb.book.models import *


def hash_password(join_date, password):
	#CLEAN PASSWORD - REMOVE NON ALPHA NUMERIC
	pattern = re.compile('(\W|_)')
	clean_pass = re.sub(pattern, '', password)
	hsh = hashlib.sha1()
	hsh.update(str(join_date) + clean_pass + password)
	return hsh.hexdigest()
		
def login(request, uemail, upassword):
	try:	
		u = User.objects.get(email=uemail)
		if hash_password(u.date_joined, upassword) == u.password:
			request.session['user_id'] = u.id
			# return request.session['user_id']
			return HttpResponseRedirect('http://www.google.com')
		else:
			return "Bad username/password"
	except ObjectDoesNotExist:
		return "Bad username/password"
		
def logout(request):
	try:
		del request.session['user_id']
	except KeyError:
		pass
	return HttpResponse("You're logged out.")