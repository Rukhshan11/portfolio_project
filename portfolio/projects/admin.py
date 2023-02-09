from django.contrib import admin

from .models import Job, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class JobAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)
admin.site.register(PostImage)

class PostImageAdmin(admin.ModelAdmin):
     pass

#     class PostImageAdmin(admin.StackedInline):
#     model = PostImage
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
#
#     class Meta:
#        model = Post
#
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass
