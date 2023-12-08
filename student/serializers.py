from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.response import Response
from .models import ClassDetail,CustomUser
class ClassDetailSerializer(serializers.ModelSerializer):
        #studentclass=ClassDetailSerializer(read_only=True)

    class Meta:
        model = ClassDetail
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    stclass=ClassDetailSerializer(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['is_staff','is_active','date_joined','user_permissions','groups']

class UserUpdateSerializer(serializers.ModelSerializer):
    stclass=ClassDetailSerializer(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['is_staff','is_active','date_joined','user_permissions','groups','phone_number']

class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetail
        fields = '__all__'

