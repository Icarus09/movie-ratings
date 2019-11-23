from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('starrings', StarringList.as_view(), name=StarringList.name),
    path('starrings/<int:pk>', StarringDetail.as_view(), name=StarringDetail.name),
]