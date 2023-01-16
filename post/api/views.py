from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from django.shortcuts import render,HttpResponse

class PostApiViewSet(ModelViewSet):
    serializer_class=PostSerializer
    queryset= Post.objects.all()

def genIp(request):
    ipl=Post.objects.get()
    iplg= '.'.join(ipl)
    return HttpResponse(iplg)