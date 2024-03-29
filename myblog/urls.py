"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import blog.views
import users.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('about/', blog.views.about, name='about'),
    path('contact/', blog.views.contact, name='contact'),
    path('post/<int:post_id>', blog.views.detail, name='detail'),
    path('newpost', blog.views.newpost, name='newpost'),
    path('post/<int:post_id>/newcomment', blog.views.newcomment, name='newcomment'),
    path('login/', users.views.login, name='login'),
    path('logout/', users.views.logout, name='logout'),
    path('signup', users.views.SignUpView.as_view(), name='signup'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
