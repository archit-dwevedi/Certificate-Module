from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
  #   file_path="C:/Users/Archit/Projects/Certificate_Module/temp.pdf"
  #   with open(file_path, 'wb') as pdf:
		# pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def render_to_file(path: str, params: dict):
    template = get_template(path)
    html = template.render(params)
    file_name = "temp.pdf"
    # file_path = os.path.join(os.path.abspath(os.path.dirname("__file__")), "store", file_name)
    file_path = "C:/Users/Archit/Projects/Certificate_Module/temp.pdf"
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
    return [file_name, file_path]