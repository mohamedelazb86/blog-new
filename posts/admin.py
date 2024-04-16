from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Category,Comment


class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','draft']
    list_filter=['draft']
    search_fields=['title']
    summernote_fields = ('content',)


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)

