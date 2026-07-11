"""
URL configuration for hacknestpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from accounts.views import login_view, signup_view, orilogin_view, studenthome_view, otp_verify_view, profile_view, admin_view, get_chat_messages, send_chat_message


def home(request):
    return render(request, 'home.html')


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('orilogin/', orilogin_view, name='orilogin'),
    path('studenthome/', studenthome_view, name='studenthome'),
    path('otp-verify/', otp_verify_view, name='otp_verify'),
    path('profile/', profile_view, name='profile'),
    path('admin-view/', admin_view, name='admin_view'),
    path('studenthome/chat/send/', send_chat_message, name='send_chat_message'),
    path('studenthome/chat/messages/<int:team_id>/', get_chat_messages, name='get_chat_messages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




