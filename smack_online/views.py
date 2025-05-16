from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect
from django.conf import settings

from .forms import SmackForm

import random
import pandas as pd
import os

random.seed()

class Index(FormView):
    template_name = 'index.html'
    form_class = SmackForm

    def form_valid(self, form):
        level = self.request.POST.get("smack_level")
        df = pd.read_csv(os.path.join(settings.BASE_DIR, 'slaps.csv'), delimiter=',', quotechar='*')
        smack = df[f'Level {level}'][random.randint(0, 85)]
        return redirect('smack:dashboard', id=smack)
    
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'