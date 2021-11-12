from django.shortcuts import redirect, render
from wines.models import Wine

def list(request):
    print(request.method)
    list = Wine.objects.all()
    return render(request, 'wines/index.html', {"list":list})

def save(request):
    if request.method == "GET":
        return render(request, 'wines/save.html')
    name_ = request.POST['name']
    score_ = request.POST['score']
    price_ = request.POST['price']
    wine = Wine(
        name=name_,
        score=score_,
        price=price_
    )
    wine.save()
    return redirect('wines:list_wines')

