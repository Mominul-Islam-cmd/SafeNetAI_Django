from django.shortcuts import render
from login_app.forms import UserForm, UserInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from login_app.models import UserInfo
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




# last_login_user
# @login_required
# def last_login_user(request):
#     last_login = None
#     if request.user.is_authenticated:
#         last_login = request.user.last_login

#     return render(request, 'login_app/login_user_show.html', {'last_login': last_login})



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



# Create login_users views here.
# def login_users(request):
#     dict = {}
#     if request.user.is_authenticated:
#         current_user = request.user
#         user_id = current_user.id
#         user_basic_info = User.objects.get(pk=user_id)
#         try:
#             user_more_info = UserInfo.objects.get(user__pk=user_id)
#         except UserInfo.DoesNotExist:
#             user_more_info = None

#         dict = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}
#     return render(request, "login_app/login_user_show.html", context=dict)

#register viewer



def login_users(request):
    users = User.objects.all()
    users_info = UserInfo.objects.all()

    context = {
        'users': users,
        'users_info': users_info,
    }

    return render(request, 'login_app/login_user_show.html', context)
