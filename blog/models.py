from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    frequence = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class Post(models.Model):
    # A primary key field will automatically be added to your model, if you don't specify.
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    abstract = models.CharField(max_length=200)
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
    category= models.ForeignKey('Category')
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('category', 'publish_date')

    def __str__(self):
        return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

