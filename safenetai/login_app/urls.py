
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls.static import static


app_name = 'login_app'
urlpatterns = [
    
    path('login_page/', views.login_page, name='login_page'),
    path('user_login/', views.user_login, name='user_login'),
    path('index/', views.index, name='index'),
    # path('user_logout/', views.user_logout, name='user_logout'),
    path('register_view/', views.register_view, name='register_view'),
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)