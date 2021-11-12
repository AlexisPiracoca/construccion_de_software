from django.http import HttpResponse
from django.shortcuts import render, redirect
from characters.models import Character, PowerCharacter
from django.db.models import Count
from django.db.models import Q

def list(request):
    print(request.method)
    list = Character.objects.all()
    return render(request, 'characters/index.html', {"list":list})


def save(request):
    if request.method == "GET":
        return render(request, 'characters/save.html')
    name_ = request.POST['name']
    description_ = request.POST['description']
    file = request.FILES["file"]
    character = Character(
        name=name_,
        description=description_,
        path=file
    )
    character.save()
    return redirect('characters:list_characters')

def detail(request, id):
    try:
        character = Character.objects.get(id=id)
    except Character.DoesNotExist:
        return HttpResponse("Not found register")
    return render(request, 'characters/detail.html', {"character":character})

def edit(request, id):
    return HttpResponse(id)

def puntoUno(request):
    list = Character.objects.select_related('cit')
    html = ""
    for character in list:
       html = html + character.name + " || " + character.cit.name + "<br>" 
    return HttpResponse(html)

def puntoDos(request):
    list = (Character.objects.select_related('cit')
                             .values('cit')
                             .annotate(personajes=Count('cit'))
                             .order_by('cit'))
    html = list  
    return HttpResponse(html)
    
def puntoTres(request):
    list = PowerCharacter.objects.select_related('pow','cha')
    html = ""
    for character in list:
       html = html + character.cha.name + " || " + character.cha.cit.name + " || " + character.pow.name + " || " + str(character.level) +"<br>" 
    return HttpResponse(html)

def puntoCuatro(request):
    list = (Character.objects.select_related('cit')
                             .values('cit')
                             .annotate(personajes=Count('cit'))
                             .order_by('cit'))
    html = list  
    return HttpResponse(html)

def puntoCinco(request):
    list = Character.objects.filter(name__contains="u")
    html = ""
    for character in list:
        html = html + character.name+"<br>"
    return HttpResponse(html)

def puntoSeis(request):
    list = PowerCharacter.objects.select_related('cha').filter(Q(pow__name__contains='Super fuerza') & Q(pow__name__contains='Volar') & Q(pow__name__contains='Telequinesis'))
    html = ""
    for character in list:
        html = html + character.cha.name + " || " + character.pow.name + "<br>"
    return HttpResponse(html)

def puntoSiete(request):
    list = PowerCharacter.objects.select_related('cha').filter(
        Q(pow__name__contains='Super fuerza') | Q(pow__name__contains='Volar') | Q(pow__name__contains='Telequinesis'))
    html = ""
    for character in list:
        html = html + character.cha.name + " || " + character.pow.name + "<br>"
    return HttpResponse(html)

def puntoOcho(request):
    list = Character.objects.filter(Q(date_of_birth__range=('2010','2020')))
    html = ""
    for character in list:
        html = html + character.name + " || " + character.date_of_birth +"<br>"
    return HttpResponse(html)

def puntoNueve(request):
    list = Character.objects.filter(date_of_birth__lt=2011)
    html = ""
    for character in list:
        html = html + character.name + " || " + character.date_of_birth +"<br>"
    return HttpResponse(html)

def puntoDiez(request):
    list = PowerCharacter.objects.select_related('cha').filter(~Q(pow__name='Volar'))
    html = ""
    for character in list:
        html = html + character.cha.name + " |" + character.pow.name + "<br>"
    return HttpResponse(html)





