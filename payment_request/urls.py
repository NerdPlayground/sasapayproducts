from django.urls import path
from payment_request.views import PhoneNumberRequestPaymentAPIView,AliasNumberRequestPaymentAPIView

urlpatterns= [
    path("request-payment-phone-number/",PhoneNumberRequestPaymentAPIView.as_view(),name="request-payment-phone-number"),
    # JSONDecodeError at /request-payment-alias-number/
    path("request-payment-alias-number/",AliasNumberRequestPaymentAPIView.as_view(),name="request-payment-alias-number"),
]