from django.shortcuts import render
# Create your views here.
from .models import Man


def first_page(request):
    men = Man.objects.all()
    context = {'men': men}
    return render(request, 'first_page.html', context)