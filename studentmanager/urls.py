"""studentmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app.student.views import StudentCreate, StudentList, StudentUpdate, StudentDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", StudentList.as_view(), name='index'),
    path("CreateStudent/", StudentCreate.as_view(), name="CreateStudent"),
    path("UpdateStudent/<int:pk>/", StudentUpdate.as_view(), name="UpdateStudent"),
    path("DeleteStudent/<int:pk>/", StudentDelete.as_view(), name="DeleteStudent"),
]
