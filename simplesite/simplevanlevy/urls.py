from django.urls import path
from simplevanlevy.views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
