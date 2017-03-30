from django.conf.urls import url
from longclaw.longclawshipping import api
from longclaw.settings import API_URL_PREFIX

address_list = api.AddressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
address_detail = api.AddressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(API_URL_PREFIX + r'addresses/$',
        address_list,
        name='longclaw_address_list'),
    url(API_URL_PREFIX + r'addresses/(?P<pk>[0-9]+)/$',
        address_detail,
        name='longclaw_address_detail'),
    url(API_URL_PREFIX + r'shipping/cost/$',
        api.shipping_cost,
        name='shipping_cost'),
    url(API_URL_PREFIX + r'shipping/countries/$',
        api.shipping_countries,
        name="shipping_countries")
]
