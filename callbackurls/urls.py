from django.urls import path
from callbackurls.views import (
    RegisterValidationURLAPIView,
    RegisterConfirmationURLAPIView
)

urlpatterns= [
    # JSONDecodeError at /register-validation-url/
    path("register-validation-url/",RegisterValidationURLAPIView.as_view(),name="register-validation-url"),
    # JSONDecodeError at /register-confirmation-url/
    path("register-confirmation-url/",RegisterConfirmationURLAPIView.as_view(),name="register-confirmation-url"),
]