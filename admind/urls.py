from django.urls import path
from . import views

urlpatterns = [
    path('itemwise/',views.itemwise,name='itemwise'),
    path('endoftheday/',views.endoftheday, name='endoftheday'),
    path('hourlysales/',views.Hourlysales, name = 'hourlysales'),
    path('paymentrecieved/',views.paymentrecieved, name='paymentrecieved'),
    path('salesreport/',views.salesreport, name='salesreport'),
    path('categorywise/',views.categorywise,name='categorywise')

]
