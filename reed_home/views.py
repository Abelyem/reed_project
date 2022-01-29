from django.shortcuts import render, HttpResponse
import requests, os
from dotenv import load_dotenv

load_dotenv()


def home(request):
   API_KEY = os.getenv("API_KEY")
   API_PASS = os.getenv("API_PASS")
   x=requests.get("https://www.reed.co.uk/api/1.0/search?keywords=junior+developer&locationName=london", auth=(API_KEY, API_PASS))
   response= x.json()
   if 'name' and 'locationName' in request.GET:
      name = request.GET['name']
      location = request.GET['locationName']
      url = requests.get(f"https://www.reed.co.uk/api/1.0/search?keywords=junior+developer+{name}&locationName={location}", auth=(API_KEY, API_PASS))
      response = url.json()
      return render (request, 'job_details/details.html', {'response': response})
   return render(request, 'reed_home/index.html', {'response': response})
 








