from django.shortcuts import render
from .models import Pages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def inicio(request):
    if request.method == "GET":
        titulo = "<h3>Bienvenido a cmsUsersPut</h3>"
        respuesta = "<br>La lista de páginas guardadas es:<br>"
        paginas = Pages.objects.all()
        for pagina in paginas:
            respuesta += "<ul><li>" + pagina.name + " => "
            respuesta += pagina.page + "</ul></li>"

        #  Logged:
        if request.user.is_authenticated():
            logged = "> Logged in as " + request.user.username
            logged += ". <a href='/logout'> Logout </a><br>"
        else:
            logged = "> Not logged in. "
            logged += "<a href='/login'> Login </a><br>"
    else:
        respuesta = "Método no permitido"
    return HttpResponse(titulo + logged + respuesta)


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

def login_exito (request):
    respuesta = "Logged in as " + request.user.username
    respuesta += " successfully"
    return HttpResponse(respuesta)
