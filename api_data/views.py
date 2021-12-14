from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import requests
import json

# Create your views here.

class GetData(View):
    def get(self,request):
        try:
            url = 'http://13.213.188.225:8081/listing/v1.0/read'
            request_headers = {
                'Content-Type': 'application/json'
            }
            request_body = {
                "filters": {
                    "filter_name": [
                    "value1",
                    "value2"
                    ]
                },
                "get_filters": False,
                "get_records": False,
                "listing_type": "FINAL_MH",
                "product_count": 20,
                "search_query": "*",
                "sort": [
                    "price",
                    "asc"
                ],
                "start_page": 1,
                "user_id": "email@sample.com"
            }
            json_data = json.dumps(request_body)
            res = requests.post(url = url, headers = request_headers,data = json_data)
            # print(res.json())
            listing_data = []
            for i in res.json()['result']['records']:
                listing_data.append(i)
            print(listing_data)
            return render(request,'change_form.html',{'listing_data':listing_data})
            
        except Exception as exception:
            print(exception)
        