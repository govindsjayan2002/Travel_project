from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Place
from .models import Team

#place
def demo(request):
    obj=Place.objects.all()
    a = Team.objects.all()
    return render(request, 'index.html', {'result':obj,'home':a})



