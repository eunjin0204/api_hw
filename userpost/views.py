from django.shortcuts import render
from userpost.models import UserPost, Album, Files
from userpost.serializer import UserSerializer, AlbumSerializer, FileSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body') # 튜플(끝에 , 찍어야)

    def get_queryset(self):
        # 이 내부에서 쿼리셋을 처리하고 리턴
        qs = super().get_queryset()

        if self.request.user.is_authenticated: # 지금 요청 보낸 유저가 등록된 유저라면(로그인 되어있다면)
            qs = qs.filter(author = self.request.user) # author = 지금 http request를 보낸 그 유저
        else:
            qs = qs.none()
        
        return qs

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)