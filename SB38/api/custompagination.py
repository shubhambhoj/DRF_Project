from rest_framework.pagination import PageNumberPagination

class MyCustomPagination(PageNumberPagination):
    page_size=5
    # page_query_param='pg'
    # page_size_query_param='records'
    # max_page_size=7
    # last_page_strings='end'         # or 'bottom'