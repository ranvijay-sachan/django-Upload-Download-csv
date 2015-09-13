__author__ = 'ranvijay'

from django import forms

class UploadCsvForm(forms.Form):
    title = forms.CharField()
    city = forms.CharField()
    upload_file = forms.FileField()