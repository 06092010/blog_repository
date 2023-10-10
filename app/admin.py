from django.contrib import admin
from .models import ProfileData, About, SocialLink, Tools, Service, Project, Category, Post, Tag, PostCategorys
# Register your models here.

admin.site.register(ProfileData)
admin.site.register(About)
admin.site.register(SocialLink)
admin.site.register(Tools)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(PostCategorys)
admin.site.register(Category)
admin.site.register(Tag)
from .models import ProfileData, SocialLink, Service, About, Post, PostCategorys, Project, Tag, Tools, Category

# @admin.register(ProfileData)
# class ProfileDataAdmin(admin.ModelAdmin):
#     list_display = ('id', 'full_name', 'image', 'bio')
#     list_display_links = ('full_name',)

# @admin.register(SocialLink)
# class SocialLinkAdmin(admin.ModelAdmin):
#     list_display = ('url', 'name', 'icon', 'order')
#     list_display_links = ('name', 'url', 'icon')
#     search_fields = ('name', 'url')

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'category', 'tags', 'body', 'short_description')
#     list_display_links = ('image',)
#     search_fields = ('name',)


# @admin.register(Tools)
# class ToolsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'percemtage', 'order')
#     list_display_links = ('title',)
#     search_fields = ('title',)


# @admin.register(About)
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ('bio', 'projects', 'money', 'valuenteers')
    

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'category')
#     list_display_links = ('name',)
    

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('icon', 'name', 'description')
#     list_display_links = ('name',)
#     search_fields = ('name',)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)

# @admin.register(PostCategorys)
# class PostCategorysAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)


