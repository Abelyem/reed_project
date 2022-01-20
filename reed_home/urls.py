from django.urls import path
from reed_home import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("search", views.search_jobs, name="search_jobs"),
]