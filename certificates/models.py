#encoding: utf-8

import os
import StringIO

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.files.base import ContentFile

from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4, LETTER, landscape, portrait, letter
from reportlab.lib.units import inch, cm


class Enrollment(models.Model):

    name = models.CharField(verbose_name=u'Nome', max_length=100)
    email = models.EmailField(verbose_name=u'E-mail')
    cpf = models.CharField(verbose_name=u'CPF', blank=True, max_length=14)
    certificate = models.FileField(
        verbose_name=u'Certificado',
        upload_to='certificates'
    )
    created_on = models.DateTimeField(
        verbose_name=u'Criado em', 
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        verbose_name=u'Atualizado em', 
        auto_now=True
    )

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, self.email)


    class Meta:
        verbose_name = u'Inscrição'
        verbose_name_plural = u'Inscrições'


def pre_save_enrollment(signal, sender, instance, **kwargs):
    images_path = os.path.join(settings.PROJECT_DIR, 'static_files', 'img')
    signature_path = os.path.join(images_path, 'signature.jpg')
    logo_path = os.path.join(images_path, 'cert_logo.png')
    context = {
        'enrollment': instance, 
        'domain': Site.objects.get_current().domain,
        'signature_path': signature_path,
        'logo_path': logo_path,
    }
    certificate_txt = render_to_string('certificates/certificate.txt', context)

    elements = []
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name='Justify', alignment=TA_JUSTIFY, fontSize=16, leading=22
        )
    )

    elements.append(Spacer(1, 16))
    paragraphs = certificate_txt.split("\n")
    for p in paragraphs:
        if p.strip():
            elements.append(Paragraph(p, styles['Justify']))
            elements.append(Spacer(1, 16))

    output = StringIO.StringIO()
    doc = SimpleDocTemplate(output, topMargin=3 * cm, bottomMargin=0)
    doc.pagesize = landscape(A4)
    doc.build(elements)

    filename = u'{0}.pdf'.format(instance.name)
    pdf = output.getvalue()
    instance.certificate.save(filename, ContentFile(pdf), save=False)

models.signals.pre_save.connect(
    pre_save_enrollment, sender=Enrollment, dispatch_uid='pre_save_enrollment',
)