from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('chaos/index.html')
    context = {'title' : 'Accueil'}
    return HttpResponse(template.render(context, request))

def produit(request):
    template = loader.get_template('chaos/index.html')
    context = {'title': 'Produit'}
    return HttpResponse(template.render(context, request))