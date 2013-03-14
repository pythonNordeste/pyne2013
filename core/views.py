#encoding: utf-8

from django.views.generic import CreateView, TemplateView
from django.contrib import messages

from core.models import Sponsor

class IndexView(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['gold_sponsors'] = Sponsor.objects.filter(
            type=Sponsor.GOLD_TYPE)
        context['silver_sponsors'] = Sponsor.objects.filter(
            type=Sponsor.SILVER_TYPE)
        context['bronze_sponsors'] = Sponsor.objects.filter(
            type=Sponsor.BRONZE_TYPE)
        return context


class CallForPapersView(TemplateView):
    
    template_name = "callforpapers.html"