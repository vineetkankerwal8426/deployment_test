from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='tasks'),
    path('about/',views.aboutPageView.as_view()),
]
