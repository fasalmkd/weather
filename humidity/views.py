import requests
from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        response = requests.get('https://api.weatherbit.io/v2.0/current?city=%s&country=india&key=2312ee03870b4e6f972e55dc9accdcf0' %city)
        posts = response.json()
        data = posts['data']
        return render(request,"index.html",{"data":data})
    return render(request,"index.html")

# Create your views here.