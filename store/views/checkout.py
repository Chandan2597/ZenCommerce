from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products
from django.conf import settings

class CheckOut(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')

        customer_id = request.session.get('customer')
        if not customer_id:
            return redirect('login')

        products = Products.get_products_by_id(list(cart.keys()))
        total = sum(product.price * cart[str(product.id)] for product in products)

        return render(request, 'checkout.html', {
            'products': products,
            'cart': cart,
            'total': total,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID
        })
