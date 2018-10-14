# in employee homescreen in for write method = 'GET'
# and name= 'q'
# and value = '{{ request.GET.q }}'
from django.contrib.postgres.search import SearchQuery,SearchVector

query = request.GET.get ("Vehicle_entered")
if query:
    queryset_list = queryset_list.filter(title_icontains=query)


query2 = request.GET.get ("customer_search")
if query2:
    queryset_list = queryset_list.filter(title_icontains=query2)