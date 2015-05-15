from django.conf.urls import include, url, patterns
from products.views import product, add_request, requested

urlpatterns = [
    url(r'^(\d+)/$', product),
    url(r'^requested/$', requested, name='requested'),
    url(r'^/(?P<product_id>\d+)/$', add_request, name='add'),
]