from django.views.generic import TemplateView
from django.conf import settings

import random
import pandas as pd
import os

class ForgotView(TemplateView):
    template_name = 'forgot.html'
    
class SmackView(TemplateView):
    template_name = 'smack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['smack'] = self.kwargs['id']
        return context
    
class ClickView(TemplateView):
    template_name = 'click.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        df = pd.read_csv(os.path.join(settings.BASE_DIR, 'affection.csv'), delimiter=',')
        smack = df[f'items'][random.randint(0, 200)]
        context['smack'] = smack
        return context



