from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
urlpatterns = [
    # path('',views.testview.as_view(),name="testview"),
    path('createview',views.createview.as_view(),name="createview"),
    path('gettoken',views.genview.as_view(),name="genview"),
    path('',views.authview.as_view(),name="authview"),
    # path('gettoken/', obtain_auth_token)
]