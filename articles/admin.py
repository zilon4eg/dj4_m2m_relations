from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.contrib import admin
from .models import Tag, Article, TagScope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        all_tag_count = list(form.cleaned_data['tag'].id for form in self.forms if form.cleaned_data)
        main_tag_count = list(form.cleaned_data['tag'].id for form in self.forms if form.cleaned_data if form.cleaned_data['is_main'] is True)

        if len(main_tag_count) > 1:
            raise ValidationError('Основной раздел может быть только один!')

        if len(all_tag_count) > 0 and len(main_tag_count) < 1:
            raise ValidationError('Должен быть хотябы один основной раздел!')

        if len(all_tag_count) != len(set(all_tag_count)):
            raise ValidationError('Ошибка: Два одинаковых раздела!')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = TagScope
    formset = ScopesInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline]
