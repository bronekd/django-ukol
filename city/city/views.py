from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Konečně jsem se spustil.")

def mycity(request):
    template = loader.get_template('mycity.html')
    return HttpResponse(template.render())

