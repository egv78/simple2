from django.shortcuts import render
from django.views.generic.base import TemplateView
import datetime


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'simplevanlevy/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        return context


