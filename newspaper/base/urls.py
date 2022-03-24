from django.urls import path
from . import views
 
urlpatterns=[ 
    path('',views.home,name="HOME"),
    path('summarize/general/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/business/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/health/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/sports/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/entertainment/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/science/<str:pk>',views.summarize,name="summarizer"),
    path('summarize/technology/<str:pk>',views.summarize,name="summarizer"),



]