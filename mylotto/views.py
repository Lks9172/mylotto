from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
# Create your views here.
from mylotto.forms import PostForm
from mylotto.models import GuessNumbers


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'mylotto/defalut.html', {'lottos': lottos})

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=True)
            lotto.generate()
            lotto.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'mylotto/form.html', {'form': form})

def detail(request, pk):
    lotto = GuessNumbers.objects.get(pk = pk)
    return render(request, 'mylotto/detail.html', {'lotto' : lotto})

