from django.shortcuts import render

# Create your views here.

def guidelines_cards(request):
    return render (request, 'guidelines/gudielines_cards.html',context= {})


def ai(request):
    return render (request, 'guidelines/ai.html',context= {})


def data_analytics(request):
    return render (request, 'guidelines/DA.html',context= {})

def data_engineer(request):
    return render (request, 'guidelines/Data_engineer.html',context= {})


def research(request):
    return render (request, 'guidelines/researech.html',context= {})



