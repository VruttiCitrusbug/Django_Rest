from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.testview.as_view(),name="testview")
]
