#encoding: utf-8

from django import forms

from .models import Enrollment


class SearchEnrollmentForm(forms.Form):

    cpf = forms.CharField(label=u'CPF')
    email = forms.EmailField(label='E-mail')

    def __init__(self, *args, **kwargs):
        super(SearchEnrollmentForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'pure-input-1-3'
        self.fields['email'].widget.attrs['class'] = 'pure-input-1-3'

    def enrollments(self):
        return Enrollment.objects.filter(
            cpf=self.cleaned_data['cpf'], email=self.cleaned_data['email']
        )