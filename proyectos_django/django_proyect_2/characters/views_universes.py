from django.http import HttpResponse
from django.shortcuts import render, redirect
from characters.models import Universe

def list(request):
    list = Universe.objects.all()
    return render(request, 'universes/index.html', {"list":list})


def save(request):
    if request.method == "GET":
        return render(request, 'universes/save.html')
    name_ = request.POST['name']
    description_ = request.POST['description']
    foundation_ = request.POST['foundation']
    universe = Universe(
        name=name_,
        description=description_,
        foundation=foundation_
    )
    universe.save()
    return redirect('characters:list_universes')

def detail(request, id):
    oneUniverse = Universe.objects.get(id=id)
    return render(request, 'characters/detail.html', {"universe":oneUniverse})
