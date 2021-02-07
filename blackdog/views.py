from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Bark
from .forms import BarkForm


def index(request):
    return render(request, 'index.html')


def bark(request, bark_id):
    bark = get_object_or_404(Bark, pk=bark_id)
    bark.views = bark.views + 1 
    bark.save()
    return render(request, "bark.html", {"bark": bark})


def new(request):
    if request.method == 'POST':
        bark_form = BarkForm(request.POST)
        if bark_form.is_valid():
            bark = bark_form.save(commit=False)
            bark.author = request.user
            bark.save()
            return HttpResponseRedirect(reverse('blackdog:bark', args=(bark.id,)))
    else:
        bark_form = BarkForm()
    return render(request, 'new.html', {'form': bark_form})


def edit(request, bark_id):
    bark = Bark.objects.get(pk=bark_id)
    if bark.author != request.user:
        return HttpResponse('Forbidden', status=403)

    if request.method == 'POST':
        bark_form = BarkForm(request.POST)
        if bark_form.is_valid():
            bark.content = bark_form.cleaned_data['content']
            bark.save()
    else:
        bark_form = BarkForm(instance=bark)
    return render(request, 'new.html', {'form': bark_form})
