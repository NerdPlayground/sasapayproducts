import json
import requests
from django.conf import settings
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
            confirmation_callback_url= data.get("ConfirmationURL")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }
            
            payload={
                "MerchantCode": merchant_code,
                "ConfirmationURL": confirmation_callback_url,
            }
            
            response= requests.post(
                "%s" %settings.REGISTER_CONFIRMATION_URL,
                json=payload,
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
            validation_callback_url= data.get("ValidationURL")

            client_token= get_client_token()
            headers= {
                "Authorization": "Bearer %s" %client_token["access_token"]
            }
            
            payload={
                "MerchantCode": merchant_code,
                "ValidationURL": validation_callback_url,
            }
            
            response= requests.post(
                "%s" %settings.REGISTER_VALIDATION_URL,
                json=payload,
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