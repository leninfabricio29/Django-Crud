from django.shortcuts import render

# Create your views here.


def home(request):
    nombre = "user1"

    num_visitsHome= request.session.get('num_visitsHome', 0)
    request.session['num_visitsHome'] = num_visitsHome + 1

    context = {
        'nombre':nombre,
        'num_instances':0,
        'num_visitsHome':num_visitsHome,
    } 

    print(context)
    return render(request,"appBanco/home.html")
    

def services(request):
    nombre = "user1"

    num_visitsServices= request.session.get('num_visitsServices', 0)
    request.session['num_visitsServices'] = num_visitsServices + 1

    context = {
        'nombre':nombre,
        'num_instances':0,
        'num_visitsServices':num_visitsServices,
    } 

    print(context)
    return render(request,"appBanco/services.html")
    
def banca(request):
    return render(request,"appBanco/banca.html")

def information(request):
    return render(request,"appBanco/information.html")

def contact(request):
    return render(request,"appBanco/contact.html")