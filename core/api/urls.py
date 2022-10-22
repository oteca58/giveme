from django.urls import path
from core.api import views as q

urlpatterns = [
    
    path("activities/", q.ActivitiesListApiView.as_view(), name="activities-list"),
    path("activities/create/", q.ActivityCreateAPIView.as_view(), name="create-activity"),
    path("activities/<int:pk>/", q.ActivityRUDAPIView.as_view())
]