from django.contrib import admin

from .models import Post, Tag, TagPost, Comment


class TagInline(admin.TabularInline):
    """Добавление тегов в админку рецептов."""

    model = TagPost
    extra = 0

class PostAdmin(admin.ModelAdmin):
    
    inlines = (TagInline,)
    
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag)
admin.site.register(TagPost)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
        
        
