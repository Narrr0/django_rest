from .models import Post
from .serializer import PostSerializer
from .pagination import Mypagination
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('id')
    serializer_class=PostSerializer
    pagination_class=Mypagination

