from django.urls import path

from .views import *

app_name= "my_app"
urlpatterns=[

	path('',index, name='index'),
	path('submit/',url_shorten,name='url-shorten'),
	path('l/<slug:unique_id>/',url_redirect, name='url-redirect'),

]