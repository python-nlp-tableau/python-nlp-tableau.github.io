import json
import os
import requests
from django.shortcuts import render_to_response, render
from django.http import JsonResponse
# Create your views here.

def index(request):
    """ index
        @params
        @return
        @raise
    """
    return render_to_response('dashboard.html')

def tableaugetdata(request):
    """ tableau get data
        @params
        @return
        @raise
    """
    response_data = {}
    return JsonResponse(response_data)