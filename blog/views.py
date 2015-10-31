from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Tag, Category, Post

# Create your views here.

# Create the home page of the blog
def index(request):
    context_dict = common()
    post_list = Post.objects.order_by('publish_date')
    context_dict['posts'] = post_list
    return render(request, 'blog/index.html', context_dict)

# Return the Tags and the Categories
def common():
    # Create the tag cloud in the index page
    tag_list = Tag.objects.order_by('frequence')
    # List all the category in the side bar
    category_list = Category.objects.order_by('name')
    context_dict = {
            'tags': tag_list,
            'categories': category_list,
            }
    return context_dict


# Create a page for different categories
def category(request, category_name_slug):
# create a context dictionary which we can pass to the template rendering engine
    context_dict = common()
    try:
        # If we find a category name slug with the given name?
        # Otherwise the get() method raise a DoseNotExist exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        # Retrieve all the associated pages
        # Note that filter returns >= 1 model instance
        posts_list = Post.objects.filter(category=category)


        # Cannot find another good way to do this. Mark here for better improvement
# create another class that contain the result of the post query
# in order to add the tags field in the result
        class Append_tag():
            pass
        result = []
        for post in posts_list:
            add_tag = Append_tag()
# Add the tags object 
            add_tag.tags = Tag.objects.filter(post = post.post_id)
# add the original post object
            add_tag.post = post
            result.append(add_tag)
        
        context_dict['category'] = category
        posts_list = result

    except Category.DoesNotExist:
        pass

    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # if the page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context_dict['posts'] = posts
    return render(request, 'blog/category.html', context_dict)

def about(request):
    blog = '<a href="/blog">Blog Home Page</a>'
    return HttpResponse("This is the about section" + blog)

