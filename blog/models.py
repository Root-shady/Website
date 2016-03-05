from django.db import models
#from django.template.defaultfilters import slugify
from slugify import slugify

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
# Record the tag's frequence, add one when a post is related to that tag
    frequence = models.PositiveIntegerField(default=0)
    
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    # A primary key field will automatically be added to your model, if you don't specify.
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    abstract = models.CharField(max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)
    # 0 stands for public
    # 1 stands private or draft
    POST_ATTRIBUTES = (
                ('PL', 'Public'),
                ('PT', 'Private'),
                ('RT', 'Reprint'),
                ('DE', 'Debatable'),
            )
    status = models.CharField(max_length=2, choices=POST_ATTRIBUTES,default='PL')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    image_link = models.URLField(blank=True)
    category= models.ForeignKey('Category')
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        # The post is first add, instead of update 
        if not self.post_id:
            category = Category.objects.get(pk = self.category_id)
            category.related_post += 1
            category.save()
#            tags = Tag.objects.filter(post__post_id = self.post_id)
#            for tag in tags:
#                tag.frequence += 1
#                tag.save()
#
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
# Counting how many post are belong to the category 
    related_post = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name

