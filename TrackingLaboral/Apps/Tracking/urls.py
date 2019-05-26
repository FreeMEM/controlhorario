from django.urls import path, include
from TrackingLaboral.Apps.Tracking.views import test,tracking

urlpatterns = [
    path('test', test, name='test-view'),
    path('tracking', tracking, name="tracking")
]