
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .serializers import stuser,seruser
from .models import student
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.permissions import IsAuthenticated
# class testview(APIView):
#     # permission_classes=(IsAuthenticated)
#     def get(self,request):
#         qs=User.objects.all()
#         ser=seruser(qs,many=True)
#         return Response(ser.data)
class createview(APIView):
    def post(self,request):
        ser=seruser(data=request.data)
        if ser.is_valid():
            ser.save()
            u=User.objects.get(username=ser.data['username'])
            token, created = Token.objects.get_or_create(user=u)
            return Response({'status':403,'payload':ser.data,'token':token.key})
        else:
            return Response({'status':403,'errors':ser.errors})
    # from djrestapp import views
    # path('',views.testview.as_view(),name="testview")
class authview(ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        queryset=User.objects.all()
        ser=seruser(queryset,many=True)
        return Response(ser.data)
class genview(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            })
        return Response(
            {
                'error': "user not found"
            }
        )