from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# Index Portugues
from form import form

from core.models import Header


def home(request):
    success = False
    header = Header.objects.all()
    context = {
        'form': form,
        'success': success,
        'header': header,
    }
    return render(request, 'home/home.html', context)