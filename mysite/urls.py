"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.api.urls')),
]



# from django.db import models
# from django.utils.translation import gettext_lazy as _

# class Book(models.Model):
#     name = models.CharField(_('Name'), max_length=150)
#     title = models.CharField(_('Title'), max_length=50)
#     excerpt = models.TextField(_('Excerpt'))
    
    
#     def __str__(self):
#         return self.title + " by " + self.name

# # class Books(models.Model):
# #     name = models.CharField(max_length=150)
# #     title = models.CharField(max_length=50)
# #     excerpt = models.TextField()
    
# #     def __str__(self):
# #         return self.title + " by " + self.name
