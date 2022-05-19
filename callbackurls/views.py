import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from authentication.authentication import get_client_token
from callbackurls.serializers import (
    RegisterValidationURLSerializer,
    RegisterConfirmationURLSerializer,
)

class RegisterConfirmationURLAPIView(GenericAPIView):
    serializer_class= RegisterConfirmationURLSerializer
    def post(self,request):
        data= request.data
        serializer= RegisterConfirmationURLSerializer(data=data)
        if serializer.is_valid():
            merchant_code= data.get("MerchantCode")
            confirmation_callback_url= data.get("ConfirmationCallbackURL")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }
            
            payload={
                "MerchantCode": merchant_code,
                "ConfirmationCallbackURL": confirmation_callback_url,
            }
            
            response= requests.post(
                "https://api.sasapay.me/api/v1/payments/register-ipn-url/",
                data=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_200_OK,
                )
            else:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class RegisterValidationURLAPIView(GenericAPIView):
    serializer_class= RegisterValidationURLSerializer
    def post(self,request):
        data= request.data
        serializer= RegisterValidationURLSerializer(data=data)
        if serializer.is_valid():
            merchant_code= data.get("MerchantCode")
            validation_callback_url= data.get("ValidationCallbackURL")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }
            
            payload={
                "MerchantCode": merchant_code,
                "ValidationCallbackURL": validation_callback_url,
            }
            
            response= requests.post(
                "https://api.sasapay.me/api/v1/payments/register-ipn-url/",
                data=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_200_OK,
                )
            else:
                response= json.loads(response.text)
                return Response(
                    response,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )