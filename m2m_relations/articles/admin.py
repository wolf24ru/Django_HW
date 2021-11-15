from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, ArticleTag, Article


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_list = [form.cleaned_data.get('is_main') for form in self.forms]
        if 1 < main_list.count(True) or main_list.count(True) <= 0:
            raise ValidationError('Должен быть только один главный тег')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
