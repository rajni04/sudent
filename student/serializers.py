from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.response import Response
from drf_extra_fields.fields import Base64ImageField
from .models import ClassDetail,CustomUser

class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetail
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    stclass=ClassDetailSerializer(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['is_staff','is_active','date_joined',
                   'user_permissions','groups','is_superuser','status','last_login']

class UserUpdateSerializer(serializers.ModelSerializer):
    stclass=ClassDetailSerializer(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['is_staff','is_active','date_joined','user_permissions','groups','phone_number']

class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetail
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=11, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number','password']

    def validate(self, data):
        print("data----------", data)
        phone_number = data.get("phone_number",None)
        print("phon",phone_number)
        password = data.get("password",None)

        if phone_number and password:
            user= CustomUser.objects.get(phone_number=phone_number,password=password)
            print("user-fff-",user.status)
            #if user.status==2:
                #data['user'] = user
                #print("data",data["user"])
            return user
            #else:
                #return Response({"message": "User need to be activated"},status=404)



