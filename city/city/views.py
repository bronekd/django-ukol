from django.http import HttpResponse
from django.template import loader

# tento index se spouštěl na začátku při propramování
def index_old(request):
    return HttpResponse("Konečně jsem se spustil.")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def mycity(request):
    template = loader.get_template('mycity.html')
    return HttpResponse(template.render())

def facts(request):
    template = loader.get_template('facts.html')
    return HttpResponse(template.render())

def history(request):
    template = loader.get_template('history.html')
    return HttpResponse(template.render())

def photos(request):
    template = loader.get_template('history_photos.html')
    return HttpResponse(template.render())

