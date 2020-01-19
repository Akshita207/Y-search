import requests
from bs4 import BeautifulSoup
import json

from django.conf import settings
from django.shortcuts import render, redirect

def strToJSON(str):
    str = str.replace('google.sbox.p50 &amp;&amp; google.sbox.p50(', '')[0:-1]
    return json.loads(str)

def index(request):
    keyword = []
    if request.method == "POST":
        q = request.POST['query']
        base_url = 'https://clients1.google.com/complete/search?q='
        end_url = '&client=youtube&hl=en&gl=in&gs_rn=64&gs_ri=youtube&ds=yt&cp=3&gs_id=j&callback=google.sbox.p50&gs_gbg=WRtSTd9WG6xa377'
        url = base_url + q + end_url
        yelp_r = requests.get(url)

        yelp_soup = BeautifulSoup(yelp_r.text,'html.parser')
        yelp_soup = str(yelp_soup)

        def strToJSON(strx):
            strx = strx.replace('google.sbox.p50 &amp;&amp; google.sbox.p50(', '')[0:-1]
            return json.loads(strx)
            

        b = strToJSON(yelp_soup)[1]

        context = {
            'b':b
        }
        return render(request, 'search/search.html', context)
    return render(request, 'search/search.html')    
