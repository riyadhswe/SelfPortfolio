from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    portfoliodata = Portfolio.objects.all()[0]
    Imagedata = Image.objects.all()
    contex = {
        'p': portfoliodata,
        'i': Imagedata
    }

    if request.method == 'POST':  # For Insert Data
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contactdata = Contact(name=name, email=email, description=description)
        contactdata.save()
    return render(request, 'index.html', contex)
