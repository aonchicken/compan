''''from django.shortcuts import render

# Create your views here.
'''



from __future__ import absolute_import, print_function, unicode_literals
import os
#
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse
#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

#html2pdf

from .utils import render_to_pdf ##created in step 4
from .utils import render_to_pdf2
from django.views.generic import View
from django.template.loader import get_template,render_to_string
#html2pdf

from django.conf import settings

from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.views.generic import DetailView

from easy_pdf.views import PDFTemplateResponseMixin, PDFTemplateView


from django.template import Context, loader

from os.path import basename, splitext

from django.test import override_settings
from django.views.generic import TemplateView
import pdfkit


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating



@login_required
def home(request):
    products = Product.objects.filter(status=True)
    return render(request,'home.html',{"products" : products})  


@login_required
def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'detial.html',{"product" : product })  

@login_required
def addnew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'new.html', {'form': form})


@login_required
def edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})

@login_required
def document(request):
    product = Product.objects.get(id=1)
    return render(request,'document.html',{"product": product})  


#html2pdf

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         template = get_template('doc_pdf.html')
         product = Product.objects.get(id=1)
         context = {
              'amount': 39.99,
             'customer_name': 'Cooper Mann',
             'order_id': 'เอกสารใบส่งมอบสินค้า',
             'name': product.device_name,
         }
         html = template.render(context)
         pdf = render_to_pdf('doc_pdf.html', context )
         return HttpResponse(pdf, content_type='application/pdf')


#@login_required
def doc_pdf2(request):
    product = Product.objects.get(id=1)
    return render(request,'doc_pdf.html',{"product" : product })  
@login_required
def view_pdf(request):
    product = Product.objects.get(id=1)
    return render(request,'hello.html',{"product" : product })  



'''

def product_search(request):
    products = Product.objects.filter(name__contains = request.GET['product_search'])
    return render(request,'index.html',{"products" : products})
'''

class DemoPDFView(PDFTemplateView):
    template_name = 'hello.html'

    pdf_filename = 'hellalo.pdf'

    def get_context_data(self, **kwargs):
        return super(DemoPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            today=now(),
            **kwargs
        )


class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'





class PDF_View(TemplateView):
    #: Set to change the filename of the PDF.
    filename = None

    #: Set to default the PDF display to inline.
    inline = False

    #: Set pdfkit options dict.
    pdfkit_options = None

    def get(self, request, *args, **kwargs):


        """
        Return a HTTPResponse either of a PDF file or HTML.

        :rtype: HttpResponse
        """
        if 'html' in request.GET:
            # Output HTML
            content = self.render_html(*args, **kwargs)
            return HttpResponse(content)

        else:
            # Output PDF
            content = self.render_pdf(*args, **kwargs)

            response = HttpResponse(content, content_type='application/pdf')

            if (not self.inline or 'download' in request.GET) and 'inline' not in request.GET:
                response['Content-Disposition'] = 'attachment; filename=%s' % self.get_filename()

            response['Content-Length'] = len(content)

            return response

    def render_pdf(self, *args, **kwargs):
        """
        Render the PDF and returns as bytes.

        :rtype: bytes
        """
        html = self.render_html(*args, **kwargs)

        options = self.get_pdfkit_options()
        if 'debug' in self.request.GET and settings.DEBUG:
            options['debug-javascript'] = 1

        kwargs = {}
        wkhtmltopdf_bin = os.environ.get('WKHTMLTOPDF_BIN')
        if wkhtmltopdf_bin:
            kwargs['configuration'] = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)

        pdf = pdfkit.from_string(html, False, options, **kwargs)

        return pdf

    def get_pdfkit_options(self):
        """
        Returns ``self.pdfkit_options`` if set otherwise a default dict of options to supply to pdfkit.

        :rtype: dict
        """
        if self.pdfkit_options is not None:
            return self.pdfkit_options

        return {
            'page-size': 'A4',
            'encoding': 'UTF-8',
        }

    def get_filename(self):
        """
        Return ``self.filename`` if set otherwise return the template basename with a ``.pdf`` extension.

        :rtype: str
        """
        if self.filename is None:
            name = splitext(basename(self.template_name))[0]
            return '{}.pdf'.format(name)

        return self.filename

    def render_html(self, *args, **kwargs):
        """
        Renders the template.

        :rtype: str
        """
        static_url = '%s://%s%s' % (self.request.scheme, self.request.get_host(), settings.STATIC_URL)
        media_url = '%s://%s%s' % (self.request.scheme, self.request.get_host(), settings.MEDIA_URL)

        with override_settings(STATIC_URL=static_url, MEDIA_URL=media_url):
            template = loader.get_template(self.template_name)
            #context = self.get_context_data(*args, **kwargs)
            context = {
                'date' : '24 พฤษภาคม 2561',
                'customer_tel' : '0859078578',
                'customer_address' : 'Bankok',
                'no': 1,
                'contract_no': 'สอ.2/2561',
                'customer_name': 'สมมติ ขึ้นมา',
                'detail_pd': 'Router 892w',
                'staff_name': 'รัฐกานต์ บันที',
                'count_pd' : 1 ,
                'key_pd': '-',
                'serial_pd' : 8400344678923,
                'ref' : '-',
                'note' : '1กล่อง',
            }  
            html = template.render(context)
            return html
