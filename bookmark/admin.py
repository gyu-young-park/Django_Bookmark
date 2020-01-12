from django.contrib import admin
from .models import Bookmark

#여기서 모델에 대한 테스트를 진행할 수 있다.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["id","site_name","url"]

admin.site.register(Bookmark,BookmarkAdmin)