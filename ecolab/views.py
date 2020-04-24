from django.http import HttpResponse
from django.template import loader
 
 
def e_handler404(request,e):
    t = loader.get_template('404.html')
    return HttpResponse(t.render(c, request))
 
 
def e_handler500(request):
    t = loader.get_template('404.html')
    return HttpResponse(t.render(c, request))