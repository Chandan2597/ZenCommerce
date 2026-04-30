import json
import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from store.models.product import Products
from store.models.orders import Order
from store.models.customer import Customer

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class CreateRazorpayOrder(View):
    def post(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        customer_id = request.session.get('customer')
        if not customer_id:
            return JsonResponse({'error': 'Not logged in'}, status=400)

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if not address or not phone:
            return JsonResponse({'error': 'Address and phone are required'}, status=400)

        products = Products.get_products_by_id(list(cart.keys()))
        amount = sum(product.price * cart[str(product.id)] for product in products)
        amount_paise = int(amount * 100)

        try:
            razorpay_order = razorpay_client.order.create({
                'amount': amount_paise,
                'currency': 'INR',
                'payment_capture': '1',
                'notes': {
                    'customer_id': str(customer_id),
                    'address': address,
                    'phone': phone
                }
            })
            request.session['checkout_info'] = {
                'address': address,
                'phone': phone,
                'razorpay_order_id': razorpay_order['id']
            }
            return JsonResponse({
                'order_id': razorpay_order['id'],
                'amount': amount_paise,
                'currency': 'INR',
                'key': settings.RAZORPAY_KEY_ID,
                'name': 'ZenCommerce',
                'description': f'Order for {len(products)} item(s)'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class PaymentSuccess(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return HttpResponseBadRequest('Invalid request payload')

        razorpay_payment_id = data.get('razorpay_payment_id')
        razorpay_order_id = data.get('razorpay_order_id')
        razorpay_signature = data.get('razorpay_signature')

        if not (razorpay_payment_id and razorpay_order_id and razorpay_signature):
            return JsonResponse({'error': 'Missing payment information'}, status=400)

        params = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            razorpay_client.utility.verify_payment_signature(params)
        except Exception as e:
            return JsonResponse({'error': 'Payment verification failed: ' + str(e)}, status=400)

        cart = request.session.get('cart', {})
        if not cart:
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        checkout_info = request.session.get('checkout_info', {})
        customer_id = request.session.get('customer')
        products = Products.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                customer=Customer(id=customer_id),
                product=product,
                price=product.price,
                address=checkout_info.get('address', ''),
                phone=checkout_info.get('phone', ''),
                quantity=cart.get(str(product.id), 1),
                payment_status='paid',
                payment_id=razorpay_payment_id,
                payment_gateway='razorpay'
            )
            order.save()

        request.session['cart'] = {}
        request.session.pop('checkout_info', None)

        return JsonResponse({'success': True, 'redirect_url': '/store/payment-success/'})

    def get(self, request):
        return render(request, 'payment_success.html')

class PaymentCancel(View):
    def get(self, request):
        return render(request, 'payment_cancel.html')