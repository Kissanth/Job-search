from django.urls import path
from .views import * 

urlpatterns = [
	
	path('',home,name='Home'),
	path('Posting',Posting,name="Posting"),
	path('Search',Search,name="search")
]