from django.shortcuts import render
from django.views import generic
from models import *

class AgreeViews(generic.View):
    templates_file = 'agreement.html'

    def get(self, request):

        agreements = list(Agreement.objects.all())
        if agreements:
            agrees = agreements.pop().content
        else:
            agrees = ""

        context = {
            'agrees': agrees
        }

        return render(request,
                      self.templates_file,
                      context)


class PrivacyViews(generic.View):
    templates_file = 'privacy.html'

    def get(self, request):

        privacys = list(Privacy.objects.all())
        if privacys:
            privacy = privacys.pop().content
        else:
            privacy = ""

        context = {
            'privacy': privacy
        }

        return render(request,
                      self.templates_file,
                      context)