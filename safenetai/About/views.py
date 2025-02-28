from django.shortcuts import render
from django.http import HttpResponse

from About.models import TeamMembers
from About import forms

# Create your views here.

def about_us(request):
    team_list=TeamMembers.objects.order_by('first_Name')
    # Researchers_list=researcher_form.objects.get(pk=researcher_id)
    diction={'title':'Home Page','team_list':team_list}
    return render(request, "about_us/about.html", context=diction)

def index(request):
    return render(request, "about_us/about.html")


def home(request):
    return render(request, "home/home.html")



def team_info_form(request):
    new_form = forms.team_form_Details()

    if request.method == 'POST':
        new_form = forms.team_form_Details(request.POST, request.FILES)

        if new_form.is_valid():
            new_form.save(commit=True)
            return about_us(request)
        else:
            print('ERROR FORM INVALID', new_form.errors)
    dict1 = {'test_form': new_form, 'heading': 'Add New teammate'}

    return render(request, 'about_us/teaminfo_form.html', context=dict1)


 #info_form show

# def team_member_view(request):
#     team_list=TeamMembers.objects.order_by('first_Name')
#     # Researchers_list=researcher_form.objects.get(pk=researcher_id)
#     diction={'title':'Home Page','team_list':team_list}
#     return render(request, 'about_us/teaminfo_show.html', context=diction)
