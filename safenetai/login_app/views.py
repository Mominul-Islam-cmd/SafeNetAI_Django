from django.shortcuts import render
from login_app.forms import UserForm, UserInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.



#login
def login_page(request):
    
    return render(request, 'login_app/login.html',context= {})


#user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('About:about_us'))
                # return render(request, 'login_app/login.html',context= {})
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
                # return HttpResponseRedirect(reverse('login_app:login_page'))
        else:
            return HttpResponse("Someone tried to login and failed!")
      
    else:
       return HttpResponseRedirect(reverse('login_app:login_page'))
    #    return render(request, 'login_app/login.html',context= {})


def index(request):
    return render(request, 'login_app/index.html',context= {})

#log out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('About:about_us'))



#register
def register_view(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()

            registered = True


    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    dict={'user_form':user_form, 'user_info_form':user_info_form, 'registered': registered}

    return render(request, 'login_app/register.html',context= dict)
