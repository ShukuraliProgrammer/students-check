from django.contrib import admin

from .models import StudentUser, Profile, Lesson, Post


# Register your models here.
@admin.register(StudentUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'gruh', 'kursi']
    list_filter = ('first_name', 'gruh', 'last_name', 'kursi')
    search_fields = ('username', 'email', 'gruh')


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
