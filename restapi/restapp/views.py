from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
class book_view(ListAPIView,views.APIView):
    # serializer_class=serializers.serbook
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    pagination_class = LimitOffsetPagination
    queryset = models.book.objects.all()
    serializer_class=serializers.serbook
    filter_backends = [DjangoFilterBackend,OrderingFilter,filters.SearchFilter]
    search_fields = ['title','author__name']
    ordering_fields=['price']
class book_create(views.APIView):
    # permission_classes=[IsAuthenticated]
    def post(self,request):
        data=None
        if request.data!={}:
            data = {
                "title" : request.data['title'],
                "price" : request.data['price'],
                "totalpage": request.data['totalpage'],
                "author": models.auther.objects.get(name=request.data['author']).id
            }
        ser=serializers.serbook(data=data)
        if ser.is_valid():
            ser.save()
            return Response(
                {
                    'payload':request.data,
                    'message':'Created'
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
                {
                    'errors':ser.errors,
                    'message':'Bad Request'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
class book_patch(views.APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request,pk=None):
            id=pk
            queryset = models.book.objects.get(id=id)
            ser=serializers.serbook(queryset)
            return Response(ser.data)
    def patch(self,request,pk):
        id=pk
        if id is not None:
            fatchbook=models.book.objects.get(pk=id)
            ser=serializers.serbook(fatchbook,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response(
                    {
                        'message':'data updated'
                    },
                    status=status.HTTP_204_NO_CONTENT
                )
            return Response(
                    {
                        'errors':ser.errors,
                        'message':'Bad Request'
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
class book_delete(views.APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request,pk=None):
            id=pk
            queryset = models.book.objects.get(id=id)
            ser=serializers.serbook(queryset)
            return Response(ser.data)
    def delete(self,request,pk):
        id=pk
        fatchbook=models.book.objects.get(pk=id)
        fatchbook.delete()
        # ser=serializers.serbook(fatchbook,data=request.data,partial=True)
        return Response(
            {
                'message':'data deleted'
            }
            )

# class book_filter(views.APIView):


# class book_filter(ListAPIView,views.APIView):
# #     # permission_classes=[IsAuthenticated]
#     queryset = models.book.objects.all()
# #     print(queryset,"*------------")
#     serializer_class = serializers.serbook
    
#     filter_backends = [filters.SearchFilter]
    # filter_backends = [DjangoFilterBackend]
#     search_fields=['title']
#     # filterset_fields = ['price']




class auther_view(ListAPIView,views.APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    pagination_class = LimitOffsetPagination
    queryset = models.auther.objects.all()
    serializer_class=serializers.serauther
class auther_create(views.APIView):
    # permission_classes=[IsAuthenticated]
    def post(self,request):
        ser=serializers.serauther(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(
                {
                    'payload':request.data,
                    'message':'Created'
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
                {
                    'errors':ser.errors,
                    'message':'Bad Request'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
class auther_patch(views.APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request,pk=None):
            id=pk
            queryset = models.auther.objects.get(id=id)
            ser=serializers.serauther(queryset)
            return Response(ser.data)
    def patch(self,request,pk):
        id=pk
        if id is not None:
            fatchbook=models.auther.objects.get(pk=id)
            ser=serializers.serauther(fatchbook,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response(
                    {
                        'message':'data updated'
                    },
                    status=status.HTTP_204_NO_CONTENT
                )
            return Response(
                    {
                        'errors':ser.errors,
                        'message':'Bad Request'
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
class auther_delete(views.APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request,pk=None):
            id=pk
            queryset = models.auther.objects.get(id=id)
            ser=serializers.serauther(queryset)
            return Response(ser.data)
    def delete(self,request,pk):
        id=pk
        fatchbook=models.auther.objects.get(pk=id)
        fatchbook.delete()
        # ser=serializers.serbook(fatchbook,data=request.data,partial=True)
        return Response(
            {
                'message':'data deleted'
            },
            status=status.HTTP_202_ACCEPTED
            )
