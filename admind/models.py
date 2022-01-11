from django.db import models

# Create your models here.
class Itemwise(models.Model):
    date = models.CharField(max_length=300,blank=False)
    name = models.CharField(max_length=100, blank = False)
    unitprice = models.CharField(max_length=300, blank = False)
    qty = models.CharField(max_length=300, blank = False)
    returns = models.CharField(max_length=300, blank = False)
    netsales = models.CharField(max_length=300, blank = False)
    total = models.CharField(max_length=300, blank = False)
    cost =  models.CharField(max_length=300, blank = False)
    grossprofit = models.CharField(max_length=300, blank = False)
    profitpercent = models.CharField(max_length=300, blank = False)

    def __str__(self):
        return self.date
class Endoftheday(models.Model):
    date = models.CharField(max_length=300,blank=False)
    ticketid = models.CharField(max_length=300,blank=False)
    discount = models.CharField(max_length=300,blank=False)
    grosssales = models.CharField(max_length=300,blank=False)
    totalrecieved = models.CharField(max_length=300,blank=False)

    def __str__(self):
        return self.date


class Salesreport(models.Model):
    date = models.CharField(max_length=300,blank=False)
    grosssales = models.CharField(max_length=300,blank=False)
    returns = models.CharField(max_length=300,blank=False)
    netsales = models.CharField(max_length=300,blank=False)
    total = models.CharField(max_length=300,blank=False)
    cost = models.CharField(max_length=300,blank=False)
    grossprofit = models.CharField(max_length=300,blank=False)
    profitpercent = models.CharField(max_length=300,blank=False)

    def __str__(self):
        return self.date

class Categorywise(models.Model):
    date = models.CharField(max_length=300,blank=False)
    category = models.CharField(max_length=300,blank=False)
    grosssales = models.CharField(max_length=300,blank=False)
    returns = models.CharField(max_length=300,blank=False)
    netsales = models.CharField(max_length=300,blank=False)
    total = models.CharField(max_length=300,blank=False)
    grossprofit = models.CharField(max_length=300,blank=False)
    profitpercent = models.CharField(max_length=300,blank=False)

    def __str__(self):
        return self.date

class Hourlysales(models.Model):
    date = models.CharField(max_length=300,blank=False)
    period = models.CharField(max_length=300,blank=False)
    checks = models.CharField(max_length=300,blank=False)
    sales = models.CharField(max_length=300,blank=False)

    def __str__(self):
        return self.date

class paymentrecieved(models.Model):
    date = models.CharField(max_length=300,blank=False)
    time = models.CharField(max_length=300,blank=False)
    trans = models.CharField(max_length=300,blank=False)
    paymenttype = models.CharField(max_length=300,blank=False)
    ticketid = models.CharField(max_length=300,blank=False)
    total = models.CharField(max_length=300,blank=False)
    

    def __str__(self):
        return self.date
