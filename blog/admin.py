from django.contrib import admin
from blog.models import blogPost,Category
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display=("title","published","date","last_updated")
    list_editable=("published",)

class CategoryBlogPostAdmin(admin.ModelAdmin):
    # list_display=("title",)
    # list_editable=("title",)
    pass

admin.site.register(Category,CategoryBlogPostAdmin)
admin.site.register(blogPost,BlogPostAdmin)