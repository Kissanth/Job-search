from django.shortcuts import render
from .models import Postingmodel
from .forms import Postform
# Create your views here.
from django.db.models import Q
def home(request):
	return render(request,'index.html')

def Posting(request):
	job=Postingmodel.objects.all()
	form = Postform()

	title = request.get.GET('title')
	print(title)
	if request.method == 'POST':
		form = Postform(request.POST)
		if form.is_valid():

			form.save()
			return render(request,'index.html')

	return render(request,'Posting.html')


def Search(request):
	return render(request,'Search.html')


	


# def filters(request):
	
	# result = Postingmodel.objects.filter(Q(title__icontains=""))

