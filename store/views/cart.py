from django.shortcuts import render
from django.views import View
from store.models.product import Products

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        ids = list(cart.keys())
        products = Products.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})
