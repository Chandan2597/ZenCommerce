from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.payment import CreateRazorpayOrder, PaymentSuccess, PaymentCancel
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', store, name='store'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out/', auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
    path('create-payment-order/', auth_middleware(CreateRazorpayOrder.as_view()), name='create_payment_order'),
    path('payment-success/', auth_middleware(PaymentSuccess.as_view()), name='payment_success'),
    path('payment-cancel/', auth_middleware(PaymentCancel.as_view()), name='payment_cancel'),
]
