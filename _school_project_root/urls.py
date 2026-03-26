"""
URL configuration for school project.

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
from django.urls import path, include
from professors import views
from rest_framework.routers import DefaultRouter
from result import views as res_views

router = DefaultRouter()
router.register('professors', views.ProfessorViewSet, basename='professor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # for func based views
    # path('professors/', views.Professor.as_view()), # for class based views
    # path('professors/<int:id>', views.ProfessorDetails.as_view())

    path('', include(router.urls)),

    path('result/', res_views.ResultView.as_view()),
    path('marksheet/', res_views.MarkSheetView.as_view()),

    path('library/', include('library.urls')),
]
