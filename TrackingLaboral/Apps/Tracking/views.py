from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import formats
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from .models import Track,Employee
from datetime import datetime, date
from .forms import TrackingForm

# Create your views here.
def test(request):
	return render(request,"tracking/test.html")

def trackinglist(request):
	tracklist=Track.objects.order_by(F('start').desc(nulls_last=True))[:10]
	today = datetime.today()
	return render(request,"tracking/trackinglist.html",{'tracklist': tracklist,"today":today})

def tracking(request):
	results = None
	if request.method == 'POST':
		form = TrackingForm(request.POST)
		results = form
		if form.is_valid():
			post = form.save(commit=False)

			post.employee=Employee.objects.filter(email="francisco@ttss.net").first()
			print(post)
			# post.start = 
			post.save()
		else:
			print("algo salio mal")	
			print(form.errors)
		
	else:
		form = TrackingForm()
	
	today = datetime.today()
	# print(type(tracklist[0].start))
	#return render(request,"tracking/tracking.html",{'tracklist': tracklist,'isToday':isToday,'today':today})
	return render(request,"tracking/tracking.html",{'form':form,"today":today, "results":results})