#encoding: utf-8

from django.views.generic import TemplateView
from core.models import Sponsor
from schedule.models import Slot


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
        context['first_day_slots'] = Slot.objects.filter(
            time__day='24'
        ).order_by('time')
        context['second_day_slots'] = Slot.objects.filter(
            time__day='25'
        ).order_by('time')
        return context


class CallForPapersView(TemplateView):

    template_name = "callforpapers.html"
