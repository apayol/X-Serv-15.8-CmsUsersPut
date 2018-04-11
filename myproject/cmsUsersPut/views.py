from django.shortcuts import render
from .models import Pages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def inicio(request):
    if request.method == "GET":
        respuesta = "<h3>Bienvenido a cmsUsersPut</h3><br>"
        respuesta += "La lista de páginas guardadas es:<br>"
        paginas = Pages.objects.all()
        for pagina in paginas:
            respuesta += "<ul><li>" + pagina.name + " => "
            respuesta += pagina.page + "</ul></li>"
    else:
        respuesta = "Método no permitido"
    return HttpResponse(respuesta)


def pagina(request, name):
    if request.method == "GET":
        try:
            pagina = Pages.objects.get(name=name)
            respuesta = pagina.page
        except Pages.DoesNotExist:
            return HttpResponseNotFound("La página no existe")
    else:
        respuesta = "Método no permitido"
    return HttpResponse(respuesta)
