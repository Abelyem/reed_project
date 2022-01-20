from django.shortcuts import render, HttpResponse
import requests


def job_info(request):
    return render(request, 'job_details/details.html')

