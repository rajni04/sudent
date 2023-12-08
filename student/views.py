from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import ClassDetailSerializer,UserSerializer,UserUpdateSerializer

# Create your views here.
class ClassDetailAPIView(APIView):
    '''Api to create Class data'''
    def post(self, request):
        try:
            serializer = ClassDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message":"Success",
                    "data":serializer.data,
                    },status=status.HTTP_200_OK,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"message":"Something went wrong",
                 "error":str(e)},
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class StudentDetailAPIView(APIView):
    '''Api to create Student Data'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'try1.html'

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                    "data":serializer.data,
                    }
                )
                # return Response(
                #     {"message":"Success",
                #     "data":serializer.data,
                #     },status=status.HTTP_201_CREATED,
                # )
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
        #     return Response(
        #         {"message":"Something went wrong",
        #          "error":str(e)},
        #          status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )

class StudentUpadateAPIView(APIView):
    '''Api to update student data'''
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        try:
            profile=CustomUser.objects.get(id=id)
            print(profile)
            serializer = UserUpdateSerializer(profile,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message":"Successfully Updated",
                    "data":serializer.data,
                    },status=status.HTTP_200_OK,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"message":"Something went wrong",
                 "error":str(e)},
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class LoginAPIView(APIView):
    '''Api to login and create token'''
    def post(self, request):
        try:
            phone_number = request.data.get("phone_number",'')
            password = request.data.get("password",'')
            try:
                if phone_number and password:
                    user = CustomUser.objects.get(phone_number=phone_number,password=password)
                    if user.status==2:
                        token, created = Token.objects.get_or_create(user=user)
                        return Response({"token": token.key,
                                    "user":user.id}, status=200)
                    else:
                        return Response({"message": "User need to be activated",
                                    "user":user.id}, status=404)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User with this phone does not exist.',
                                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"message":"Something went wrong",
                 "error":str(e)},
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )