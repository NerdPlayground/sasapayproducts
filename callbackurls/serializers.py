from rest_framework import serializers

class RegisterConfirmationURLSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    ConfirmationURL= serializers.CharField()

class RegisterValidationURLSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    ValidationURL= serializers.CharField()