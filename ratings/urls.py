from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('starrings', StarringList.as_view(), name=StarringList.name),
    path('starrings/<int:pk>', StarringDetail.as_view(), name=StarringDetail.name),
    path('titles', TitleList.as_view(), name=TitleList.name),
    path('titles/<int:pk>', TitleDetail.as_view(), name=TitleDetail.name),
        path('genders', GenderList.as_view(), name=GenderList.name),
    path('genders/<int:pk>', GenderDetail.as_view(), name=GenderDetail.name),
    path('starring-titles', TitleStarringList.as_view(), name=TitleStarringList.name)
]