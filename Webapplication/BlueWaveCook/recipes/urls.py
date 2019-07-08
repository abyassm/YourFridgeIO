from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('recipes/', views.recipes, name='recipes'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('footer/', views.footer, name='footer'),
    path('logout/', views.logout_user, name='logout'),
]
