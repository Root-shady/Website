from django.contrib import admin
from blog.models import Post, Tag, Category

# Setting the format of the models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name', 'related_post', 'create_date','slug']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ['post_id', 'title','status','category','author','publish_date','slug', 'image_link']
    #fieldsets = [
    #        ('Author', {'fields':['author']}),
    #        ('Post information', {'fields':['post_id','title', 'category', 'publish_date','slug','status','abstract'], "classes":['collapse']} ),
    #        ]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'frequence','slug']
# Register your models here.


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
