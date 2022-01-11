from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from . models import Itemwise, Endoftheday, Salesreport, Categorywise,Hourlysales, paymentrecieved
# Register your models here.
class ItemwiseAdmin(admin.ModelAdmin):
    list_display = ('date','unitprice','qty','returns','netsales','total','cost','grossprofit','profitpercent')

class ItemAdmin(ImportExportModelAdmin):
    resource_class = Itemwise



class ImportExportAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(Itemwise,ImportExportAdmin)
admin.site.register(Endoftheday,ImportExportAdmin)
admin.site.register(Salesreport,ImportExportAdmin)
admin.site.register(Categorywise,ImportExportAdmin)
admin.site.register(Hourlysales,ImportExportAdmin)
admin.site.register(paymentrecieved,ImportExportAdmin)
