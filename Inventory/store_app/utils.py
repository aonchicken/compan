from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
   
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8","ignore")), result)
  
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def render_to_pdf2(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO()

    pdf = pisa.pisaDocument(StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

'''
pisaDocument(
            fsrc,
            fdest,
            debug=debug,
            path=wpath,
            errout=sys.stdout,
            tempdir=tempdir,
            format=format,
            link_callback=lc,
            default_css=css,
            xhtml=xhtml,
            encoding=encoding,
            xml_output=xml_output
        )
        '''