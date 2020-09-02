from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        len_head_tags = len(
            [form.cleaned_data.get('tag').favorite 
            for form in self.forms 
            if form.cleaned_data.get('tag') is not None 
            and form.cleaned_data.get('tag').favorite])
        if len_head_tags == 0:
            raise ValidationError('Укажите основной раздел')
        if len_head_tags > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagInline(admin.TabularInline):
    model = Tag.article.through
    extra = 1
    formset = RelationshipInlineFormset
    verbose_name = 'Раздел'
    verbose_name_plural = 'Тематики Статьи'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (TagInline,)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # inlines = (TagInline,)
    list_display = ('name', 'favorite',)

