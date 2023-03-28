from django.shortcuts import render
from django.http import HttpResponse

from web.forms import DjangoTemplateForm
from web.maker import make_template


def template(request, meta):
    context = {}
    Form = meta['form']
    cookiecutter_path = meta['cookiecutter_path']
    page = meta['page']
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            file = make_template(form.cleaned_data, cookiecutter_path)
            response = HttpResponse(file, content_type='application/zip')
            filename = form.cleaned_data['project_name'] + '-' + form.cleaned_data['app_service_name']
            response['Content-Disposition'] = f'inline; filename={filename}.zip'
            return response
    else:
        form = Form()
        context['form'] = form
    return render(request, page, context)


def django(request):
    meta = {
        'form': DjangoTemplateForm,
        'cookiecutter_path': 'django-template',
        'page': 'web/index.html'
    }
    return template(request, meta)
