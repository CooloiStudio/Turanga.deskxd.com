from django.shortcuts import render
from django.views import generic
from models import *
from django.http import HttpResponse, HttpResponseRedirect

class IndexViews(generic.View):
    templates_file = 'testing.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)