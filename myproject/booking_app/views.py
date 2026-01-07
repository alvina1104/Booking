from .serializer import (UserProfileListSerializer,UserProfileDetailSerializer,
                         CityListSerializer,CityDetailSerializer,
                         HotelListSerializer,HotelCreateSerializer,
                         HotelDetailSerializer,
                         RoomListSerializer,RoomDetailSerializer,
                         BookingSerializer,ReviewCreateSerializer)
from .models import (UserProfile,City,Hotel,Room,Booking,Review)
from rest_framework import viewsets,generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import HotelPagination, RoomPagination
from .permissions import CheckRolePermissions,CreateHotelPermissions


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['country', 'city', 'hotel_stars']
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']
    pagination_class = HotelPagination

class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer
    permission_classes = [CreateHotelPermissions]

    def get_queryset(self):
        return Hotel.objects.filter(owner=self.request.user)

class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['room_number)']
    ordering_fields = ['price']
    pagination_class = RoomPagination

class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckRolePermissions]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [CheckRolePermissions]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

class ReviewEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [CheckRolePermissions]



