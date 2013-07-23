#encoding: utf-8

from django.contrib import admin
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from .models import Enrollment


class EnrollmentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'created_on', 'updated_on')
    search_fields = ('name', 'email',)
    exclude = ('certificate',)

    actions = ['send_mail']

    def send_mail(self, request, queryset):
        subject = u'Certificado de Participação Python Nordeste 2012'
        for enrollment in queryset:
            context = {'enrollment': enrollment}
            message = render_to_string('certificates/email.txt', context)
            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL,
                [enrollment.email])
            certificate_file = default_storage.open(enrollment.certificate.name)
            email.attach('certificado.pdf', certificate_file.read())
            email.send()
        self.message_user(request, u'E-mail enviado com sucesso')
    send_mail.short_description = u'Enviar e-mail para selecionado(s)'

admin.site.register(Enrollment, EnrollmentAdmin)