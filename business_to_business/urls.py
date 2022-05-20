from django.urls import path
from business_to_business.views import B2BPaymentAPIView

urlpatterns= [
    path("business-to-business/",B2BPaymentAPIView.as_view(),name="business-to-business"),
]