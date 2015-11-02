from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Tag, Category, Post

# Create your views here.

# Create the home page of the blog
def index(request):
    context_dict = common()
    post_list = Post.objects.order_by('publish_date')

    # Adding the category of the post, bundle the post object and the category object together.
    class Append_category():
        pass
    result = []
    for post in post_list:
        add_category = Append_category()
        add_category.post = post
# Retreive the category of the post(FK)
        add_category.category = Category.objects.filter(post__post_id=post.category_id)[0]
        result.append(add_category)
    post_list = result

    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context_dict['posts'] = posts
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
        # Otherwise the get() method raise a DoesNotExist exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        # Retrieve all the associated pages
        # Note that filter returns >= 1 model instance
        posts_list = Post.objects.filter(category__category_id=category.category_id)


        # Cannot find another good way to do this. Mark here for better improvement
# create another class that contain the result of the post query
# in order to add the tags field in the result
        class Append_tag():
            pass
        result = []
        for post in posts_list:
            add_tag = Append_tag()
# Add the tags object 
            add_tag.tags = Tag.objects.filter(post__post_id = post.post_id)
# add the original post object
            add_tag.post = post
            result.append(add_tag)
        
        context_dict['category'] = category
        posts_list = result

    except Category.DoesNotExist:
        return render(request, 'common/404.html')

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

def tags(request, tag_name_slug):
    context_dict = common()
    try:
        tag = Tag.objects.get(slug=tag_name_slug)
        posts_list = Post.objects.filter(tags__tag_id = tag.tag_id)
        context_dict['tag'] = tag
    except (Tag.DoesNotExist, Post.DoesNotExist):
        pass
    class Append_category():
        pass

    result = []
    for post in posts_list:
        add_category = Append_category()
        add_category.category = Category.objects.get(post__post_id = post.post_id)
        add_category.tags = Tag.objects.filter(post__post_id=post.post_id)
        add_category.post = post
        result.append(add_category)

    posts_list = result
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
    return render(request, 'blog/tags.html', context_dict)

def single_post(request, category_name_slug, post_title):
    context_dict = common()
    try:
        post = Post.objects.get(slug=post_title)
        category = Category.objects.get(slug=category_name_slug)
        post_list = Post.objects.filter(category__category_id=category.category_id).order_by('post_id')
    except (Post.DoesNotExist, Category.DoesNotExist):
        pass#404 here
# To check if there are next page or previus page. Not related to the category
# Turn the queryset into a list, in order to use the index method.
    post_list = list(post_list)
    condition = {}
    prev, next = True, True
    if post.post_id == post_list[0].post_id:
        prev = False
    if post.post_id == post_list[len(post_list)-1].post_id:
        next = False
    if prev:
        condition['has_pre'] = prev
        condition['pre_slug'] = post_list[post_list.index(post)-1].slug
    if next:
        condition['has_next'] = next
        condition['next_slug'] = post_list[post_list.index(post)+1].slug

    context_dict['category'] = category_name_slug
    context_dict['condition'] = condition
    context_dict['post'] = post
    return render(request, 'blog/post.html', context_dict)

    
def about(request):
    blog = '<a href="/blog">Blog Home Page</a>'
    return HttpResponse("This is the about section" + blog)

