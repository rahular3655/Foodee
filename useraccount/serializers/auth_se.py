from rest_framework import serializers
from useraccount.models import accounts 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(token)
        # Add custom claims
        token['username'] = user.username
        token['phone_number'] = user.phonenumber
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['is_active'] = user.is_active
        token['is_restaurant'] = user.is_restaurant
        
        return token 
    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(required=True)
    phonenumber = serializers.IntegerField(required = True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(required=True)
    
    def validate (self,data):
        username= data.get('username')
        first_name = data .get('first_name')
        last_name = data.get('last_name')
        email= data.get('email')
        phonenumber = data.get('phonenumber')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if username == "" or None:
            raise serializers.ValidationError("Username can't be empty")
        if accounts.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists,Try different names")
        if not first_name:
            raise serializers.ValidationError("Field can't be empty") 
        if not last_name:
            raise serializers.ValidationError("Field can't be empty")
        if accounts.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists,Try to login")
        if password != confirm_password :
            raise serializers.ValidationError("Password didn't match")
        
        return data
               
    def create(self, validated_data):
        obj = accounts.objects.create(**validated_data)
        _password = validated_data.get("password")
        obj.set_password(_password)
        obj.save()

        return obj