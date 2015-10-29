from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {
                'boldmessage' : 'I am being transform!!!',
            }
    return render(request, 'blog/index.html', context_dict)
def about(request):
    blog = '<a href="/blog">Blog Home Page</a>'
    return HttpResponse("This is the about section" + blog)

