from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dealer/<int:dealer_id>/', views.dealer_details, name='dealer_details'),
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),
    path('sentiment/', views.sentiment_analyzer, name='sentiment_analyzer'),
    path('car-makes/', views.car_makes, name='car_makes'),
    path('car-models/', views.car_models, name='car_models'),
]
