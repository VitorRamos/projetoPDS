from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import *
from forms import *

def index(request):
    if request.method == "POST" and "logarGlobal" in request.POST:  # global login
        return login(request)

    if request.method == "POST" and "cadastrarGlobal" in request.POST:
        return HttpResponseRedirect('/cadastro')

    if request.method == "POST" and "sairGlobal" in request.POST:
        auth.logout(request)
        return HttpResponseRedirect('/')

    return render(request, "home.html")

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == "POST" and "cadastrarGlobal" in request.POST:
        return HttpResponseRedirect("/cadastro")

    avisos= []
    if request.method == "POST" and "voltar" in request.POST:
        return HttpResponseRedirect('/')

    elif request.method == "POST" and ("logar" in request.POST
                                    or "cadastrar" in request.POST
                                    or "logarGlobal" in request.POST):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get("nome"),
                                     password=form.cleaned_data.get("senha"))
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    avisos.append("Essa conta foi desativada.")
            else:
                request.path= "/login/" # bug consertar
                avisos.append("Senha ou usuario incorretos.")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form, "avisos": avisos})


def cadastro(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == "POST" and "logarGlobal" in request.POST:  # global login
        return login(request)

    avisos = []
    if request.method == "POST" and "voltar" in request.POST:
        return HttpResponseRedirect('/')

    elif request.method == "POST" and "cadastrar" in request.POST:
        form = CadastroForm(request.POST)

        if form.is_valid():
            if auth.models.User.objects.filter(username=form.cleaned_data.get("nome")).count() == 0:
                grupo = auth.models.Group.objects.get(name="Clientes")
                user = auth.models.User.objects.create_user(form.cleaned_data.get("nome"),
                                                            "emal", form.cleaned_data.get("senha"))
                user.groups.add(grupo)
                user.save()
                avisos.append("Cadastrado Com Sucesso")
                return login(request)

            else:
                avisos.append("Usuario ja existe")
                form = CadastroForm()
    else:
        form = CadastroForm()

    return render(request, "cadastro.html", {"form": form, "clientes": auth.models.User.objects.all(),
                                             "avisos": avisos})


def favoritos(request):
    if not request.user.groups.filter(name="Clientes").exists():
        return HttpResponseRedirect("/")

    if request.method == "POST" and "sairGlobal" in request.POST:
        auth.logout(request)
        return HttpResponseRedirect("/")

    return render(request, "favoritos.html")

def produtos(request):
    if not request.user.groups.filter(name="Donos").exists():
        return HttpResponseRedirect("/")

    if request.method == "POST" and "sairGlobal" in request.POST:
        auth.logout(request)
        return HttpResponseRedirect("/")

    avisos= []
    if request.method == "POST" and "cadastrarProd" in request.POST:
        form = CadastroProd(request.POST)

        if form.is_valid():
            produto = Produto()
            produto.nome = form.cleaned_data.get("nome")
            produto.marca = form.cleaned_data.get("marca")
            produto.save()

        else:
            avisos.append("Produto Invalido")

    else:
        form = CadastroProd()

    return render(request, "produtos.html", {"form":form, "avisos":avisos,
                                             "produtos":Produto.objects.all()})

def sobre(request):
    if request.method == "POST" and "logarGlobal" in request.POST:  # global login
        return login(request)

    if request.method == "POST" and "sairGlobal" in request.POST:
        auth.logout(request)
        return HttpResponseRedirect("/")

    if request.method == "POST" and "cadastrarGlobal" in request.POST:
        return HttpResponseRedirect("/cadastro")

    return render(request, "sobre.html")