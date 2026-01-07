from django.db import router
from django.urls import path,include

from .serializer import ReviewCreateSerializer
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CityListAPIView, CityDetailAPIView,
                    HotelListAPIView, HotelDetailAPIView,
                    RoomListAPIView, RoomDetailAPIView,
                    BookingViewSet, ReviewCreateAPIView, ReviewEditAPIView,
                    HotelCreateSerializer, HotelViewSet)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'booking',BookingViewSet)
router.register(r'hotel_create',HotelViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('cities/',CityListAPIView.as_view(),name='city_list'),
    path('cities/<int:pk>',CityDetailAPIView.as_view(),name='city_detail'),
    path('hotels/',HotelListAPIView.as_view(),name='hotel_list'),
    path('hotels/<int:pk>',HotelDetailAPIView.as_view(),name='hotel_detail'),
    path('rooms/',RoomListAPIView.as_view(),name='room_list'),
    path('rooms/<int:pk>',RoomDetailAPIView.as_view(),name='room_detail'),
    path('users/',UserProfileListAPIView.as_view(),name='user_list'),
    path('users/<int:pk>',UserProfileDetailAPIView.as_view(),name='user_detail'),
    path('reviews/',ReviewCreateAPIView.as_view(),name='create_review'),
    path('reviews/<int:pk>/',ReviewEditAPIView.as_view(), name= 'edit_review')
]