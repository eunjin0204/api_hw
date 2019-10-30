from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title',) # 튜플(끝에 , 찍어야)

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