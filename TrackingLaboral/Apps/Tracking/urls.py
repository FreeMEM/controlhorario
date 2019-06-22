from django.urls import path, include
from TrackingLaboral.Apps.Tracking.views import test,tracking,trackinglist

urlpatterns = [
    path('', trackinglist, name="trackinglist"),
    path('tracking/', tracking, name="tracking"),
    path('trackinglist/', trackinglist, name="trackinglist")
]