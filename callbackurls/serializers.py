from rest_framework import serializers

class RegisterConfirmationURLSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    ConfirmationCallbackURL= serializers.CharField()

class RegisterValidationURLSerializer(serializers.Serializer):
    MerchantCode= serializers.IntegerField()
    ValidationCallbackURL= serializers.CharField()