from products.models import RequestProduct


def requested_items(request):
    req_items = RequestProduct.objects.all()
    return {'req_items': req_items, 'test': test}