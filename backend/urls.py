from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transports', TransportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('verify-payment/', PaymentVerifyViewSet.as_view({'post': 'create'}), name='verify_payment'),
    path('password-reset/', ForgotPasswordView.as_view(), name='password-reset'),
    path('change_password/', ResetPasswordView.as_view(), name='change_password'),
]
