from django import forms
from django.contrib import admin

from models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ['content', 'slug']


class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'markdown_content')


admin.site.register(Entry, EntryAdmin)
