from django.contrib import admin
from .models import LikeCount

# Register your models here.
@admin.register(LikeCount)
class LikesAdmin(admin.ModelAdmin):
	list_display=('liked_num',)