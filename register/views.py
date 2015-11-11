from django.shortcuts import render
from django.views import generic
from models import *


class IndexViews(generic.View):
    templates_file = 'registerIndex.html'

    def get(self, request):

        context = {
        }

        return render(request,
                      self.templates_file,
                      context)


class AgreeViews(generic.View):
    templates_file = 'agreement.html'

    def get(self, request):

        agreements = list(Agreement.objects.all())
        if agreements:
            agrees = agreements.pop()
        else:
            agrees = ""

        context = {
            'agrees': agrees
        }

        return render(request,
                      self.templates_file,
                      context)