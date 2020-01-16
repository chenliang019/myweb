from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import csv
from .models import Product

def index(request):
    return HttpResponse("Hello world")

def myyear(request,year):
    return render(request,'myyear.html')

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    writer.writerow(['How', 'are', 'you'])
    return response

def huawei(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    context = {'title':'首页','type_list':type_list,'name_list':name_list}
    return render(request,'index.html',context=context,status=200)

def login(request):
    if request.GET.get('name'):
        name = request.GET.get('name')
    else:
        name = 'Everyone'
    return HttpResponse('usename is '+ name)

