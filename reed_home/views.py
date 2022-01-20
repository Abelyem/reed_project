from django.shortcuts import render, HttpResponse
import requests
from reed_home.models import Job


def home(request):
     x=requests.get("https://www.reed.co.uk/api/1.0/search?keywords=junior+developer&locationName=london", auth=("0c955f14-546b-4d94-b95f-9e730fd4fad2",""))
     response= x.json()
     if 'name' and 'locationName' in request.GET:
        name = request.GET['name']
        location = request.GET['locationName']
        url = requests.get(f"https://www.reed.co.uk/api/1.0/search?keywords=junior+developer+{name}&locationName={location}", auth=("0c955f14-546b-4d94-b95f-9e730fd4fad2",""))
        response = url.json()
        return render (request, 'job_details/details.html', {'response': response})
     return render(request, 'reed_home/index.html', {'response': response})








