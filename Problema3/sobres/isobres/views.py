from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context

from django.contrib.auth.models import User

# Create your views here.


def mainpage(request):
    # S'ha d'acabar!!!.
    # return render_to_response()
    template = get_template("principal.html")
    variables = Context({
        'appname': "electrosobres",
        'titlepage': "sobres",
        'author': "Luis Barcenas"
    }
    )
    page = template.render(variables)
    return HttpResponse(page)


def dashboard(request, usuari):
    try:
        user = User.objects.get(username=usuari)
    except:
        raise Http404("L'usuari no hi es, c*ll*ns")

    sobres = user.sobre_set.all()
    template = get_template("dashboard.html")
    variables = Context({
        "username": usuari,
        "author": "Luis Barcenas",
        "sobres": sobres
    })
    page = template.render(variables)
    return HttpResponse(page)
