
from rest_framework.views import APIView
# Create your views here.
from .serializers import stuser
from .models import student
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
class testview(APIView):
    # permission_classes=(IsAuthenticated)
    def get(self,request,*args, **kwargs):
        qs=student.objects.all()
        ser=stuser(qs,many=True)
        return Response(ser.data)
    def post(self,request,*args, **kwargs):
        ser=stuser(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    # from djrestapp import views
    # path('',views.testview.as_view(),name="testview")
