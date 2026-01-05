from django.urls import path,include
from .views import (UserProfileViewSet, CountryViewSet, CityListAPIView, CityDetailAPIView, ServiceViewSet,
                    HotelListAPIView,
                    HotelDetailSerializer, HotelImageViewSet,
                    RoomViewSet, RoomImageViewSet, BookingViewSet, ReviewViewSet, HotelDetailAPIView)
from rest_framework import routers

roter = routers.DefaultRouter()
roter.register(r'user',UserProfileViewSet)
roter.register(r'country',CountryViewSet)
roter.register(r'service',ServiceViewSet)
roter.register(r'hotelImage',HotelImageViewSet)
roter.register(r'room',RoomViewSet)
roter.register(r'roomImage',RoomImageViewSet)
roter.register(r'booking',BookingViewSet)
roter.register(r'review',ReviewViewSet)

urlpatterns = [
    path('',include(roter.urls)),
    path('cities/',CityListAPIView.as_view(),name='city_list'),
    path('cities/<int:pk>',CityDetailAPIView.as_view(),name='city_detail'),
    path('hotels/',HotelListAPIView.as_view(),name='hotel_list'),
    path('hotels/<int:pk>',HotelDetailAPIView.as_view(),name='hotel_detail'),
]