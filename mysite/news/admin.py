from django.contrib import admin
from .models import News, Category
# Register your models here.


# название настраивающего класа = название модели + Admin
class NewsAdmin(admin.ModelAdmin):
    # добавляем поля в админку для отображения
    list_display = ('id', 'title', 'created_at', 'updated', 'is_published', 'category')
    # добавляем какие ссылки будут кликабельными что бы открыть новость
    list_display_links = ('id', 'title')
    # по каким полям будет осущесвляться поиск
    search_fields = ('id', 'title', 'content')
    list_editable = ('is_published',)
    # добавляем боковой фильтр для сортировки
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    # добавляем поля в админку для отображения
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# регистрируем модель в админке
# второй параметр это клас отвечающий за отображение доп полей
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

