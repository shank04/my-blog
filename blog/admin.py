from django.contrib import admin
from .models import Post
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


# class EntryAdmin(MarkdownModelAdmin):
#    list_display = ("title", "created")
#     #populated_fields = {"slug": ("title",)}
#     # Next line is a workaround for Python 2.x
#     formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(Post)
