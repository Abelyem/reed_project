from django.urls import path
from job_details import views

urlpatterns = [
    path("", views.job_info, name="job_info"),
]