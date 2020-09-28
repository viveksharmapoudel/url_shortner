import string
import random

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import F

from .models import * 
from .forms import *


def index(request):
	form=ShortURLForm()
	context={'form':form}
	return render(request, 'index.html',context)


def url_redirect(request, unique_id):
	url_object= get_object_or_404(ShortURL, unique_id=unique_id)
	url_object.count=F('count')+1
	url_object.save()
	return HttpResponseRedirect(url_object.url)


def url_shorten(request):

	if request.method == 'GET':
		url=request.GET['url']
		unique_id=create_unique_id()
		print("inside ")
		short_url_obj= ShortURL.objects.create(url=url, unique_id=unique_id)
		short_url_obj.save()
		full_shortend_url=request.META['HTTP_HOST']+'l/' + unique_id
		print(full_shortend_url)
		return JsonResponse({'full_shortend_url':full_shortend_url,
							 'msz': " Successful creation of new object"
							 '' })
	else:
		return render(request,'index.html',{'failure_msz': "invalid urls"})





def create_unique_id(str_length=7):
	random_string=''
	alpha_numerals= string.ascii_letters+ string.digits

	for _ in range(str_length):
		random_string=random_string+random.choice(alpha_numerals)
	return random_string

