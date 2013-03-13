from contact.forms import ContactForm
from django.views.generic import CreateView, TemplateView
from django.contrib import messages


class IndexView(CreateView):
    form_class = ContactForm
    template_name = "index.html"
    success_url = '/'

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, u'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(*args, **kwargs)


class CallForPapersView(TemplateView):
    template_name = "callforpapers.html"
