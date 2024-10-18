from django.http import HttpResponse
from django.template import loader

def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())

def project_details(request):
    template = loader.get_template('project_details.html')
    return HttpResponse(template.render())