from django.shortcuts import render
from .models import (
Itemwise,
Endoftheday,
Salesreport,
Categorywise,
Hourlysales,
paymentrecieved

)


# Create your views here.
def itemwise(request):
    items = Itemwise.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/itemwise-report.html',context)


def endoftheday(request):
    items = Endoftheday.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/end-of-the-day.html',context)

def Hourlysales(request):
    items = Hourlysales.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/hourly-sales.html',context)

def paymentrecieved(request):
    items = paymentrecieved.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/payment-recieved.html',context)

def salesreport(request):
    items = Salesreport.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/sales-report.html',context)

def categorywise(request):
    items = Categorywise.objects.all().order_by('-date')

    context = {
        'items': items,
    }
    return render(request,'admind/category-wise.html',context)
