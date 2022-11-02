from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from rest_framework import filters
# class booksearch(generics.ListAPIView):
#     queryset = models.book.objects.all()
#     ser=serializers.serbook(queryset,many=True)
#     filter_backends=[filters.SearchFilter]
#     search_fields=['title']
    # return Response(ser.data)
class book_view(views.APIView):

    def get(self, request,pk=None):
        id=pk
        if id is not None:
            queryset = models.book.objects.get(id=id)
            ser=serializers.serbook(queryset)
            return Response(ser.data)
        queryset = models.book.objects.all()
        ser=serializers.serbook(queryset,many=True)
        return Response(ser.data)
    def post(self,request):
        ser=serializers.serbook(data=request.data)
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