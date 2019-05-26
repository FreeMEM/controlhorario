from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import formats
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from .models import Track
from datetime import datetime, date
from .forms import TrackingForm

# Create your views here.
def test(request):
	return render(request,"tracking/test.html")

def tracking(request):

	if request.method == 'POST':
		form = TrackingForm(request.POST)
				
		if form.is_valid():
			post = form.save(commit=False)
			print(post)
			# post.start = 
			# post.save()
		else:
			print("algo salio mal")	
			print(form.errors)
		# return redirect('Tracking:tracking')
	else:
		form = TrackingForm()
	


	tracklist=Track.objects.order_by(F('start').desc(nulls_last=True))[:10]
	#isToday = (False,True)[tracklist[0].start.date() < datetime.today().date()]
	today = datetime.today()
	# print(type(tracklist[0].start))
	#return render(request,"tracking/tracking.html",{'tracklist': tracklist,'isToday':isToday,'today':today})
	return render(request,"tracking/tracking.html",{'tracklist': tracklist,'form':form,"today":today})