from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from useraccount.serializers.auth_se import MyTokenObtainPairSerializer 
from useraccount.serializers.auth_se import UserSerializer
from drf_spectacular.utils import extend_schema



@extend_schema(tags=['User Auth'],summary='UserLogin')
class MyTokenObtainPairView(TokenObtainPairView):
    """
    User Login  
    """
    permission_classes=(AllowAny,)
    serializer_class = MyTokenObtainPairSerializer 
    
    
@extend_schema(tags=['User Auth'],summary='UserSignup',request=UserSerializer)
class UserRegisterView(APIView):
    """
    User signup
    
    """
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)