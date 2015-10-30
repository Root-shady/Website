from django.shortcuts import render
from blog.models import Tag

# Create your views here.
def index(request):
    tag_list = Tag.objects.order_by('frequence')
    context_dict = {
            'tags': tag_list,
            }
    return render(request, 'blog/index.html', context_dict)
def about(request):
    blog = '<a href="/blog">Blog Home Page</a>'
    return HttpResponse("This is the about section" + blog)

