from django.contrib import admin
from post.models import Post, ipPost
# Register your models here.
@admin.register(Post)
class postIpAdmin(admin.ModelAdmin):
    list_display=['id','ip']
@admin.register(ipPost)
class listIP(admin.ModelAdmin):
    list_display=['direccion']