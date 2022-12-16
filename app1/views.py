from django.shortcuts import render, redirect
from app1.forms import CardForm
from app1.models import Card


def index(request):
    cards = Card.objects.all()
    return render(request, "app1/index.html", {'cards': cards})


def card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app1')
            except:
                pass
    else:
        form = CardForm()
    return render(request, 'app1/create.html', {'form': form})


def show(request, id):
    card = Card.objects.get(id=id)
    return render(request, "app1/show.html", {'card': card})


def create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('app1/show')
            except:
                pass
    else:
        form = CardForm()
    return render(request, 'app1/create.html', {'form': form})


def update(request, id):
    print('AAAAAAAAA')
    card = Card.objects.get(id=id)
    form = CardForm(request.POST, instance = card)
    if form.is_valid():
        print('BBBBBBBB')
        form.save()
        return redirect("/app1")
    return render(request, 'app1/edit.html', {'card': card})


def destroy(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    return redirect("/app1")
