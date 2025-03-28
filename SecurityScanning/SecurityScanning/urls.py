"""LoginPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Security import views

urlpatterns = [
    # superuser:
    path("admin/", admin.site.urls),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('placement/', views.PlacementPage, name='placement'),
    path('query/', views.query),
    path('submitedQuery/', views.submitedQuery, name='submitedQuery'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('', views.SignupPage, name='signup')
]