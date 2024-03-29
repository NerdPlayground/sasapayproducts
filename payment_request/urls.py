from django.urls import path
from payment_request.views import (
    ProcessPaymentAPIView,
    PhoneNumberRequestPaymentAPIView,
    AliasNumberRequestPaymentAPIView,
    TransactionStatusAPIView,
    VerifyTransactionAPIView
)

urlpatterns= [
    path("request-payment-phone-number/",PhoneNumberRequestPaymentAPIView.as_view(),name="request-payment-phone-number"),
    path("request-payment-alias-number/",AliasNumberRequestPaymentAPIView.as_view(),name="request-payment-alias-number"),
    path("process-payment/",ProcessPaymentAPIView.as_view(),name="process-payment"),
    path("transaction-status/",TransactionStatusAPIView.as_view(),name="transaction-status"),
    path("verify-transaction/",VerifyTransactionAPIView.as_view(),name="verify-transaction"),
]