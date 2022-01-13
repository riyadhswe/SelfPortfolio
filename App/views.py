from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    portfoliodata = Portfolio.objects.all()
    imagedata = Image.objects.all()
    pdfdata = Pdf.objects.all()
    workdata = Work.objects.all()
    skilldata = Skills.objects.all()
    socialdata = Social.objects.all()
    contex = {
        'p': portfoliodata,
        'i': imagedata,
        'pdf': pdfdata,
        'work': workdata,
        'Skills': skilldata,
        'social': socialdata,
    }

    if request.method == 'POST':  # For Insert Data
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contactdata = Contact(name=name, email=email, description=description)
        contactdata.save()

    return render(request, 'index.html', contex)
