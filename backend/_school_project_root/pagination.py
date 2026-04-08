# Custom Pagination (create in root and use anywhere by importing)

from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size=3
    page_size_query='size'
    max_page_size=10