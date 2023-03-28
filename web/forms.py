from django import forms


class DjangoTemplateForm(forms.Form):
    project_name = forms.CharField(label='Project name', max_length=100)
    app_service_name = forms.CharField(label='AppService name', max_length=100)
