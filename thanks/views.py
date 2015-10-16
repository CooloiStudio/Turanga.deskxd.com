from django.shortcuts import render
from django.views import generic

class IndexViews(generic.View):
    templates_file = 'thanksIndex.html'

    def get(self, request):

        context = {}

        return render(request,
                      self.templates_file,
                      context)