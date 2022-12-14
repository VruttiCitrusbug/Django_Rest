"""apicurd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_view.as_view(),name='book_view'),
    # path('create',views.book_createview.as_view(),name='book_detailview'),
    # path('<int:pk>',views.book_detailview.as_view(),name='book_detailview')
    path('create',views.book_create.as_view(),name='book_create'),
    path('patch/<int:pk>',views.book_patch.as_view(),name='book_patch'),
    path('delete/<int:pk>',views.book_delete.as_view(),name='book_delete'),
    # path('filter/',views.book_filter.as_view(),name='book_filter'),

    path('auther/',views.auther_view.as_view(),name='auther_view'),
    # path('create',views.book_createview.as_view(),name='book_detailview'),
    # path('<int:pk>',views.book_detailview.as_view(),name='book_detailview')
    path('auther/create',views.auther_create.as_view(),name='auther_create'),
    path('auther/patch/<int:pk>',views.auther_patch.as_view(),name='auther_patch'),
    path('auther/delete/<int:pk>',views.auther_delete.as_view(),name='auther_delete'),
    # path('auther/filter/',views.auther_filter.as_view(),name='auther_filter'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
