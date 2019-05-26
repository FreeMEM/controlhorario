from django.contrib import admin
#from .models import Company, Employee, Track
#from TrackingLaboral.Apps.Tracking.models import *
from TrackingLaboral.Apps.Tracking.models import Company, Employee, Track
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Track)
