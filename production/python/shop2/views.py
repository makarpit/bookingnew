from django.shortcuts import render
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index(request):
    return render(request, 'shop/index.html')

def searchMatch(query, item):
        return False

def search(request):
    return render(request, 'shop/search.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productView(request, myid):
    return render(request, 'shop/prodView.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    return render(request, 'shop/paymentstatus.html')
