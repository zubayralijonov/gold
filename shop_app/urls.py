from django.urls import path 

from . views import index_page, gold_main_page, gold_ring_page, gold_set_page, gold_braslet_page

urlpatterns = [
    path('', view=index_page),
    path('gold_main_page/', view=gold_main_page, name='gold_main_page'),
    path('gold_ring_page/', view=gold_ring_page, name='gold_ring_page'),
    path('gold_set_page/', view=gold_set_page, name='gold_set_page'),
    path('gold_braslet_page/', view=gold_braslet_page, name='gold_braslet_page'),
]