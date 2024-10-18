from django.http import HttpResponse
from django.template import loader

def blog_index(request):
    template = loader.get_template('blog_index.html')
    return HttpResponse(template.render())

def blog_post(request):
    template = loader.get_template('blog_post.html')
    return HttpResponse(template.render())