from django.urls import path
from callbackurls.views import (
    RegisterValidationURLAPIView,
    RegisterConfirmationURLAPIView
)

urlpatterns= [
    path("register-validation-url/",RegisterValidationURLAPIView.as_view(),name="register-validation-url"),
    path("register-confirmation-url/",RegisterConfirmationURLAPIView.as_view(),name="register-confirmation-url"),
]