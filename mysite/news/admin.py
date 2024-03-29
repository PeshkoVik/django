from django.contrib import admin

# Register your models here.


from .models import News, Category

class NewsAdmin(admin.ModelAdmin) :
  list_display = ('id', 'title','category', 'created_at', 'updated_at', 'is_publish')
  list_display_links = ('id', 'title')
  search_fields = ('title', 'content')
  list_editable =('is_publish',)
  list_filter = ('is_publish', 'category')

class CategoryAdmin(admin.ModelAdmin) :
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')
  search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)