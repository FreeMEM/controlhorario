from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import formats
from django.db.models import Count, F, Value, Q
from django.db.models.functions import Length, Upper
from .models import Track,Employee
from datetime import datetime, date
from .forms import TrackingForm

# Create your views here.
def test(request):
	return render(request,"tracking/test.html")

def trackinglist(request):
	employee = Employee.objects.get(user=request.user)
	# print(employee)
	trackinglist=Track.objects.filter(Q(employee=employee) & Q(created_at__month = datetime.today().month) ).order_by(F('created_at').desc(nulls_last=True))#[:10]

	tracks={}
	for track in trackinglist:
		dateKey=datetime.strftime(track.created_at, '%Y-%m-%d')
		hour=datetime.strftime(track.created_at, '%H:%M')
		if dateKey in tracks:
			tracks[dateKey].append(hour)
		else:
			tracks[dateKey]= [hour]
	
	
	tracklist=[]
	for date,hours in tracks.items():
		# print(hours)
		row=[]
		firstRow=True
		hours.reverse()
		for key in range(len(hours)):
			if len(row) < 2:
				row.append(("-",date)[firstRow==True])
				row.append(("-",date)[firstRow==True])
				row.append(hours[key])
				firstRow=False
			else:
				row.append(hours[key])
				tracklist.append(row)
				row=[]
			# print('>> %d == %d %d == 2' % (key,len(hours),len(row)))
			if (key==len(hours)-1) and (len(row)-1==2):
				row.append("-")
				tracklist.append(row)


	# for pinta in tracklist:
	# 	print("%s %s %s %s" % (pinta[0],pinta[1],pinta[2],pinta[3]))
	# # 	hours = date.values()
	# 	print(date)
	# 	print(hours.reverse())
	print("EL TIPO ES %s" % type(tracklist))

	return render(request,"tracking/trackinglist.html",{'tracklist': tracklist})

def tracking(request):
	results = dict()
	now = datetime.now()
	if request.method == 'POST':
		form = TrackingForm(request.POST)
		
		
		if form.is_valid():
			post = form.save(commit=False)	
			today = datetime.today()
				
			# datetimeObject = datetime.datetime.strpstrptime(date_time_str, '%Y-%m-%d %H:%M')
			# post.
			results = dict(start=post.start, end=post.end)
			# post.employee=Employee.objects.filter(email="francisco@ttss.net").first()
			post.employee=Employee.objects.get(email="francisco@ttss.net")
			
			# post.start = 
			# post.save()
		else:
			print(post.start)
			print(type(post.start))
			print("algo salio mal")	
			print(form.errors)
		
	else:
		form = TrackingForm()
	
	today = datetime.today()
	# print(type(tracklist[0].start))
	#return render(request,"tracking/tracking.html",{'tracklist': tracklist,'isToday':isToday,'today':today})
	return render(request,"tracking/tracking.html",{'form':form,"today":today, "results":results})