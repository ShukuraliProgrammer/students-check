from django.contrib import admin
from .models import StudentUser, Profile, Lesson, Post, PhotoModel, AboutProject, UsefulLink


@admin.register(StudentUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'group', 'degree']
    list_filter = ('first_name', 'group', 'last_name', 'degree')
    search_fields = ('username', 'email', 'group')


@admin.register(Profile)
class StudentProfile(admin.ModelAdmin):
    list_display = ('user', 'age', 'photo', 'phone')


admin.site.register(Lesson)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ['title', ]}
    raw_id_fields = ('author',)

    ordering = ('status', 'publish')


@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutProject)
class AboutProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    pass
