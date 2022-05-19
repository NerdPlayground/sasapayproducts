from django.urls import path
from payment_request.views import NumberRequestPaymentAPIView,AliasNumberRequestPaymentAPIView

urlpatterns= [
    path("request-payment-phone-number/",NumberRequestPaymentAPIView.as_view(),name="request-payment-phone-number"),
    # JSONDecodeError at /request-payment-alias-number/
    path("request-payment-alias-number/",AliasNumberRequestPaymentAPIView.as_view(),name="request-payment-alias-number"),
]