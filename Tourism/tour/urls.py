from django.urls import path
from .views import homepage
from . import views

urlpatterns = [
    path('', homepage, name='index'),
    path('Zoo/', views.Zoo, name='Zoo'),
    path('Palace/', views.Palace, name='Palace'),
    path('Hills/', views.Hills, name='Hills'),
    path('Gardens/', views.Gardens, name='Gardens'),
    # path('feedback/', views.feedback, name='feedback'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('devs/', views.DEVS, name='devs'),
    path('devs/devs2/', views.DEVS2, name='devs2'),
]