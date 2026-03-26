from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studentlist/', views.student_details, name='student_details'),
    path('studentlist/<int:id>/', views.student_detail_view),
]