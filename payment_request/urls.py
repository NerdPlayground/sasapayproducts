from django.urls import path
from payment_request.views import NumberRequestPaymentAPIView

urlpatterns= [
    path("request-payment-phone-number/",NumberRequestPaymentAPIView.as_view(),name="request-payment-phone-number"),
]