from django.urls import path
from business_to_customer.views import B2CPaymentsAPIView

urlpatterns= [
    path("business-to-customer/",B2CPaymentsAPIView.as_view(),name="business-to-customer"),
]