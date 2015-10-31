from django.contrib import admin
from blog.models import Post, Tag, Category

# Setting the format of the models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name', 'related_post', 'create_date','slug']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','category','author','publish_date','slug']
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'frequence','slug']
# Register your models here.


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
