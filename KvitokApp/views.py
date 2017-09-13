from django.shortcuts import render, get_object_or_404, redirect
from KvitokApp.models import ZapisTable
from KvitokApp.forms import KvitokAddForm
#эксперемент
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
# Функция представления главной страницы

def home(request):
    kvitki = ZapisTable.objects.all() # Запрос к базе на получение всех объектов
    return render(request, 'home.html', {'kvitki': kvitki})

def kvitok_base(request):
    kvitki = ZapisTable.objects.all()
    return render(request, 'kvitok_base.html', {'kvitki': kvitki})

def kvitok_detail(request, kvitok_id):
    kvitok = get_object_or_404(ZapisTable, id=kvitok_id)
    return render(request, 'kvitok_detail.html', {'kvitok': kvitok})

def kvitok_add(request):
    form = KvitokAddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'kvitok_add.html', {
        'form': form
    })
