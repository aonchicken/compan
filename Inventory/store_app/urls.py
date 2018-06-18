#!python
# log/urls.py
from django.conf.urls import url

from .import views
#2pdf
from store_app.views import GeneratePdf
#from django_pdfkit import PDFView

#log in 
from django.contrib.auth.decorators import login_required

#from easy_pdf.views import PDFTemplateView
from .views import PDF_View
from django.template import Context, loader

#from .models import Product

#product = Product.objects.get(id=1)
'''context = {
    'amount': 39.99,
    'customer_name': 'Cooper Mann',
    'order_id': 'เอกสารใบส่งมอบสินค้า',
    'name': 'TTTTT',#product.device_name,
}'''
#context = Context({'amount': 39.99,})



# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product/(?P<id>[0-9]+)/', views.detail, name='detail'),#localhost:8000/product/10/
    url(r'^addnew/', views.addnew, name="addnew"),
    url(r'^edit/(?P<id>[0-9]+)/', views.edit, name="edit"),
    url(r'^document/', views.document, name="document"),
    url(r'^doc_pdf/', views.doc_pdf, name="doc_pdf"),
    url(r'^my-pdf/', PDF_View.as_view(inline=True,template_name='doc_pdf.html'),name='my-pdf'),

    
    #url(r'^pdf-inline/', PDFView.as_view(inline=True, template_name='doc_pdf.html'), name='pdf-inline'),
    #url(r'^pdf-filename/', PDFView.as_view(filename='foo.pdf', template_name='doc_pdf.html'), name='pdf-filename'),

    
    
]
