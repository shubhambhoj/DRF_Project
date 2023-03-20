from rest_framework.pagination import CursorPagination

class MyCustomPagination(CursorPagination):
    page_size=5
    cursor_query_param='cu'
    ordering='name'