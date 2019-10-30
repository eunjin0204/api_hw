from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    PAGE_SIZE = 3