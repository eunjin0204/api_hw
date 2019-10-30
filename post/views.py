from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from post.pagination import MyPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination


# 액션은 GET이 기본, 바꾸려면 @action(method=['post'])
#    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) #커스터마이징
#    def highlight(self, request, *args, **kwargs):
#        post = self.get_object()
#        return Response(post.highlighted)
#
#    def hi(self, request, *args, **kwargs):
#        return HttpResponse("안녕?")