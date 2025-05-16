from django.views.generic import TemplateView

# Create your views here.
class SmackView(TemplateView):
    template_name = 'smack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['smack'] = self.kwargs['id']
        return context

class ForgotView(TemplateView):
    template_name = 'forgot.html'

