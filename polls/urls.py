from django.urls import path

from . import views

from .views import rate_site

urlpatterns = [
     path("", views.index, name="index"),
     path('rate/', rate_site, name='rate_site'),
     path('polls/', views.polls_view, name='polls'),
]



